const WAVE_LIFE_TIME = 0.3;
const WAVE_MAX_LENGTH = 250;
const WAVE_SPEED = 60;
const WAVE_COLLISION_SAMPLE_COUNT = 5;
const WAVE_HEIGHT = 16;
const WAVE_IMAGES = {
    red: null,
    blue: null,
    yellow: null
};

const EXPLOSION_SPRITE_INFO = {
    image: null,
    frameWidth: 240,
    frameHeight: 188,
    anims: {
        explode: {
            startFrame: 0,
            length: 9,
            frameTime: 1 / 30
        }
    },

    onLoop: function(sprite) {
        removeSprite(sprite)
    }
};

const EXPLOSION_SHAKE_DURATION = 0.2;
const EXPLOSION_SHAKE_MAGNITUDE = 8;

let waves = [];

function initWaves() {
    loadImage("assets/redwave.png", function(image) {
        WAVE_IMAGES.red = image;
    });

    loadImage("assets/bluewave.png", function(image) {
        WAVE_IMAGES.blue = image;
    });

    loadImage("assets/yellowwave.png", function(image) {
        WAVE_IMAGES.yellow = image;
    });

    loadImage("assets/explosion.png", function(image) {
        EXPLOSION_SPRITE_INFO.image = image;
    });
}

function createWave(x, y, dir, color) {
    let wave = {
        x: x,
        y: y,
        color: color,
        timer: WAVE_LIFE_TIME,
        length: 0,
        dir: dir,
        done: false
    };

    waves.push(wave);

    return wave;
}

function updateWaves() {
    for(let i = 0; i < waves.length; ++i) {
        let wave = waves[i];

        if(!wave.done) {
            if(Math.abs(wave.length) > WAVE_MAX_LENGTH) {
                wave.done = true;
                continue;
            }

            for(let j = 0; j < WAVE_COLLISION_SAMPLE_COUNT; ++j) {
                if(collideTileMap(wave.x, wave.y, wave.length, WAVE_HEIGHT)) {
                    wave.done = true;
                    break;
                }

                let e = getFirstCollidingEnemy(wave.x, wave.y, wave.length, WAVE_HEIGHT);
                if(e && e.color == wave.color) {
                    removeEnemy(e);

                    let explosion = createSprite(EXPLOSION_SPRITE_INFO);

                    // Center the explosion
                    explosion.x = e.x + e.sprite.info.frameWidth / 2 - EXPLOSION_SPRITE_INFO.frameWidth / 2;
                    explosion.y = e.y + e.sprite.info.frameHeight / 2 - EXPLOSION_SPRITE_INFO.frameHeight / 2;

                    playAnim(explosion, "explode");

                    shakeCamera(EXPLOSION_SHAKE_DURATION, EXPLOSION_SHAKE_MAGNITUDE);

                    wave.done = true;
                    break;
                }

                wave.length += wave.dir * WAVE_SPEED / WAVE_COLLISION_SAMPLE_COUNT;
            }
        } else {
            if(wave.timer <= 0.1) {
                waves.splice(i, 1);
            }

            wave.timer -= SEC_PER_FRAME;
        }
    }
}

function drawWaves(camera) {  
    for(let i = 0; i < waves.length; ++i) {
        let wave = waves[i];

        const prevAlpha = ctx.globalAlpha;

        ctx.globalAlpha = wave.timer / WAVE_LIFE_TIME;
        if(ctx.globalAlpha < 0) {
            ctx.globalAlpha = 0;
        }

        const waveImage = WAVE_IMAGES[wave.color];

        if(wave.dir < 0) {
            ctx.drawImage(waveImage, wave.x - camera.x + wave.length, wave.y - camera.y, -wave.length, WAVE_HEIGHT);
        } else {
            ctx.drawImage(waveImage, wave.x - camera.x, wave.y - camera.y, wave.length, WAVE_HEIGHT);
        }

        ctx.globalAlpha = prevAlpha;
    }
}

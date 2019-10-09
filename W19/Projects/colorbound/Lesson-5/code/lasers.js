// LASERS!

let lasers = [];

function createLaser(x, y, dir, color) {
    let laser = {
        x: x,
        y: y,
        dir: dir,
        color: color,

        length: 0,
        fadeTimer: 0
    };

    lasers.push(laser);

    return laser;
}

function removeLaser(laser) {
    let i = lasers.indexOf(laser);

    if(i < 0) {
        return;
    }

    lasers.splice(i, 1);
}

const LASER_GROW_RATE = 3000;
const LASER_MAX_LENGTH = 300;
const LASER_FADE_TIME = 0.5;

function updateLasers() {
    for(let i = 0; i < lasers.length; ++i) {
        let laser = lasers[i];

        if(laser.fadeTimer > 0) {
            laser.fadeTimer -= SEC_PER_FRAME;
            if(laser.fadeTimer <= 0) {
                removeLaser(laser);
            }
            continue;
        }

        // SEC_PER_FRAME = 1 / 60

        laser.length += LASER_GROW_RATE * SEC_PER_FRAME;

        if(laser.length >= LASER_MAX_LENGTH) {
            laser.fadeTimer = LASER_FADE_TIME;
        }
    }
}

const LASER_IMAGES = {
    red: loadImage("assets/redwave.png"),
    blue: loadImage("assets/bluewave.png"),
    yellow: loadImage("assets/yellowwave.png")
};

function drawLasers(camera) {
    for(let i = 0; i < lasers.length; ++i) {
        let laser = lasers[i];

        // color has to be "red", "blue", or "yellow"
        const image = LASER_IMAGES[laser.color];

        let prevAlpha = ctx.globalAlpha;

        if(laser.fadeTimer > 0) {
            ctx.globalAlpha = laser.fadeTimer / LASER_FADE_TIME;
        }

        if(laser.dir < 0) {
            ctx.drawImage(image, laser.x - laser.length - camera.x, laser.y - camera.y, 
                          laser.length, image.height);
        } else {
            ctx.drawImage(image, laser.x - camera.x, laser.y - camera.y, laser.length, image.height);
        }

        ctx.globalAlpha = prevAlpha;
    }
}











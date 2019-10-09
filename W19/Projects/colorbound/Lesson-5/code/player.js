let playerImage = loadImage("assets/player.png");

let player = {
    sprite: createSprite({
        image: playerImage,

        frameWidth: 128,
        frameHeight: 128,

        anims: {
            run: {
                startFrame: 6,
                length: 7,
                frameTime: 0.08
            }
        }
    }),

    dx: 0,
    dy: 0,

    hp: 5,
    maxHp: 5,

    laserCooldownTimer: 0
};

player.sprite.x = 100;
player.sprite.y = 200;

playAnim(player.sprite, "run");

const PLAYER_MOVE_SPEED = 6;
const PLAYER_JUMP_ACCEL = 13;
const PLAYER_TERMINAL_VEL = 20;
const PLAYER_GRAVITY = 0.5;
const PLAYER_LASER_COOLDOWN = 0.2;

function playerCreateLaser(color) {
    if(player.laserCooldownTimer > 0) {
        return;
    }

    const dir = player.sprite.flip ? -1 : 1;

    /*
    if(player.sprite.flip) {
        dir = -1;
    } else {
        dir = 1;
    }
    */

    let x = 0;
    let y = 0;

    if(dir > 0) {
        x = player.sprite.x + 100;
        y = player.sprite.y + 50;
    } else {
        x = player.sprite.x + 10;
        y = player.sprite.y + 50;
    }

    createLaser(x, y, dir, color);

    player.laserCooldownTimer += PLAYER_LASER_COOLDOWN;
}

function playerProcessInput() {
    player.grounded = collideTileMap(player.sprite.x, player.sprite.y + 1, 128, 128);

    if(input.left) {
        player.dx = -PLAYER_MOVE_SPEED;
        player.sprite.flip = true;
    } else if(input.right) {
        player.dx = PLAYER_MOVE_SPEED;
        player.sprite.flip = false;
    } else {
        player.dx = 0;
    } 

    if(input.jump && player.grounded) {
        player.dy = -PLAYER_JUMP_ACCEL;

        createRocket(player.sprite.x, player.sprite.y, Math.random() * Math.PI * 2);
    }

    if(input.shootRed) {
        playerCreateLaser("red");
    } else if(input.shootBlue) {
        playerCreateLaser("blue");
    } else if(input.shootYellow) {
        playerCreateLaser("yellow");
    }
}

function updatePlayer() {
    if(player.laserCooldownTimer > 0) {
        player.laserCooldownTimer -= SEC_PER_FRAME;
    }

    player.dy += PLAYER_GRAVITY;

    if(player.dy > PLAYER_TERMINAL_VEL) {
        player.dy = PLAYER_TERMINAL_VEL;
    }

    if(!collideTileMap(player.sprite.x + player.dx, player.sprite.y, 128, 128)) {
        player.sprite.x += player.dx;
    } else {
        player.dx = 0;
    }
    
    if(!collideTileMap(player.sprite.x, player.sprite.y + player.dy, 128, 128)) {
        player.sprite.y += player.dy;
    } else {
        player.dy = 0;
    }
}

const HEART_IMAGE = loadImage("assets/heart.png");
const EMPTY_HEART_IMAGE = loadImage("assets/empty_heart.png");

function drawPlayerHp() {
    for(let i = 1; i <= player.maxHp; ++i) {
        if(i > player.hp) {
            ctx.drawImage(EMPTY_HEART_IMAGE, i * EMPTY_HEART_IMAGE.width - 50, 0);
        } else {
            ctx.drawImage(HEART_IMAGE, i * HEART_IMAGE.width - 50, 0);
        }
    }
}






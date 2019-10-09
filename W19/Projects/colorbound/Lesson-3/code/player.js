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
    dy: 0
};

player.sprite.x = 100;
player.sprite.y = 200;

playAnim(player.sprite, "run");

const PLAYER_MOVE_SPEED = 6;
const PLAYER_JUMP_ACCEL = 13;
const PLAYER_TERMINAL_VEL = 20;
const PLAYER_GRAVITY = 0.5;

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
    }
}

function updatePlayer() {
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

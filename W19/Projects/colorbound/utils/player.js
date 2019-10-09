const PLAYER_MOVE_SPEED = 6;
const PLAYER_SHOOT_COOLDOWN = 0.4;

const PLAYER_GUN_OFFSET = {
    x: 85,
    y: 36
};
const PLAYER_GUN_OFFSET_FLIPPED = {
    x: 34,
    y: 36
};

const CAMERA_SPEED_FACTOR = 0.1;

let player = {
    x: 0,
    y: 0,
    dx: 0,
    dy: 0,
    rect: {
        x: 48,
        y: 0,
        w: 20,
        h: 128
    },
    cooldownTimer: 0
};

function initPlayer(x, y) {
    player.x = x;
    player.y = y;

    loadImage("assets/player.png", function(image) {
        player.sprite = createSprite({
            image: image,
            frameWidth: 128,
            frameHeight: 128,

            anims: {
                idle: {
                    startFrame: 0,
                    length: 1,
                    frameTime: 1
                },
                run: {
                    startFrame: 6,
                    length: 7,
                    frameTime: 0.08
                },
                air: {
                    startFrame: 1,
                    length: 1,
                    frameTime: 1
                }
            }
        });

        playAnim(player.sprite, "idle");
    });
}

function updatePlayer() {
    if(input.left) {
        player.dx = -PLAYER_MOVE_SPEED;
        player.sprite.flip = true;
        playAnim(player.sprite, "run");
    } else if(input.right) {
        player.dx = PLAYER_MOVE_SPEED;
        player.sprite.flip = false;
        playAnim(player.sprite, "run");
    } else {
        player.dx = 0;
        playAnim(player.sprite, "idle");
    }

    if(player.cooldownTimer > 0) {
        player.cooldownTimer -= SEC_PER_FRAME;
    }

    function shoot(color) {
        if(player.cooldownTimer > 0) {
            return;
        }

        const offset = player.sprite.flip ? PLAYER_GUN_OFFSET_FLIPPED : PLAYER_GUN_OFFSET;

        createWave(player.x + offset.x, player.y + offset.y, player.sprite.flip ? -1 : 1, color);
        player.cooldownTimer += PLAYER_SHOOT_COOLDOWN;
    }

    if(input.shootRed) {
        shoot("red");
    } else if(input.shootBlue) {
        shoot("blue");
    } else if(input.shootYellow) {
        shoot("yellow");
    }

    let playerRect = player.rect;
    player.grounded = collideTileMap(player.x + player.rect.x, player.y + player.rect.y + 1, player.rect.w, player.rect.h);

    if(!player.grounded) {
        player.dy += 0.2;
        playAnim(player.sprite, "air");
    } else {
        if(input.jump) {
            player.grounded = false;
            player.dy -= 8;
        }
    }

    moveCollideTileMap(player, true);

    player.sprite.x = player.x;
    player.sprite.y = player.y;

    let cx = player.x - canvas.width / 2 + playerRect.x + playerRect.w / 2
    let cy = player.y - canvas.height / 2 + playerRect.y + playerRect.h / 2;

    camera.x += (cx - camera.x) * CAMERA_SPEED_FACTOR;
    camera.y += (cy - camera.y) * CAMERA_SPEED_FACTOR;
}

function debugDrawPlayer(camera) {  
    if(!player.sprite) {
        return;
    }

    const offset = player.sprite.flip ? PLAYER_GUN_OFFSET_FLIPPED : PLAYER_GUN_OFFSET;

    ctx.fillStyle = "red";
    ctx.fillRect(player.x + offset.x - camera.x, player.y + offset.y - camera.y, 4, 4);
}

const ENEMY_RADIUS = 20;
const ENEMY_REPULSION_ACCEL = 5;
const ENEMY_RECT = {
    x: 41,
    y: 18,
    w: 58,
    h: 87
};
const ENEMY_SPRITE_INFO = {
    red: {
        frameWidth: 128,
        frameHeight: 128,

        anims: {
            idle: {
                startFrame: 0,
                length: 1,
                frameTime: 1
            }
        }
    }
};

let enemies = [];

function initEnemies() {
    loadImage("assets/redenemy.png", function(image) {
        ENEMY_SPRITE_INFO.red.image = image;
    });
}

function getFirstCollidingEnemy(x, y, w, h) {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        if(collideRects(x, y, w, h,
                        enemy.x + enemy.rect.x, enemy.y + enemy.rect.y, enemy.rect.w, enemy.rect.h)) {
            return enemy;
        }
    }

    return null;
}

function createEnemy(x, y, color) {
    let enemy = {
        x: x,
        y: y,
        dx: 0,
        dy: 0,
        sprite: createSprite(ENEMY_SPRITE_INFO[color]),
        rect: ENEMY_RECT,
        color: color
    };

    playAnim(enemy.sprite, "idle");

    enemies.push(enemy);

    return enemy;
}

function removeEnemy(e) {
    let i = enemies.indexOf(e);

    if(i < 0) {
        return;
    }

    removeSprite(enemies[i].sprite);
    enemies.splice(i, 1);
}

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        for(let j = i + 1; j < enemies.length; ++j) {
            let otherEnemy = enemies[j];

            if(!collideCircles(enemy.x, enemy.y, ENEMY_RADIUS, 
                              otherEnemy.x, otherEnemy.y, ENEMY_RADIUS)) {
                continue;
            }

            const angle = Math.atan2(enemy.y - otherEnemy.y, enemy.x - otherEnemy.x);
            const c = Math.cos(angle);
            const s = Math.sin(angle);

            enemy.dx += c * ENEMY_REPULSION_ACCEL / 2;
            enemy.dy += s * ENEMY_REPULSION_ACCEL / 2;
            otherEnemy.dx -= c * ENEMY_REPULSION_ACCEL / 2;
            otherEnemy.dy -= s * ENEMY_REPULSION_ACCEL / 2;
        }

        enemy.dx *= 0.92;
        enemy.dy *= 0.92;

        const angle = Math.atan2(player.y - enemy.y, player.x - enemy.x);

        enemy.dx += Math.cos(angle) * 0.2;
        enemy.dy += Math.sin(angle) * 0.2;

        moveCollideTileMap(enemy);

        enemy.sprite.flip = player.x < enemy.x;

        enemy.sprite.x = enemy.x;
        enemy.sprite.y = enemy.y;
    }
}

function debugDrawEnemies(camera) {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        ctx.fillStyle = "red";
        ctx.fillRect(enemy.x + enemy.rect.x - camera.x, enemy.y + enemy.rect.y - camera.y, enemy.rect.w, enemy.rect.h);
    }
}

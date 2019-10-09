let enemies = [];

function createEnemy(x, y) {
    let enemy = {
        sprite: createSprite({
            image: loadImage("assets/redenemy.png"),

            frameWidth: 128,
            frameHeight: 128,

            anims: {
                idle: {
                    startFrame: 0,
                    length: 1,
                    frameTime: 1
                }
            }
        }),

        dx: 0,
        dy: 0
    };

    enemy.sprite.x = x;
    enemy.sprite.y = y;

    enemies.push(enemy);

    return enemy;
}

function removeEnemy(enemy) {
    let i = enemies.indexOf(enemy);

    if(i < 0) {
        return;
    }

    removeSprite(enemy.sprite);

    enemies.splice(i, 1);
}

const ENEMY_MOVE_ACCEL = 0.3;
const ENEMY_CHASE_RADIUS = 300;
const ENEMY_DRAG_FACTOR = 0.94;
const ENEMY_RADIUS = 64;
const ENEMY_REPLUSION_ACCEL = 5;

// ax, ay = center of first circle
// ar = radius of first circle
// bx, by = center of second circle
// br = radius of second circle
function collideCircles(ax, ay, ar, bx, by, br) {
    const distX = bx - ax;
    const distY = by - ay;

    // We use the same trick as above to avoid square root: compare
    // squared distances  
    return distX * distX + distY * distY < (ar + br) * (ar + br);
}

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        const distX = player.sprite.x - enemy.sprite.x;
        const distY = player.sprite.y - enemy.sprite.y;

        if(enemy.sprite.x > player.sprite.x) {
            enemy.sprite.flip = true;
        } else {
            enemy.sprite.flip = false;
        }

        enemy.sprite.x += enemy.dx;
        enemy.sprite.y += enemy.dy;

        enemy.dx *= ENEMY_DRAG_FACTOR;
        enemy.dy *= ENEMY_DRAG_FACTOR;

        for(let j = 0; j < enemies.length; ++j) {
            if(i == j) {
                continue;
            }

            let otherEnemy = enemies[j];

            if(collideCircles(enemy.sprite.x, enemy.sprite.y, ENEMY_RADIUS,
                              otherEnemy.sprite.x, otherEnemy.sprite.y, ENEMY_RADIUS)) {
                const distX = enemy.sprite.x - otherEnemy.sprite.x;
                const distY = enemy.sprite.y - otherEnemy.sprite.y;
                
                const angle = Math.atan2(distY, distX);

                const ddx = Math.cos(angle) * ENEMY_REPLUSION_ACCEL;
                const ddy = Math.sin(angle) * ENEMY_REPLUSION_ACCEL;

                enemy.dx += ddx;
                enemy.dy += ddy;

                otherEnemy.dx -= ddx;
                otherEnemy.dy -= ddy;
            }
        }

        if((distX * distX + distY * distY) > ENEMY_CHASE_RADIUS * ENEMY_CHASE_RADIUS) {
            const angle = Math.atan2(distY, distX);

            enemy.dx += Math.cos(angle) * ENEMY_MOVE_ACCEL;
            enemy.dy += Math.sin(angle) * ENEMY_MOVE_ACCEL;
        }
    }
}








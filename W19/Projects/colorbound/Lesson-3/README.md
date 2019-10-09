# Meet-Up #3 Agenda:

**Objective**: Refactor code into separate files, and introduce enemies.

## 1. Refactoring
Right now, all the logic relating to the player is located in `loop.js`. As our game gets more complex, it will be difficult to find and modify the appropriate logic if we were to place it all in this one file. Let's move it to another file called `player.js`

```js
// player.js

let player = {
    sprite: createSprite({
        image: loadImage("assets/player.png"),

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

    grounded: false
};

function playerProcessInput() {
    player.grounded =  collideTileMap(player.sprite.x, player.sprite.y + 1, 128, 128);
    
    if(input.left) {
        player.dx = -4;
        player.sprite.flip = true;        
    } else if(input.right) {
        player.dx = 4;
        player.sprite.flip = false;
    } else {
        player.dx = 0;
    }
}

function updatePlayer() {
    player.dy += 0.3;

    if(player.dy > 15) {
        player.dy = 15;
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
```

While we're at it, let's also separate our input state and event handlers into a separate file called `input.js`

```js
// input.js

let input = {
    left: false,
    right: false,
    jump: false
};

window.addEventListener("keydown", function(e) {
    if(e.key == "a") {
        input.left = true;
    } else if(e.key == "d") {
        input.right = true;
    } else if(e.key == "w") {
        input.jump = true;
    }
});

window.addEventListener("keyup", function(e) {
    if(e.key == "a") {
        input.left = false;
    } else if(e.key == "d") {
        input.right = false;
    } else if(e.key == "w") {
        input.jump = false;
    }
});
```

Cool, now our `loop.js` is greatly simplified:

```js

let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

function processInput() {
    playerProcessInput();
}

function update() {
    updatePlayer();
    updateSprites();
}

function draw() {
    const camera = {
        x: 0,
        y: 0
    };

    drawTilemap(camera);
    drawSprites(camera);
}

function loop() {
    if(!areAllAssetsLoaded()) {
        processInput();
        update();
        draw();
    }

    requestAnimationFrame(loop);
}

loop();
```

Make sure you update `index.html` accordingly!

## 2. Enemies!
Enemies in Colorbound are relatively simple and homogenous, but they're still very fun to fight because they tend to swarm the player.

Let's play the game a little to get a feel for how the enemies behave:

https://goodpaul6.itch.io/colorbound

Their behavior is very simple: follow the player until you're within firing range, and then fire. Also, enemies bounce off of each other once they get close enough.

As such, enemies can be thought of as having 2 "states". The reason why I make this clear is because we are essentially going to be implementing what's called a "State Machine" for the AI.

State machines can be used to represent complex execution flows where only one action can be performed at a given time. Complexity is introduced by providing transitions between states; in our case, the enemy transitions from the "chasing player" state to the "firing rocket" state once it's close enough.

However, before we implement the AI, let's just get the enemies displaying and following the player:

### Simple Enemy

```js
// enemies.js

// Like I mentioned in the previous lesson, since
// all the enemy sprites share the same animations, we will
// store them in a single object here
const ENEMY_ANIMS = {
    // This is a placeholder; you can add more animations as you see fit
    idle: {
        startFrame: 0,
        length: 1,
        frameTime: 1
    }
};

// The 3 enemies share very similar sprite information
// the only difference being the image. As such, we store
// them in a single object here, identified by color.
// This way, we can look them up later by doing ENEMY_SPRITE_INFO[color]
const ENEMY_SPRITE_INFO = {
    red: {
        image: loadImage("assets/redenemy.png"),

        frameWidth: 128,
        frameHeight: 128,
        
        anims: ENEMY_ANIMS
    },
    
    blue: {
        image: loadImage("assets/blueenemy.png"),
        
        frameWidth: 128,
        frameHeight: 128,
    
        anims: ENEMY_ANIMS
    },

    yellow: {
        image: loadImage("assets/yellowenemy.png"),
        
        frameWidth: 128,
        frameHeight: 128,
        
        anims: ENEMY_ANIMS
    }
};

const ENEMY_MOVE_SPEED = 5;

// We will store all enemy objects in this array
let enemies = [];

function createEnemy(x, y, color) {
    let enemy = {
        sprite: createSprite(ENEMY_SPRITE_INFO[color]), 
        color: color,
        dx: 0,
        dy: 0
    };

    playAnim(enemy.sprite, "idle");

    enemy.sprite.x = x;
    enemy.sprite.y = y;

    // This adds our enemy object to the end of the array
    enemies.push(enemy);
    
    return enemy;
}

function removeEnemy(enemy) {
    // This will loop through the enemies array and find
    // the index at which the given enemy is located; it will
    // produce -1 if it doesn't exist
    let index = enemies.indexOf(enemy); 

    if(index < 0) {
        // This enemy doesn't exist in the array; don't bother
        return;
    }
    
    // splice(index, count) removes count elements from the array starting at the given index
    // Here we are removing the one enemy 
    enemies.splice(index, 1);
}

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        // Get the angle between the player and the enemy
        // Math.atan2 is just like arctan except it works for all
        // 4 quadrants of the unit circle. 
        // TODO: More/visual explanation
        const angle = Math.atan2(player.sprite.y - enemy.sprite.y, player.sprite.x - enemy.sprite.x);

        enemy.dx = Math.cos(angle) * ENEMY_MOVE_SPEED;
        enemy.dy = Math.sin(angle) * ENEMY_MOVE_SPEED;
        
        enemy.sprite.x += enemy.dx;
        enemy.sprite.y += enemy.dy;
    }
}
```

Now let's actually add an enemy to our level and watch it follow our player.
Where should this enemy creation code go? It can't be in any of the functions inside
the game loop since it should only be run once at the start of the game.
Well, we initially start the game loop by calling the `loop` function at the
bottom of `loop.js`. Let's just create another function that holds all the initialization
logic for our game and call it before `loop`.

```js
// loop.js

function init() {
    createEnemy(100, 100, "red");    
}

// Other code

function update() {
    updatePlayer();
    updateEnemies();
}

// Other code

init();
loop();
```

Great! If we run the game, we should see a red enemy that moves directly towards the player. However, it doesn't always face the player. I'm going to let you figure out how to fix this :) (Hint: `sprite.flip`).

### Bouncy Boi

You might also be wondering why I decided to include the `dx` and `dy` for the enemy even though it's always moving at a constant velocity towards the player. The reason why is because we want to change that behaviour so that the enemy _accelerates_ towards the player and slows down when near. Furthermore, we want the enemies bouncing off of each other. Generally speaking, as soon as we introduce any concept of acceleration, we must keep track of velocity in some manner.

So how can we go about implementing the acceleration/deceleration? It is actually surprisingly simple. Fundamentally, decelerating the enemy is just reducing its speed in the direction it is going. Cool, so we can just subtract from the enemy's `dx` and `dy` until they reach 0, right? Well, technically, yes, that works (but you must handle the case where the dx and dy are negative as well as when they're less than the constant you're subtracting), however, it doesn't feel very good. It doesn't quite mimic how things slow down in the real world.

In the _real world_, the drag on an object is proportional to the (square of) its velocity. In other words, the faster the object moves, the more drag it experiences (and thus greater decelerative forces). Since our enemies fly through the air, it'd be great to simulate something similar for them.

How do we do this? It's simple, we just multiply their velocity by a factor < 1 every frame.
This, in essence, applies a deceleration that's proportional to the magnitude of their velocity; furthermore, it's much simpler to write than the other approach. Let's implement it!

```js
// enemies.js

// Replace ENEMY_MOVE_SPEED with ENEMY_ACCEL to be more descriptive
const ENEMY_ACCEL = 2;

const ENEMY_DRAG_FACTOR = 0.9;

const ENEMY_CLOSE_ENOUGH_DISTANCE = 200;

// Other code

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        const distX = player.sprite.x - enemy.sprite.x;
        const distY = player.sprite.y - enemy.sprite.y;
        
        // Compute the square of the euclidean (straight line) distance
        const dist2 = (distX * distX) + (distY * distY);
        
        // Only accelerate the enemy if they're too far to shoot
        // Notice how we square the distance before comparing; this is because
        // we computed the square of the distance, not the actual distance above
        // Doing this saves us a square root operation
        if(dist2 < ENEMY_CLOSE_ENOUGH_DISTANCE * ENEMY_CLOSE_ENOUGH_DISTANCE) {
            // Get the angle between the player and the enemy
            // Math.atan2 is just like arctan except it works for all
            // 4 quadrants of the unit circle. 
            // TODO: More/visual explanation
            const angle = Math.atan2(distY, distX);

            enemy.dx += Math.cos(angle) * ENEMY_ACCEL;
            enemy.dy += Math.sin(angle) * ENEMY_ACCEL;
        }

        enemy.sprite.x += enemy.dx;
        enemy.sprite.y += enemy.dy;

        // Decelerate the enemy
        enemy.dx *= ENEMY_DRAG_FACTOR;
        enemy.dy *= ENEMY_DRAG_FACTOR;
    }
}
```

Perfect! The enemies should now be moving smoothly until they get within 200 pixels of the player, at which point they slow down. Let's think about implementing the enemy bounce now.

Here's a diagram that hopefully provides some intuition:

![Alt text](../assets/circle_diagram.png?raw=true "Enemy bounce")

First of all, in order to determine if two circles are overlapping, we can check if the distance between their centers is < radius of the first + radius of the second.

This is generally useful, so let's write a function to do this check:

```js
// util.js

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
```

Nice! Now as far as implementing the bounce goes, the diagram gives us a clue. 
Much like we did for the enemy navigating to the player, we can get the angle between
two enemies and use that to produce a force vector repelling them. 

Note that the angle produced depends on the direction of the difference vector between the
two positions. In other words, the angle of (a - b) is different from (b - a). Moving in the angle of (a - b) moves _towards_ a, whereas (b - a) would move _away_ from a.

Let's keep that in mind as we implement this

```js
// enemies.js

// Other code

// I haven't thought any of the constants through
const ENEMY_REPULSION_ACCEL = 5;
const ENEMY_RADIUS = 64;

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        // Compare against every other enemy for collision
        // notice we start at i + 1 and not 0. This is because
        // Every enemy before this one will already have compared
        // itself with us, so we skip them. 
        for(let j = i + 1; j < enemies.length; ++j) {
            let otherEnemy = enemies[j];

            // I am adding sprite.info.frameWidth / 2 to the sprite position
            // so we are at the center of the sprite
            const fw2 = enemy.sprite.info.frameWidth / 2;
            const fh2 = enemy.sprite.info.frameHeight / 2;

            if(collideCircles(enemy.sprite.x + fw2, enemy.sprite.y + fh2, ENEMY_RADIUS,
                        otherEnemy.sprite.x + fw2, otherEnemy.sprite.y + fh2, ENEMY_RADIUS)) {
                const distX = (enemy.sprite.x + fw2) - (otherEnemy.sprite.x + fw2);
                const distY = (enemy.sprite.y + fh2) - (otherEnemy.sprite.y + fh2);

                // Since we did (enemy - otherEnemy) for the distance above,
                // this angle will move in the direction of enemy.
                const angle = Math.atan2(distY, distX);

                // We only compute this once
                const ddx = Math.cos(angle) * ENEMY_REPULSION_ACCEL;
                const ddy = Math.sin(angle) * ENEMY_REPULSION_ACCEL;

                enemy.dx += ddx;
                enemy.dy += ddy;
                
                otherEnemy.dx -= ddx;
                otherEnemy.dy -= ddy;
            }
        }

        const distX = player.sprite.x - enemy.sprite.x;
        const distY = player.sprite.y - enemy.sprite.y;

        // Compute the square of the euclidean (straight line) distance
        const dist2 = (distX * distX) + (distY * distY);

        // Only accelerate the enemy if they're too far to shoot
        // Notice how we square the distance before comparing; this is because
        // we computed the square of the distance, not the actual distance above
        // Doing this saves us a square root operation
        if(dist2 < ENEMY_CLOSE_ENOUGH_DISTANCE * ENEMY_CLOSE_ENOUGH_DISTANCE) {
            // Get the angle between the player and the enemy
            // Math.atan2 is just like arctan except it works for all
            // 4 quadrants of the unit circle. 
            // TODO: More/visual explanation
            const angle = Math.atan2(distY, distX);

            enemy.dx += Math.cos(angle) * ENEMY_ACCEL;
            enemy.dy += Math.sin(angle) * ENEMY_ACCEL;
        }

        enemy.sprite.x += enemy.dx;
        enemy.sprite.y += enemy.dy;

        // Decelerate the enemy
        enemy.dx *= ENEMY_DRAG_FACTOR;
        enemy.dy *= ENEMY_DRAG_FACTOR;
    }
}

```

And there you have it! Enemies that follow the player until they're close, and repel against each other.

### State Machine

So we were discussing creating a state machine to represent the enemy. There are many ways we can do this, but the approach I'll be using is having a function for each state and then cycling between them as needed. We can store the function in a property on the enemy object itself. Let's do this:

```js
// enemies.js

// Other code

function enemyChasePlayer(enemy) { 
    const distX = player.sprite.x - enemy.sprite.x;
    const distY = player.sprite.y - enemy.sprite.y;

    // Compute the square of the euclidean (straight line) distance
    const dist2 = (distX * distX) + (distY * distY);

    if(dist2 < ENEMY_CLOSE_ENOUGH_DISTANCE * ENEMY_CLOSE_ENOUGH_DISTANCE) {
        // The enemy is close enough, transition to the rocket firing state
        enemy.state = enemyFireRockets;
        return;
    }

    const angle = Math.atan2(distY, distX);

    enemy.dx += Math.cos(angle) * ENEMY_ACCEL;
    enemy.dy += Math.sin(angle) * ENEMY_ACCEL;
}

function enemyFireRockets(enemy) {
    const dist2 = (distX * distX) + (distY * distY);

    if(dist2 > ENEMY_CLOSE_ENOUGH_DISTANCE * ENEMY_CLOSE_ENOUGH_DISTANCE) {
        // The enemy is too far to shoot the player, start chasing again
        enemy.state = enemyChasePlayer;
        return;
    }

    // TODO: Implement this once we have rockets
}

function createEnemy(x, y, color) {
    // Other code
    enemy.state = enemyChasePlayer;

    return enemy;
}

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        let enemy = enemies[i];

        for(let j = i + 1; j < enemies.length; ++j) {
            let otherEnemy = enemies[j];

            const fw2 = enemy.sprite.info.frameWidth / 2;
            const fh2 = enemy.sprite.info.frameHeight / 2;

            if(collideCircles(enemy.sprite.x + fw2, enemy.sprite.y + fh2, ENEMY_RADIUS,
                        otherEnemy.sprite.x + fw2, otherEnemy.sprite.y + fh2, ENEMY_RADIUS)) {
                const distX = (enemy.sprite.x + fw2) - (otherEnemy.sprite.x + fw2);
                const distY = (enemy.sprite.y + fh2) - (otherEnemy.sprite.y + fh2);

                // Since we did (enemy - otherEnemy) for the distance above,
                // this angle will move in the direction of enemy.
                const angle = Math.atan2(distY, distX);

                // We only compute this once
                const ddx = Math.cos(angle) * ENEMY_REPULSION_ACCEL;
                const ddy = Math.sin(angle) * ENEMY_REPULSION_ACCEL;

                enemy.dx += ddx;
                enemy.dy += ddy;

                otherEnemy.dx -= ddx;
                otherEnemy.dy -= ddy;
            }
        }

        // Instead of doing all the logic in here, we just call
        // the state function (if it exists)
        if(enemy.state) {
            enemy.state(enemy);
        }

        enemy.sprite.x += enemy.dx;
        enemy.sprite.y += enemy.dy;

        // Decelerate the enemy
        enemy.dx *= ENEMY_DRAG_FACTOR;
        enemy.dy *= ENEMY_DRAG_FACTOR;
    }
}
```

So the behaviour of enemies remains the same as before, but now we can add more complexity to the AI easily by adding more states. For example, if the enemy is chasing the player and the player fires their gun, we can transition to an avoidance state for a bit of time.

Anyways, that's gonna do it for this lesson. Please feel free to message the Slack if you have any questions!

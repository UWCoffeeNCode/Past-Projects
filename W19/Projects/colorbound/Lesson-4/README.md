## Meet-Up #4 Agenda:

**Objective**: Give the player some health and have the enemies fire rockets that explode and hurt the player.

## 1. Player Health
Having refactored the player code into a separate file, we don't have to worry about where we're going to put this code; it belongs in the player file of course!

So in the original game, the player has a maximum health as well as a current health value.
This very simple system can be represented by adding these two properties to the player object, so that's what we'll do:

```js
// player.js

let player = {
    // other properties
    
    maxHp: 5,
    hp: 5
};
```

Now we must display this to the user in some way. Since the maximum amount of hp is relatively limited (and more importantly, it's an integer), we'll use heart containers to display it:

![Alt text](hp_bar.png?raw=true "Health")

Recall from our very first lesson that we could draw images directly to the screen using `ctx.drawImage(image, x, y)`. That's exactly what we're going to do here. Let's create another function draw drawing the player health.

```js
// player.js

const HEART_IMAGE = loadImage("assets/heart.png");
const EMPTY_HEART_IMAGE = loadImage("assets/empty_heart.png");

const HEART_DRAW_OFFSET_X = 10;
const HEART_DRAW_OFFSET_Y = 10;

function drawPlayerHp() {
    for(let i = 0; i < player.maxHp; ++i) {
        const x = HEART_DRAW_OFFSET_X + i * HEART_IMAGE.width;
        const y = HEART_DRAW_OFFSET_Y;

        if(i > player.hp) {
            ctx.drawImage(EMPTY_HEART_IMAGE, x, y);
        } else {
            ctx.drawImage(HEART_IMAGE, x, y);
        }
    }
}
```

Now, we head back to `loop.js` and call this function after drawing the tilemap and the sprites:

```js
// loop.js

function draw() {
    // Other code
    drawPlayerHp();
}
```

Notice how we didn't pass in the camera position as a parameter. This is because the player HP display is always drawn in the same location on the screen regardless of where the camera is.

Now run the game. Ta-da! That's basically it. Open up the JavaScript console in your browser and mess with `player.health` (ex. set it to a value < maxHp) and see the display change.

## 2. Rockets
So right now enemies don't really do much other than chase the player and bounce off of each other. Let's get them to fire rockets at the player! 

Now although rockets are only going to be fired by enemies, they are a separate entity altogether from them, so we'll be placing all their code in a separate file.

```js
// rockets.js

// Since there are many rockets, we keep track of them with an array (much like enemies)
let rockets = [];

const ROCKET_MOVE_SPEED = 8;

function createRocket(x, y, angle) {
    let rocket = {
        x: x,
        y: y,
        angle: angle,
        dx: Math.cos(angle) * ROCKET_MOVE_SPEED;
        dy: Math.sin(angle) * ROCKET_MOVE_SPEED;
    };

    rockets.push(rocket);

    return rocket;
}

// Pretty much exactly like removeEnemy but with rockets
function removeRocket(rocket) {
    let i = rockets.indexOf(rocket);

    if(i < 0) {
        return;
    }

    rockets.splice(i, 1);
}
```

So this is different from the entities we've created thus far because it doesn't make use of a sprite; rockets aren't animated after all.As such, we'll have to write our own `draw` function for rockets.

Notice also how I compute the velocity of the rocket immediately from the angle (and recall from last lesson that to go from an angle to a vector, you do `(Math.cos(angle) * length, Math.sin(angle) * len)` to produce the x and y components respectively). This is fine because the rocket's velocity is constant; there's no point in computing it every frame.

So why then do I store the angle of the rocket? Well, the rocket images need to be rotated to point in the direction of the angle. But before we do that, let's get the rockets moving.

```js
// rockets.js

function updateRockets() {
    for(let i = 0; i < rockets.length; ++i) {
        let rocket = rockets[i];

        rocket.x += rocket.dx;
        rocket.y += rocket.dy;

        // check if the rocket hit a wall

        // TODO(You): fill in appropriate values for the rocket collision rectangle
        if(collideTileMap(rocket.x + ROCKET_COLLISION_OFFSET_X,
                          rocket.y + ROCKET_COLLISION_OFFSET_Y,
                          ROCKET_COLLISION_W,
                          ROCKET_COLLISION_H)) {
            // TODO(Us): Explosion!
            removeRocket(rocket);
        }

        // TODO(Us): Check to see if we hit the player
    }
}
```

Pretty simple so far. Notice the `// TODO(Us): Check to see if we hit the player`. We're gonna need to check the rectangle of the player against the rectangle of the rocket. We should probably store the player rectangle somewhere; and since it never changes (at least not relative to the player's sprite position), let's make a constant for it:

```js
// player.js

const PLAYER_RECT = {
    // TODO(You): Pick good numbers
    x: 40,
    y: 0,
    w: 20,
    h: 128
};

// TODO(You): Replace all calls to collideTileMap(player.sprite.x, player.sprite.y, 128, 128) with
// collideTileMap(player.sprite.x + PLAYER_RECT.x, player.sprite.y + PLAYER_RECT.y, PLAYER_RECT.w, PLAYER_RECT.h)
```

Ok, back to rockets. Let's create a rectangle for them too.

```js
// rockets.js

const ROCKET_RECT = {
    // TODO(You): Pick good numbers for this
    x: 0,
    y: 0,
    w: 64,
    h: 64
};

// TODO(You): Add debug visualization for the rockets as well (i.e. draw their rectangles)
```

### Debug Visualization

I would also recommend that you add a new function to a file called `debug.js` that draws these rectangles to the screen
so you can visualize them more easily.

```js
// debug.js

function debugDraw(camera) {
    // Recall this is how we draw filled rectangles to the screen
    ctx.fillStyle = "red";
    ctx.fillRect(player.sprite.x + PLAYER_RECT.x - camera.x,
                 player.sprite.y + PLAYER_RECT.y - camera.y,
                 PLAYER_RECT.w,
                 PLAYER_RECT.h);
}
```

And then we can call this function in our `loop.js` before drawing sprites so we can see the rectangles beneath them.

```js
// loop.js

function draw() {
    // Before drawSprites()
    debugDraw(camera);
    // Rest of the code
}
```

When we are done with the game or if we want to get rid of the rectangles to see what it looks like, just comment out `debugDraw()`.

### Rectangle collision
Recall that in our last lesson we created a function called `collideCircles` that checks if two circles are overlapping. We're going to create a similar function for rectangles because, as you can see, we're gonna need it for rockets (and it'll be useful elsewhere as well).

```js
// util.js

function collideRects(ax, ay, aw, ah, bx, by, bw, bh) {
    // Check if not they're touching in the x-axis
    // If not, return false. Do the same for the y-axis.
    // If we're overlapping on all axes, then there's a collision,
    // so return true.

    if(ax + aw < bx || bx + bw < ax) return false;
    if(ay + ah < by || by + bh < ay) return false;

    return true;
}
```

Let's use this to check if we're touching the player.

```js
// rockets.js

function updateRockets() {
    for(let i = 0; i < rockets.length; ++i) {
        let rocket = rockets[i];

        // Other code

        if(collideRects(rocket.x + ROCKET_RECT.x, rocket.y + ROCKET_RECT.y,
                        ROCKET_RECT.w, ROCKET_RECT.h,
                        player.sprite.x + PLAYER_RECT.x, player.sprite.y + PLAYER_RECT.y,
                        PLAYER_RECT.w, PLAYER_RECT.h)) {
            // TODO(Us): create explosion

            // Let's hurt the player
            player.hp -= 1;
            removeRocket(rocket);
        }
    }
}
```

Once we get the rockets firing, the player should get hurt upon contact with them.

### Getting the rockets on the screen

Now let's just draw the rockets to the screen without any rotation so we can try them out. This is something we already know how to do:

```js
// rockets.js

const ROCKET_IMAGE = loadImage("assets/rocket.png");

function drawRockets(camera) {
    for(let i = 0; i < rockets.length; ++i) {
        let rocket = rockets[i];

        ctx.drawImage(ROCKET_IMAGE, rocket.x - camera.x, rocket.y - camera.y);
    }
}
```

And then in `loop.js`:

```js
// loop.js

function draw() {
    // After drawSprites() (because we want to always be able to see rockets even if there's tonnes of enemies)
    drawRockets(camera);
}
```

To test rockets it without writing any AI code, let's just create a rocket near the player whenever they jump:

```js
// player.js

function processInput() {
    // Other code...

    if(input.jump && player.grounded) {
        player.dy = -PLAYER_JUMP_ACCEL;
        
        // Create a rocket with a random angle (Math.random() produces a value between 0 and 1, so
        // the resulting angle will be between 0 and 2pi)
        createRocket(player.sprite.x, player.sprite.y, Math.random() * 2 * Math.PI);
    }
}
```

Ayy lmao there we go! We got rockets, they just look dumb because they don't face the direction they're travelling. 

### Canvas Transformations
So how do we make the rockets face where they're going? Well, we have yet to draw any rotated images, so let's discuss how we can do such transformations in HTML5 Canvas.

```js
// The canvas context stores the transformation state in a "matrix"
// We don't really care about that though. What's important is that 
// once we apply a transformation, it persists for all draw operations.
// So if we apply a translation to the context, all following "drawX"s will
// be translated by that amount. So how to we reset those transformations?
// Well, we call a function called "save()" on the context that will save
// the current transformation state and then call "restore()" when we want to
// switch back to it.

ctx.save();

ctx.translate(x, y);
// All the following operations will happen at (x, y)

ctx.rotate(angle);
// All the following operations will happen at (x, y) and be rotated by the angle

// We are drawing the image at (-image.width / 2, -image.height / 2) but remember that
// it's actually drawing at (x - image.width / 2, y - image.height / 2). Hence, we're
// essentially drawing the image rotated about its center and positioned at (x, y)

ctx.drawImage(image, -image.width / 2, -image.height / 2);

ctx.restore();
```

So let's apply this to drawing our rockets:

```js
// rockets.js

function drawRockets(camera) {
    for(let i = 0; i < rockets.length; ++i) {
        let rocket = rockets[i];

        ctx.save();

        // Note how we subtract the camera position as part of this translate call.
        ctx.translate(rocket.x - camera.x, rocket.y - camera.y);

        ctx.rotate(rocket.angle);

        ctx.drawImage(ROCKET_IMAGE, -ROCKET_IMAGE.width / 2, -ROCKET_IMAGE.height / 2);

        ctx.restore();
    }
}
```

Hop back into the game and try shooting rockets now. They should be facing the direction they were fired in. Lit!

## 3. Enemy AI
Having the player fire rockets whenever they jump is nice for debugging them, but now that we know they're working, let's have the enemies fire them.

Recall that the enemies only start firing rockets once they're within a certain distance from the player (i.e. they've stopped chasing the player). So let's write some code to create rockets when we know the player is close enough. Since we've already created an if statement that checks if the enemy is too far away and accelerates them towards the player, we can just add an else clause for the opposite case.

```js
// enemies.js

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        // Other code

        // Move the 'angle' const out of the body of the
        // if since we're gonna need it for the else as well
        const angle = Math.atan2(distY, distX);

        if((distX * distX + distY * distY) < ENEMY_CHASE_RADIUS * ENEMY_CHASE_RADIUS) { 
            enemy.dx += Math.cos(angle) * ENEMY_MOVE_ACCEL;
            enemy.dy += Math.sin(angle) * ENEMY_MOVE_ACCEL;
        } else {
            // The player is close enough for us to shoot them, so
            // shoot em.
            createRocket(enemy.sprite.x, enemy.sprite.y, angle);
        }
    }
}
```

Let's run the game. Right off the bat, we notice two major issues:
* Enemy spams rockets as soon as it gets close enough
* The rockets spawn at the top-left corner of the enemy sprite

I'm gonna go over how to fix the first issue. The second is an exercise for you :)

So we need to limit the rate at which enemies fire rockets. Well, you could imagine that we would need some kind of timer to determine this. Let's add a `cooldownTimer` property to the enemy.

```js
// enemies.js

function createEnemy() {
    let enemy = {
        // Other properties
        cooldownTimer: 0
    };
}
```

The idea is that we should only be able to fire rockets if this timer has a value less than or equal to zero. Whenever this timer has a greater value, we'll subtract from it every frame the amount of time that elapses per frame (remember, the `sprites.js` module defines `SEC_PER_FRAME` which is `1/60` by default).

So every time we fire, we add a cooldown duration to this timer, preventing the enemy from firing until that duration elapses.

```js
// enemies.js

const ENEMY_SHOOT_COOLDOWN = 2.0;

function updateEnemies() {
    for(let i = 0; i < enemies.length; ++i) {
        // Other code

    
        // Subtract from our timer if it's greater than 0        
        if(enemy.cooldownTimer > 0) {
            enemy.cooldownTimer -= SEC_PER_FRAME;
        }


        const angle = Math.atan2(distY, distX);

        if((distX * distX + distY * distY) < ENEMY_CHASE_RADIUS * ENEMY_CHASE_RADIUS) { 
            enemy.dx += Math.cos(angle) * ENEMY_MOVE_ACCEL;
            enemy.dy += Math.sin(angle) * ENEMY_MOVE_ACCEL;
        } else {
            if(enemy.cooldownTimer <= 0) {
                enemy.cooldownTimer += ENEMY_SHOOT_COOLDOWN;
                createRocket(enemy.sprite.x, enemy.sprite.y, angle);
            }
        }
    }  
}
```

If you run the game now, you should notice that the enemies are a lot more tame. 

Now, think about the following for a second. 
Let's say the enemy just spawned close enough to the player
that they can fire at the player. This is super frustrating, so give some thought to how you can fix this.

Hint: the easy (and I'd argue perfect) fix should only require changing one property.

That's all for this lesson. Thanks for reading!

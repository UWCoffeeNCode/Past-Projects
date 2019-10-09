# Meet-Up #2 Agenda:

**Objective**: Simplify asset loading, get an animated sprite on the screen and learn how to use tiled + display/collide with a tilemap

Turn to the person on your left and talk about the best thing that happened to you over the weekend.

Please sign up for the general slack at https://uwcoffeencode.slack.com if you haven't already. Make sure you
join the game-dev-2-colorbound channel.

## 1. Tools
* Tiled map editor (https://www.mapeditor.org)

## 2. Simplifying Asset Loading
Right now, working with images is a pain. We do the following every time we want to load an image:

```js
let someImage = null;

let image = new Image();

image.addEventListener("load", function() {
    someImage = image;
});

image.src = "assets/heart.png";
```

Later, we check if the `someImage` variable before using it so our browser doesn't complain.

We could alternatively do this:

```js
let someImage = new Image();
someImage.src = "heart.png";

// Somewhere else
if(!someImage.complete) {
    return;
}
```

But this is still annoying because we have to do this check before using images anywhere.
Often, we'd like our assets (images or any similar resource) to be loaded by the time we run the code that uses them.

How can we make sure this is the case?
Well, what if we simply do nothing in our game loop unless all images are loaded?

This will solve the problem of having to perform the checks in our code since none of our code
would be executed unless all resources are loaded.

We can keep track of how many resources have yet to be loaded and skip our game loop code if there's still some waiting.

```js
// preload.js
let loadingImagesCount = 0;

function loadImage(filename) {
    let image = new Image();

    image.addEventListener("load", function() {
        loadingImagesCount -= 1;
    });    

    image.src = filename;
    loadingImagesCount += 1;

    return image;
}

function areAllAssetsLoaded() {
    return loadingImagesCount == 0;
}

// In loop.js
function loop() {
    if(areAllAssetsLoaded()) {
        processInput();
        update();
        draw();
    }

    requestAnimationFrame(loop);
}
```

Now, our code which loads images can be replaced with the following:

```js
let image = loadImage("heart.png");
```

And we can simply draw this image in our `draw` function because we can rest assured that
the draw function will never be called when images are still being loaded.

## 3. Animation
There are many approaches to doing 2d animation in games. The approach we are going to use is referred to as spritesheet animation.
All animated entities in our game will use an image in which all the frames of its animations are 
laid out sequentially. In order to give the illusion of smooth animation, we cycle the region of the image we display
pereodically.

Here's an article which describes an implementation of this in great detail: https://gamedevelopment.tutsplus.com/tutorials/an-introduction-to-spritesheet-animation--gamedev-13099

Look at the root directory of the project. There is a folder called `utils` which contains a file called `sprites.js`.
This is a module I wrote that facilitates sprite animation, and it's what we're going to use for this lesson. I will expand on how this
is implemented later.

Here's an example to demonstrate the basic usage of this module.

```js
// We need to supply some sprite information to createSprite; since this information
// could be shared across multiple sprites (i.e. all enemies have the exact same animations)
// we can store this object in a variable separate from the sprite.
let spriteInfo = {
    image: loadImage("redenemy.png"),   // Thanks to our simplification of image loading above, this is perfectly fine
    
    // Each "frame" of the animation is 128x128 pixels large
    frameWidth: 128,
    frameHeight: 128,

    // Anims is an object whose properties are the names of the animations
    // available on this sprite
    anims: {
        idle: {
            // 0 refers to the top-left-most frame in the image
            // it increases going right. So if the image had 5 columns
            // and 3 rows of frames, there would be a total of 15 frames,
            // the first row being 0,1,2,3,4.
            startFrame: 0,

            // Number of frames in the animation
            length: 5,

            // How long each frame of the animation is displayed for (in seconds).
            // The larger this value, the slower the rate of animation
            frameTime: 0.1
        },
        
        // Other animations go here...
    },

    // This is optional; if supplied, it is called every time an animation ends and wraps around (i.e. loops).
    // So, for example, if you wanted to trigger something to happen when an animation ended, you could do that
    // in here
    onLoop: function(sprite) {
    }
};

// createSprite creates an object with an x, y position and information about the current animation
// that it is playing. When first created, no animation is playing, so it simply displays frame 0.
let sprite = createSprite(spriteInfo);

// In order to start playing an animation on a sprite, we
// call playAnim, supplying the sprite and the animation's name.
playAnim(sprite, "idle");

// This will mean that the sprite is drawn horizontally flipped (so you don't need to store separate animations
// for left and right; just use this)
sprite.flip = true;

// When appropraite, we can call this to remove the sprite
removeSprite(sprite);

function update() {
    // This is responsible for updating the current frame the sprites are displaying
    // based on their currently playing animation
    updateSprites();
}

function draw() {
    // The 'camera' is a global offset that is applied to all sprites; every sprite is
    // drawn at it's position - camera's position. This basically emulates a camera
    // one could move around.
    let camera = {
        x: 100,
        y: 100
    };

    drawSprites(camera);    
}
```

## 4. Tilemaps
Much like sprites, there are many approaches to representing levels within a game.
One approach which is very flexible and lends itself to creating a large variety of levels
relatively quickly is tilemaps.

A tilemap consists of a grid of regularly-shaped images referred to as "tiles". This allows us to create
very large and dynamic levels without having to create equally large images to represent them.

Instead of storing a separate image for each tile in a tilemap, we can store them all in a single image
and simply draw the appropriate region of the image; this is exactly how sprites work as well. 

So how do we represent this tilemap? Well, it depends. I like to use a tilemap editor called Tiled, and it conveniently
outputs a JavaScript file in which every tile is represented by an integer in an array. It also allows you to create
layers (which is just an array of objects which contain these integer arrays among other information).

Here's a good introduction to how you can use tiled: https://gamedevelopment.tutsplus.com/tutorials/introduction-to-tiled-map-editor-a-platform-agnostic-tool-for-level-maps--gamedev-2838

Again, I've written a module which lets us work with tiled maps. It's located in the `utils` folder; it's called `tilemap.js`. Copy that into your code folder and add it to your index.html.

Here's how that module can be used:

```js
// Inside preload.js

function areAllAssetsLoaded() {
    // The module defines a global variable called tileMap which contains the tile map data as given to us by tiled
    // We will wait for it to be loaded before running our code.
    return loadingImagesCount == 0 && tileMap;
}

// Inside loop.js 

function draw() {
    // Make sure camera is defined and has an x, y property
    drawTilemap(camera);
}
```

## 5. Collision
There is a handy function in `tilemap.js` which checks whether a given rectangle is intersecting with any tiles on a layer named "Main" in the tiled map.

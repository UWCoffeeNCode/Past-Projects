# Meet-Up #1 Agenda:

**Objective**: Learn about game loops, how to handle input, and learn how to draw graphics using HTML5 canvas.

Please sign up for the general slack at https://uwcoffeencode.slack.com if you haven't already. Make sure you
join the game-dev-2-colorbound channel.

## 1. Tools
* If you haven't already, I would recommend you install a text editor
* Google chrome

## 2. Colorbound
* A 2d singleplayer shooter platformer game written in a custom engine.
* Why not use a pre-existing game engine?
    - We are developing the game alongside the engine, adding features as required
    - The browser already provides the majority of the functionality we will be using; most browser game
      engines offer far more complex APIs than what we'll need
    - We are not making Unity :)
    - It allows us to gain a deeper understanding of how to implement good systems

## 3. Basics

### The Game Loop
Games, unlike most other types of software, must continue working even if the user doesn't provide any new input.
Furthermore, they must present their work frequently and steadily in order to give the appearance
of smooth animation.

Generally speaking, one unit of work for the game consists of the following:
1. Processing user input
2. Performing game logic
3. Presenting the game

This describes the high-level anatomy of a single "frame" of a game; the game loop is responsible for running
this sequence frequently and steadily.

As mentioned earlier, games differ from other types of software in that they don't wait on user input in that
first step. As such, a niave loop such as the following:

```js
while(true) {
    handleInput();
    update();
    draw();
}
```

will cause the game to run as fast as possible. Other than starving your CPU of resources (and causing chrome to crash)
this will not ensure that the game runs steadily. Any logic that depends on that behaviour (ex. physics, as you'll see later)
will certainly break.

Luckily for us, most browsers supporting the HTML5 standard provide a function `requestAnimationFrame` which will schedule our code to be run
before the browser paints a frame. This tends to happen at 60 "Frames per second" (i.e. how many times the aforementioned
loop will run every second).

```js
function loop() {
    handleInput();
    update();
    draw();    

    // Tell the browser to call this function before the end of the next frame
    requestAnimationFrame(loop);
}

// Start our game loop
loop();
```

### Input Handling

Handling input in HTML5 is simple. Every time a user interacts with the document, the browser fires an "event". Events are notable
occurances within the browser that could be prompted by a user or some code. We can respond to this event as follows:

```js
window.addEventListener("eventName", function(event) {
    // Code to handle said event
});
```

So, if we wanted to know when the user pressed a key, we could do the following:

```js
window.addEventListener("keydown", function(e) {
    console.log("The user pressed a key:", e.key);
});
```

A similar `keyup` event is fired when the user releases a key.

While handling an event as such is very simple, this does not play nicely with our game loop.
The browser calls these functions whenever it feels appropriate, so we need to keep track of the 
input information elsewhere.

```js
let input = {
    left: false,
    right: false,
    jump: false
};

// A little helper so we don't have to repeat the code
// inside the keydown and keyup listeners
function setKeyState(key, down) {
    if(key == "a") {
        input.left = down;
    } else if(key == "d") {
        input.right = down;
    } else if(key == "w") {
        input.jump = down;
    }
}

window.addEventListener("keydown", function(e) {
    setKeyState(e.key, true);
});

window.addEventListener("keyup", function(e) {
    setKeyState(e.key, false);
});
```

Now we can access the input object's properties in order to query its state at any time.
Another advantage of storing the input state in this manner is that the code which uses
it doesn't care about how it's created. Should we decide to support gamepads in the future,
we simply set corresponding properties in the input object and the game code would remain
the same.

### Game Logic
For this first lesson, the logic of the game will be pretty simple:

```js
let player = {
    // Position
    x: 0,
    y: 0,

    // Velocity
    dx: 0,
    dy: 0
};

// Our input code from above
let input = {
    left: false,
    right: false,
    jump: false
};

// A little helper so we don't have to repeat the code
// inside the keydown and keyup listeners
function setKeyState(key, down) {
    if(key == "a") {
        input.left = down;
    } else if(key == "d") {
        input.right = down;
    } else if(key == "w") {
        input.jump = down;
    }
}

window.addEventListener("keydown", function(e) {
    setKeyState(e.key, true);
});

window.addEventListener("keyup", function(e) {
    setKeyState(e.key, false);
});

function processInput() {
    if(input.left) {
        player.dx = -5;
    } else if(input.right) {
        player.dx = 5;
    } else {
        player.dx = 0;
    }
}

function update() {
    player.x += player.dx;
    player.y += player.dy;
}

function draw() {
    // TODO
}

function loop() {
    processInput();
    update();
    draw();    
}
```


### Drawing Images using Canvas

We are responding to input and updating a player object, but we don't really have anything to show for it.
That's where the "canvas" comes in. HTML5 provides the aforementioned element which allows you to draw
arbitrary shapes, images, and text onto it.

First, we must add an HTML canvas element into our document as follows (create a file called index.html):

```html
<canvas id="view" width="800" height="600"></canvas>
<script src="loop.js"></script>
```

We can then access this in our javascript code (We'll create a script called loop.js and write the code above)

```js
// At the top of the file

// We can access the canvas by the id we set ("view")
let canvas = document.getElementById("view");

// The actual HTML element object doesn't provide a means to draw onto it.
// We must ask it to give us a graphics "context", and in our case, a 2d context
// so we can draw.
let ctx = canvas.getContext("2d");

// ...

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Let's draw a filled rectangle (32x32) that's red
    ctx.fillStyle = "red";

    ctx.fillRect(player.x, player.y, 32, 32);
}
```

If you now open index.html, you should see a red rectangle at pixel coordinates (100, 100) on the canvas.
Notice that as we increase the y value parameter, the rectangle moves further down the screen. This is because the
canvas origin is in the top left corner and the y parameter increases as you go down.

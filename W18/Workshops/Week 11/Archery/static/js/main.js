// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// - { { {    GRAPHICS    } } } -
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


const SCALING_FACTOR = 1;
const HORIZONTAL = 0;
const VERTICAL = 1;
const WIDTH = window.innerWidth;
const HEIGHT = window.innerHeight;

var RES_URL;


/** Sets URL from which resources are accessed. */
function setResUrl(root) {
    RES_URL = root;
}


/** Loads global resources. Called after setRoot. */
function loadResources() {
    // Load images
    imgBow = new SpriteSheet("img/bow.png", 420, 360, 6, 4, 1.5);
    imgArrow = new Img("img/horizontal_arrow.png", 128, 40);
    imgTarget = new Img("img/crosshair_red_small.png", 42);
    imgBoard = new Img("img/target_colored_outline.png", 142);

    skyTop = new Img("img/skybox_top.png", HEIGHT / 2);
    skyBackground = new Img("img/skybox_sideHills.png", HEIGHT / 2);

    grass = new Img("img/stone_grass.png", GRASS_SIZE);
    stone = new Img("img/stone.png", GRASS_SIZE);
    gold = new Img("img/stone_gold.png", GRASS_SIZE);

    grassBlades = [];
    for (var i = 1; i <= 4; i++) {
        grassBlade = new Img("img/grass" + i + ".png", GRASS_SIZE);
        grassBlades.push(grassBlade);
    }

    grassBladePositions = {};
    for (var i = 0; i < 10; i++) {
        pos = Math.floor(Math.random() * WIDTH / GRASS_SIZE)
        grassBlade = grassBlades[Math.floor(Math.random() * grassBlades.length)];
        grassBladePositions[pos] = grassBlade;
    }

    // Set variables based on image dimensions
    boardHeight = imgBoard.height;
    boardWidth = 10;
    boardBuffer = 200;
    board = new Projectile(boardWidth, boardHeight, false, true, false);

    board.vx = 0;
    board.vy = 1;
    board.x = WIDTH - boardWidth - boardBuffer;
    board.y = 0;
}


/**
 * Sprite Sheet.
 * @param {int} n - Number of sprites in x direction.
 * @param {int} m - Number of sprites in y direction.
 */
function SpriteSheet(src, x, y, n, m) {
    this.img = new Img(src, 420, 360);
    this.sx = n;
    this.sy = m
    this.width = this.img.width / n;
    this.height = this.img.height / m;

    this.drawSprite = function(sprite, x, y, rot) {
        rot = (typeof rot == "undefined") ? 0 : rot;

        if (rot == 0) {
            canvasContext.drawImage(this.img.img,
                sprite % this.sx * this.width,
                Math.floor(sprite / 5) * this.height,
                this.width, this.height,
                x, y,
                this.width, this.height);
        }
        else {
            canvasContext.save();
            canvasContext.translate(
                x + this.width / 2,
                y + this.height / 2);
            canvasContext.rotate(rot);
            canvasContext.drawImage(this.img.img,
                sprite % this.sx * this.width,
                Math.floor(sprite / 5) * this.height,
                this.width, this.height,
                -this.width / 2, -this.height / 2,
                this.width, this.height);
            canvasContext.restore();
        }
    }
}


/** Image element of given dimensions. */
function Img(src, x, y) {
    // by default, set image height to width
    y = (typeof y == "undefined") ? x : y;

    this.img = new Image(x * SCALING_FACTOR, y * SCALING_FACTOR);
    this.img.src = RES_URL + src;
    this.width = this.img.width;
    this.height = this.img.height;

    this.draw = function(x, y, rot) {
        rot = (typeof rot == "undefined") ? 0 : rot;

        if (rot == 0) {
            canvasContext.drawImage(this.img,
                x, y,
                this.img.width,
                this.img.height);
        }
        else {
            canvasContext.save();
            canvasContext.translate(
                x + this.width / 2,
                y + this.height / 2);
            canvasContext.rotate(rot);
            canvasContext.drawImage(this.img,
                -this.width / 2,
                -this.height / 2,
                this.img.width,
                this.img.height);
            canvasContext.restore();
        }
    }

    this.tesselate = function(direction, offset) {
        // compute number of times image is drawn
        if (direction == HORIZONTAL) {
            tesselations = Math.ceil(canvas.width / this.img.width);
        }
        else {
            tesselations = Math.ceil(canvas.height / this.img.height);
        }

        // draw tesselation
        for (var i = 0; i < tesselations; i++) {
            x = (direction == HORIZONTAL) ? i * this.img.width : offset;
            y = (direction != HORIZONTAL) ? i * this.img.height : offset;
            this.draw(x, y);
        }
    }
}


// canvas
var canvas;
var canvasContext;

// icons
var imgBow;
var imgArrow;
var imgTarget;
var imgBoard;

// background
var skyTop;
var skyBackground;

// ground
const GRASS_SIZE = 64;
var grass;
var stone;
var gold;
var grassBlades = [];
var grassBladePositions = {};



// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// - { { {    GAME PLAY    } } } -
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


// game states
const PLACING_BOW = 0;
const PLACING_TARGET = 1;
const WATCHING_ARROW = 2;
var gameState = PLACING_BOW;

// game settings
const FPS = 60;
const GRAVITY = 1;
const MAX_RENDERED_ARROWS = 3;
const MAX_FIRED_ARROWS = 3;

var groundHeight;

var arrowWidth = 40;
var arrowHeight = 5;
var arrows = [];
var arrowsFired = 0; // Updated in fire()

var boardHeight;
var boardWidth;
var boardBuffer;
var board;

var bowLocation = [0, 0];
var targetLocation = [0,0];

var score = 0; // Updated in updateArrow()


window.onload = function() {
    canvas = document.getElementById('gameCanvas');
    canvas.width = WIDTH;
    canvas.height = HEIGHT;
    canvasContext = canvas.getContext('2d');

    render();

    // updates
    setInterval(function() {
        update();
        render();
    }, 100 / FPS);

    // listeners
    canvas.addEventListener('mousemove', handleMouseMove);
    canvas.addEventListener('click', handleMouseClick);
}


/** Handles any mouse movement. Updates bow and target accordingly. */
function handleMouseMove(evt) {
    var mousePos = getMousePos(evt);
    if (gameState == PLACING_BOW) {
        bowLocation[0] = mousePos.x;
        bowLocation[1] = mousePos.y;
    }
    // placing target with mouse before or after shot
    else {
        targetLocation[0] = mousePos.x;
        targetLocation[1] = mousePos.y;
    }
}


/** Handles any mouse clicks. Updates game state accordingly. */
function handleMouseClick(evt) {
    var mousePos = getMousePos(evt);
    if (gameState == PLACING_BOW) {
        targetLocation[0] = mousePos.x;
        targetLocation[1] = mousePos.y;
        gameState = PLACING_TARGET;
    }
    else if (gameState == PLACING_TARGET) {
        fire();
        gameState = WATCHING_ARROW;
    }
    else if (gameState == WATCHING_ARROW) {
        gameState = PLACING_BOW;
    }
}


/** Launches arrow. */
function fire(){
    arrow = new Projectile(arrowWidth, arrowHeight, true, false, true);
    arrow.x = bowLocation[0] + imgBow.width / 2;
    arrow.y = bowLocation[1] + imgBow.height / 2;
    arrow.vx = (targetLocation[0] - bowLocation[0]) / (FPS);
    arrow.vy = (targetLocation[1] - bowLocation[1]) / (FPS);
    arrows.push(arrow);

    if (arrows.length > MAX_RENDERED_ARROWS) arrows.shift();
    arrowsFired++;

    if (arrowsFired > MAX_FIRED_ARROWS) endGame();
}


/** Handles all trajectory updating. */
function update() {
    // board movement.
    board.update();

    // arrow movement.
    updateArrow();
}


/** Updates arrow movement. */
function updateArrow() {
    for (var i = 0; i < arrows.length; i++) {
        arrow = arrows[i];
        // Score updater
        if(arrow.doesCollide(board) && arrow.stuck != true){
          score++;
        }
        if (arrow.doesCollide(board)) {
            arrow.stuck = true;
            arrow.host = board;
        }

        arrow.update()
    }
}


/**
 * Projectile.
 * @param {bool} gravity - Whether object is affected by gravity or not.
 * @param {bool} bounce - Whether object will bounce upon striking a surface.
 * @param {bool} rotate - Whether object will rotate depending on trajectory.
 */
function Projectile(width, height, gravity, bounce, rotate) {
    this.width = width;
    this.height = height;
    this.gravity = gravity;
    this.bounce = bounce;
    this.rotate = rotate;
    this.x = 0;
    this.y = 0;
    this.vx = 0;
    this.vy = 0;
    this.rotation = 0;
    this.stuck = false;
    this.host = null;
    this.dead = false;

    this.update = function() {
        if (this.stuck) {
            // if object is stuck in another object, move both objects
            if (this.host) {
                this.x += this.host.vx;
                this.y += this.host.vy;
            }
            return;
        }

        if (this.rotate) {
            // update rotation based on trajectory
            this.rotation = Math.atan(this.vy / this.vx);
            this.rotation += (this.vx > 0 ? 0 : -Math.atan(1)*4 );
        }

        // update trajectory
        if (this.gravity) {
            this.vy += GRAVITY / FPS;
        }

        this.x += this.vx;
        this.y += this.vy;

        if (this.y <= 0 && this.bounce) {
            this.vy = -this.vy;
        }

        // check for ground collision
        if (this.y + this.height >= groundHeight) {
            if (this.bounce) {
                this.vy = -this.vy;
            }
            else {
                this.vx = 0;
                this.vy = 0;
                this.stuck = true;
            }
        }
    }

    this.doesCollide = function(target) {
        return (
            this.x + this.width / 2 >= target.x &&
            this.x + this.width / 2 <= target.x + target.width &&
            this.y + this.height / 2 >= target.y &&
            this.y + this.height / 2 <= target.y + target.height
        )
    }
}  // Projectile


function getMousePos(evt){
    // accounts for scrolling and moving the mouse outside the canvas
    var rect = canvas.getBoundingClientRect();
    var root = document.documentElement;
    var mouseX = evt.clientX - rect.left - root.scrollLeft;
    var mouseY = evt.clientY - rect.top - root.scrollTop;

    // return JSON - like returning a dictionary in python
    return {
        x:mouseX,
        y:mouseY
    };
}


/** Ends game, giving user chance to restart. */
function endGame() {
    // Overlay
    // Show score
    // Show table 
    // Give user chance to restart
    // TODO: add high score to renderGUI

    uploadScore(score);
    score = 0;
}



// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// - { { {    RENDERING    } } } -
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


/** Handles all game rendering. */
function render() {
    // background
    drawBackground();

    // GUI
    drawGUI();

    // board
    imgBoard.draw(board.x, board.y);

    // bow
    drawBow();

    // arrow
    drawArrows();

    // target
    if (gameState == PLACING_TARGET){
        imgTarget.draw(targetLocation[0], targetLocation[1]);
        drawPath();
    }
}


/** Draws path from bow to target. */
function drawPath() {
    canvasContext.setLineDash([5, 3])
    canvasContext.lineWidth = 2;
    canvasContext.strokeStyle = 'orange';
    canvasContext.beginPath();
    canvasContext.moveTo(
        bowLocation[0] + imgBow.width / 2,
        bowLocation[1] + imgBow.height / 2);
    canvasContext.lineTo(
       targetLocation[0] + imgTarget.width / 2,
       targetLocation[1] + imgTarget.height / 2);
    canvasContext.stroke();
}


/** Renders all arrows. */
function drawArrows() {
    for (var i = 0; i < arrows.length; i++) {
        arrow = arrows[i];
        imgArrow.draw(
            arrow.x,
            arrow.y - imgArrow.height / 2,
            arrow.rotation);
    }
}


/** Renders bow, rotating and choosing the correct sprite to match its power. */
function drawBow() {
    // choose sprite depending on drawback of bow
    var dx = targetLocation[0] - bowLocation[0];
    var dy = targetLocation[1] - bowLocation[1];
    var powerLevel = Math.floor(Math.sqrt(dx*dx + dy*dy) / 300.0 * 9);
    var level = (gameState == WATCHING_ARROW) ? 10 : Math.min(powerLevel, 9);
    var rad = 0;

    if (gameState == PLACING_TARGET) {
        // rotate bow to point to target
        rad = Math.atan(dy / dx);
        if (dx < 0) rad += Math.PI;
    }

    imgBow.drawSprite(level, bowLocation[0], bowLocation[1], rad);
}


/** Draws background, including sky, trees, and grass. */
function drawBackground() {
    // sky
    skyTop.tesselate(HORIZONTAL, 0);
    skyBackground.tesselate(HORIZONTAL, skyTop.height);

    // grass blades
    groundHeight = HEIGHT - grass.height * 2;
    for (var pos in grassBladePositions) {
        grassBlade = grassBladePositions[pos];
        grassBlade.draw(pos * grassBlade.width,
            groundHeight - grassBlade.height);
    }

    // ground
    grass.tesselate(HORIZONTAL, groundHeight);
    stone.tesselate(HORIZONTAL, groundHeight + grass.height);
    // drawTesselation(stone, HORIZONTAL, lowestHeight);
}


/** Draws GUI, including arrows fired, and total score. */
function drawGUI(){
    highScore = "10"
    leftPadding = 10
    topPadding = 20
    spacing = 20

    canvasContext.font = "20px Open Sans";
    canvasContext.fillText(
        "Arrows Fired: " + arrowsFired, leftPadding, topPadding);
    canvasContext.fillText(
        "Score: " + score, leftPadding, topPadding + spacing);
    canvasContext.fillText(
        "High Score: " + highScore, leftPadding, topPadding + spacing * 2);
}



// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// - { { {    WEB SERVER    } } } -
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


/** Uploads score to server. */
function uploadScore(score) {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/score", true);
    xhttp.send(score)
}
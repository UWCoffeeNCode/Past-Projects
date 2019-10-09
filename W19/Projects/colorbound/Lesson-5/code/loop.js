let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

function init() {
    for(let i = 0; i < 2; ++i) {
        createEnemy(100 + i * 5, 100);
    }
}

function processInput() {
    playerProcessInput();
}

function update() {
    updatePlayer();
    updateEnemies();
    updateRockets();
    updateLasers();
    updateSprites();
}

const PLAYER_CENTER_OFF_X = 64;
const PLAYER_CENTER_OFF_Y = 64;


function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
 
    let camera = {
        x: Math.floor(player.sprite.x + PLAYER_CENTER_OFF_X - canvas.width / 2),
        y: Math.floor(player.sprite.y + PLAYER_CENTER_OFF_Y - canvas.height / 2)
    };

    drawTilemap(camera);
    drawLasers(camera);
    drawSprites(camera);
    drawRockets(camera);


    // TODO(Apaar): Get rid of this before shipping
    debugDraw(camera);


    drawPlayerHp();
}

function loop() {
    if(areAllAssetsLoaded()) {
        processInput();
        update();
        draw();
    }

    requestAnimationFrame(loop);
}

init();
loop();

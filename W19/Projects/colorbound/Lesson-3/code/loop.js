let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

function init() {
    for(let i = 0; i < 20; ++i) {
        createEnemy(100 + i * 5, 100);
    }
}

function processInput() {
    playerProcessInput();
}

function update() {
    updatePlayer();
    updateEnemies();
    updateSprites();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
 
    let camera = {
        x: 0,
        y: 100
    };

    drawTilemap(camera);
    drawSprites(camera);
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

let camera = {
    x: 0,
    y: 0,
    shake: {
        timer: 0,
        magnitude: 0
    }
};

function shakeCamera(duration, magnitude) {
    camera.shake.timer = duration;
    camera.shake.magnitude = magnitude;
}

function initGame() {
    initEnemies();
    initWaves();

    createEnemy(60, 60, "red");
    createEnemy(200, 60, "red");
}

function updateGame() {
    if(camera.shake.timer > 0) {
        camera.shake.timer -= SEC_PER_FRAME;
    }

    updatePlayer();
    updateEnemies();
    updateWaves();
    updateSprites();
}

function drawGame() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const cam = {
        x: camera.x,
        y: camera.y
    };

    if(camera.shake.timer > 0) {
        cam.x += 2 * (Math.random() - 0.5) * camera.shake.magnitude;
        cam.y += 2 * (Math.random() - 0.5) * camera.shake.magnitude;
    }

    cam.x = Math.floor(cam.x);
    cam.y = Math.floor(cam.y);

    drawTilemap(cam);
    debugDrawEnemies(cam);
    drawWaves(cam);
    drawSprites(cam);
    debugDrawPlayer(cam);
}

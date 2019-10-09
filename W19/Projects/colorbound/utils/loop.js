// Main loop
const MS_PER_FRAME = 1000 / 60;
const SEC_PER_FRAME = MS_PER_FRAME / 1000;

let then = Date.now();
let elapsedMs = 0;

let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

ctx.imageSmoothingEnabled = false;

function loop() {
    let now = Date.now();
    let deltaTime = now - then;

    elapsedMs += deltaTime;

    while(elapsedMs >= MS_PER_FRAME) {
        updateGame();
        elapsedMs -= MS_PER_FRAME;
    }

    then = now;

    drawGame();
    window.requestAnimationFrame(loop);
}

initGame();
loop();

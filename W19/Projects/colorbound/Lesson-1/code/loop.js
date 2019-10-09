let input = {
    left: false,
    right: false,
    jump: false
};

let player = {
    x: 0,
    y: 0
};

let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

let heartImage = null;

let img = new Image();   // Create new img element
img.addEventListener("load", function() {
    heartImage = img;
}, false);
img.src = "heart.png"; // Set source path

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

function processInput() {
    if(input.left) {
        player.x -= 4;
    } else if(input.right) {
        player.x += 4;
    } else {
    }
}

function update() {
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    /*
    ctx.fillStyle = "rgb(255, 0, 255)";
    ctx.fillRect(player.x, player.y, 32, 32);
    */

    if(!heartImage) {
        return;
    }

    ctx.drawImage(heartImage, player.x, player.y);    
}

function loop() {
    processInput();
    update();
    draw();

    requestAnimationFrame(loop);
}

loop();
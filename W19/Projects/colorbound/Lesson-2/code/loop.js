let input = {
    left: false,
    right: false,
    jump: false
};

let canvas = document.getElementById("view");
let ctx = canvas.getContext("2d");

let playerImage = loadImage("assets/player.png");

let player = {
    sprite: createSprite({
        image: playerImage,

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
    dy: 0
};

player.sprite.x = 100;
player.sprite.y = 200;

playAnim(player.sprite, "run");

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
    player.grounded = collideTileMap(player.sprite.x, player.sprite.y + 1, 128, 128);

    if(input.left) {
        player.dx = -4;
        player.sprite.flip = true;
    } else if(input.right) {
        player.dx = 4;
        player.sprite.flip = false;
    } else {
        player.dx = 0;
    } 

    if(input.jump && player.grounded) {
        player.dy = -10;
    }
}

function update() {
    player.dy += 0.5;

    if(player.dy > 20) {
        player.dy = 5;
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

loop();

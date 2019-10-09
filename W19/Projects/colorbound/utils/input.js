const LEFT_KEY = "a";
const RIGHT_KEY = "d";
const JUMP_KEY = "w";
const SHOOT_RED_KEY = "j";
const SHOOT_BLUE_KEY = "k";
const SHOOT_YELLOW_KEY = "l";

let input = {
    left: false,
    right: false,
    jump: false,
    shootRed: false,
    shootBlue: false,
    shootYellow: false,
};

function setKeyState(key, down) {
    if(key == LEFT_KEY) {
        input.left = down;
    } else if(key == RIGHT_KEY) {
        input.right = down;
    } else if(key == JUMP_KEY) {
        input.jump = down;
    } else if(key == SHOOT_RED_KEY) {
        input.shootRed = down;
    } else if(key == SHOOT_BLUE_KEY) {
        input.shootBlue = down;
    } else if(key == SHOOT_YELLOW_KEY) {
        input.shootYellow = down;
    }

}

window.addEventListener("keydown", function(e) {
    setKeyState(e.key, true);
});

window.addEventListener("keyup", function(e) {
    setKeyState(e.key, false);
});

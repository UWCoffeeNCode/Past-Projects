let input = {
    left: false,
    right: false,
    jump: false,

    shootRed: false,
    shootBlue: false,
    shootYellow: false
};

window.addEventListener("keydown", function(e) {
    if(e.key == "a") {
        input.left = true;
    } else if(e.key == "d") {
        input.right = true;
    } else if(e.key == "w") {
        input.jump = true;
    } else if(e.key == "j") {
        input.shootRed = true;
    } else if(e.key == "k") {
        input.shootBlue = true;
    } else if(e.key == "l") {
        input.shootYellow = true;
    }
});

window.addEventListener("keyup", function(e) {
    if(e.key == "a") {
        input.left = false;
    } else if(e.key == "d") {
        input.right = false;
    } else if(e.key == "w") {
        input.jump = false;
    } else if(e.key == "j") {
        input.shootRed = false;
    } else if(e.key == "k") {
        input.shootBlue = false;
    } else if(e.key == "l") {
        input.shootYellow = false;
    }
});

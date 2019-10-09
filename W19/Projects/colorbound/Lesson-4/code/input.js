let input = {
    left: false,
    right: false,
    jump: false
};

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

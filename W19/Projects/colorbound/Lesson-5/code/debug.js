
function debugDraw(camera) {
    for(let i = 0; i < rockets.length; ++i) {
        let rocket = rockets[i];

        ctx.fillStyle = "red";
        ctx.fillRect(rocket.x - camera.x + ROCKET_RECT.x, rocket.y - camera.y + ROCKET_RECT.y,
                     ROCKET_RECT.w, ROCKET_RECT.h);
    }
}

const SWEEP_SAMPLES = 5;

function moveCollideTileMap(e, sweep) { 
    if(collideTileMap(e.x + e.rect.x + e.dx, e.y + e.rect.y, e.rect.w, e.rect.h)) {
        if(sweep) {
            let mx = e.dx / SWEEP_SAMPLES;

            for(let i = 0; i < SWEEP_SAMPLES; ++i) { 
                if(collideTileMap(e.x + e.rect.x + mx, e.y + e.rect.y, e.rect.w, e.rect.h)) {
                    e.dx = 0;
                    break;
                } else {
                    e.x += mx;
                }
            }
        } else {
            e.dx = 0;
        }
    }

    if(collideTileMap(e.x + e.rect.x, e.y + e.rect.y + e.dy, e.rect.w, e.rect.h)) {
        if(sweep) {
            let my = e.dy / SWEEP_SAMPLES;

            for(let i = 0; i < SWEEP_SAMPLES; ++i) { 
                if(collideTileMap(e.x + e.rect.x, e.y + e.rect.y + my, e.rect.w, e.rect.h)) {
                    e.dy = 0;
                    break;
                } else {
                    e.y += my;
                }
            }
        } else {
            e.dy = 0;
        }
    }

    e.x += e.dx;
    e.y += e.dy;
}

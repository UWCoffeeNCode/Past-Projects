function loadImage(filename, callback) {
    let image = new Image();

    image.onload = function() {
        callback(image);
    };

    image.src = filename;
}

function clamp(v, min, max) {
    if(v < min) {
        return min;
    } else if(v > max) {
        return max;
    }

    return v;
}

function collideRects(ax, ay, aw, ah, bx, by, bw, bh) {
    if(aw < 0) {
        ax += aw;
        aw *= -1;
    }

    if(ah < 0) {
        ay += ah;
        ah *= -1;
    }

    if(bw < 0) {
        bx += bw;
        bw *= -1;
    }

    if(bh < 0) {
        by += bh;
        bh *= -1;
    }

    if(ax + aw < bx || bx + bw < ax) return false;
    if(ay + ah < by || by + bh < ay) return false;

    return true;
}

function collideCircles(ax, ay, arad, bx, by, brad) {
    const dx = (bx - ax);
    const dy = (by - ay);

    return dx * dx + dy * dy < (arad + brad) * (arad + brad);
}

function collideRectCircle(ax, ay, aw, ah, bx, by, radius) {
    const cx = ax + aw / 2;
    const cy = ay + ah / 2;

    const dx = (bx - cx);
    const dy = (by - cy);

    // Clamp dx and dy to half extents
    dx = clamp(dx, -aw / 2, aw / 2);
    dy = clamp(dy, -ah / 2, ah / 2);
    
    const px = cx + dx;
    const py = cy + dy;

    dx = (bx - px);
    dy = (by - py);

    return dx * dx + dy * dy < radius * radius;
}

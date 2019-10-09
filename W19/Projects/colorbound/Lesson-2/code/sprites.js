const SEC_PER_FRAME = 1 / 60;

let sprites = [];

// info looks like:
//  {
//      image: image,
//      frameWidth: frameWidth,
//      frameHeight: frameHeight,
//      anims: {
//          name: {
//              startFrame: startFrame,
//              length: length,
//              frameTime: frameTime
//          }
//      }
//      
//      (optional) onLoop: function(sprite)
//  }
function createSprite(info) {
    let sprite = {
        info: info,
        x: 0,
        y: 0,
        flip: false,
        frame: 0,
        animTimer: 0,
        curAnim: null
    };

    sprites.push(sprite);

    return sprite;
}

function removeSprite(sprite) {
    let i = sprites.indexOf(sprite);

    if(i < 0) {
        return;
    }

    sprites.splice(i, 1);
}

function playAnim(sprite, name, reset) {
    let anim = sprite.info.anims[name];

    if(anim == sprite.curAnim && reset) {
        sprite.animTimer = 0;
    }

    sprite.curAnim = anim;
}

function updateSprites() {
    for(let i = 0; i < sprites.length; ++i) {
        let sprite = sprites[i];

        if(!sprite.curAnim) {
            continue;
        }

        let curFrame = Math.floor(sprite.animTimer / sprite.curAnim.frameTime);

        if(curFrame >= sprite.curAnim.length) {
            curFrame -= sprite.curAnim.length;
            sprite.animTimer = 0;

            if(sprite.info.onLoop) {
                sprite.info.onLoop(sprite);
            }
        }

        sprite.frame = sprite.curAnim.startFrame + curFrame;

        sprite.animTimer += SEC_PER_FRAME;
    }
}

function drawSprites(camera) { 
    for(let i = 0; i < sprites.length; ++i) {
        let sprite = sprites[i];

        if(!sprite.info.image) {
            continue;
        }

        ctx.save();

        ctx.translate(sprite.x - camera.x, sprite.y - camera.y);

        if(sprite.flip) {
            ctx.translate(sprite.info.frameWidth, 0);
            ctx.scale(-1, 1);
        }

        const columns = Math.floor(sprite.info.image.width / sprite.info.frameWidth);

        ctx.drawImage(sprite.info.image, (sprite.frame % columns) * sprite.info.frameWidth,
                                         Math.floor(sprite.frame / columns) * sprite.info.frameHeight,
                                         sprite.info.frameWidth, sprite.info.frameHeight,
                                         0, 0, sprite.info.frameWidth, sprite.info.frameHeight);
    
        ctx.restore();
    }
}

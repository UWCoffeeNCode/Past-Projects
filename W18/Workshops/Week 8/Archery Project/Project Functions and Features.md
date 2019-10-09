 # Graphics
| Function Name | Description |
| --- | --- |
SpriteSheet | “sticker sheet” to save the sprites we’ll be using |
Img | image element of specified dimensions for a given sprite (a sprite is a moving computer graphic) | 

# Gameplay
 | Function Name | Description |
 | --- | --- |
handleMouseMove | handles mouse movement and updates bow and target accordingly |
handleMouseClick | handles mouse clicks and updates the game state accordingly |
**fire** | launches arrow |
update | handles all trajectory updating |
**updateArrow** | updates arrow movement | 
**Projectile** | defines the dimensions, gravity, and rotation of a given projectile (eg. arrow) |
getMousePos | accounts for scrolling and moving the mouse outside the canvas |

# Rendering
 | Function Name | Description |
 | --- | --- |
render | handles all game graphics rendering
**drawPath** | draws path from bow to target
drawArrows | renders all arrows
drawBow | renders the bow and picks the correct sprite to match its power |
drawBackground | draws background sky, trees, and grass |

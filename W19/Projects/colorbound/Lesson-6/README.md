# Meet-Up #6 Agenda

**Objective**: Be able to kill enemies with lasers, explosions, and level design.

## Level Loading and Design

### Tiled
I hope that at this point everybody has Tiled installed. If not, take some time to install it right now. This is the first topic I'm covering since this will enable you to modify the game a great deal.

Tiled let's us create and modify tilemaps (as discussed in more detail in Lesson 2); it also lets us place arbitrary "objects" around the level. These are essentially just shapes or images with properties attached (properties like `x`, `y`, `width`, `height`, etc). These can then be loaded up along with the tilemap and we can then use these properties to construct entities in our engine.

In the case of our game, we can create a new entity which spawns enemies every 20 seconds, for example, and place these spawners all around the level in Tiled. I will not delve into how the spawner works (since the requisite knowledge is covered in previous lessons), but I will discuss how you can load these objects.

### Adding Objects
Open up `assets/level.js` inside Tiled. You'll probably see a warning regarding a missing `player_icon.png` file. This is because when I first made this level, I created a player object which had this particular image assigned to it; that image is no longer present in the assets, so you can just dismiss the error by pressing "ignore".

### Cleaning Up
So you'll see that there's an object in the middle of the level with a big red X across it. On the right side of the screen, you should see a "layers" panel. Select the "Objects" layer. Then, press S to switch to the object selection tool (or use the toolbar on the top of the screen to find it). Select the red x object and press the delete key on your keyboard.

### Creating The Player
Okay, let's create an object. Press R or select the blue rectangle on the toolbar at the top of the screen. Click and drag at a reasonable place in the level. Great, you've just created an object. Let's give it a name and a type.

On the left side of the screen, you should see a panel labeled "properties". This panel shows the properties I was talking about earlier. Click in the box to the `name` and `type` properties and type `player`. Later, when we write code we can refer to these properties to determine what entity we are going to create/modify.

### Referring To Objects In Code
If you open up `tilemap.js` and look at line 42, you'll find some commented out code. The for loop that contains this code actually iterates over all objects in the Tiled level, and the `object` variable contains the current object we are inspecting. 

So, as mentioned earlier, every object has properties. Those properties can be read by accessing them on this `object` variable. So, for example, the name of the object will just be `object.name` inside this for loop.

Let's make use of that:

```js
// tilemap.js

function onTileMapLoaded(name, data) {
    // Other code...

    // Assume this is at line 42 inside the for loop
    if(object.type == "player") {
        player.sprite.x = object.x;
        player.sprite.y = object.y;
    }
}
```

Now, if we save our level in Tiled and run the game, the player's position should correspond to the position of the player object in the level file.

You can similiarly access other properties of the object as required.

### Custom Properties
Let's say you want to load other more specific properties from the level file that are not already present on the Tiled object. You can add custom properties to them. This way, a non-technical individual (on your team or otherwise) can modify the game more easily.

Let's add a `maxHp` custom property to the player object in Tiled. Select the player object (make sure you're on the `Objects` layer) and click the plus icon in the bottom left corner of the screen. 

A popup titled "Add Property - Tiled" should appear on your screen with a field to fill in the property name and a dropdown to select the type. Type in `maxHp` and select the `int` type.

Now you should be able to modify it from the custom properties panel just like any other property. You can access it in code as follows:

```js
// tilemap.js

function onTileMapLoaded(name, data) {
    // Other code

    // Assume this is at line 42 inside the for loop
    if(object.type == "player") {
        player.sprite.x = object.x;
        player.sprite.y = object.y;

        // All custom properties are stored inside the "object.properties" object.
        player.maxHp = object.properties.maxHp;
        
        // Make sure we update the player's current hp to match the max.
        player.hp = player.maxHp;
    }
}
```

And now if we run the game, the player's maxHp should be whatever it is in the Tiled level. Think about what other properties can be stored inside the custom properties. For example, you could store the fire rate of the lasers, the player's movement speed, etc. This is a very powerful concept since it allows you (and non-programmers on your team) to modify aspects of the game almost entirely from the level editor.

### Modifying the Tilemap
We can obviously also modify the actual tilemap layers themselves. Let's make the map a little bigger. Click the "Map" menu item at the top of the screen and click "Resize Map". Change the size to 40 tiles by 40 tiles.

That's better. Let's fill out the empty space. Select the "Main" layer in the Layers panel on the right. Recall that all tiles in this layer can be collided with, so we place walls down in this layer.

In order to place a tile, you need to select it from the "Tileset" (see Lesson 2 for more information on this). You should see a "Tilesets" panel in the bottom right of the screen. You can pick a tile (or multiple tiles) by clicking inside the image that's shown there.

Now, if you select the "Stamp Brush" tool in the toolbar or press B, you can place tiles down by clicking in the level. Hold shift and click to draw lines of tiles.

Place down walls to line the entirety of the new level. Use the "Eraser" tool to erase some of the old walls. Similarly, for the background layer, select a larger portion of the tileset and use the brush to paint making sure you have the "Background" layer selected.

There's more to it, but those are all the basics.

## Explosions
Explosions are actually very simple to do in our engine. Recall the structure of the `info` object passed in to `createSprite`:

```js
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
```

Note that there is an optional property `onLoop` which is a function that's called every time an animation loops. We can just play the explosion animation and then remove the sprite as soon as it loops. This is basically all that's needed to simulate an explosion. We don't even need to write any particular logic or timing code since the sprite codee handles it for us.

```js
// explosions.js

function createExplosion(x, y) {
    let explosion = createSprite({
        image: loadImage("assets/explosion.png"),
        frameWidth: 128,
        frameHeight: 128,
        anims: {
            explode: {
                // TODO(You): I made these numbers up, figure them out yourself
                startFrame: 0,
                length: 7,
                frameTime: 0.1
            }
        }

        onLoop: function(sprite) {
            removeSprite(sprite);
        }
    });
}
```

## Killing Enemies with Lasers
This is left as an exercise. It was covered in lesson 5 so see the documentation there.

# Colorbound
Build a complete 2D game and engine _from scratch_ using standard web technologies.

## Objective
* Gain an understanding of the fundamentals of game/engine programming
* Learn to write reusable code through refactoring
* Create a fun and extendable game!

## Tools and Technologies
* Google Chrome
* A text editor (Sublime Text, Vim, Notepad++, etc)
* Javascript, HTML5
* Tiled: https://www.mapeditor.org/

## Syllabus
| Lesson # | Week # | Date          | Description                                           |
| -------- | ------ | ------------- | ------------------------------------------------------|
| 1        | 5      | Jan 29 | Get an input-enabled sprite on the screen |
| 2        | 6      | Feb 5 | Display an animated sprite and a level + basic collision |
| -        | 7      | - | Snow Day |
| -        | 8      | Feb 19 | Reading Week Break: Special Meet-Up activity |
| 3        | 6      | Feb 26 | Add enemies |
| 4        | 10     | Mar 5 | Add rockets and have enemies fire them |
| 5        | 11     | Mar 12 | Add lasers |
| 6        | 12     | Mar 19 | Add powerups, explosions, and other polish |
| -        | 13     | Mar 26 | End of Term event! |

## Summary of material covered so far
We're heading into week 11 of the term. Here's what we've covered so far and how you can get up to speed:

You can download the latest code from `Lesson-4/code.zip`. Opening `index.html` in chrome should run the game in its latest state.

* Lesson 1:
    - The game loop: one unit of work for the game; has 3 steps:
        * Processing input
        * Performing game logic
        * Updating the display (Drawing graphics)
    - Input handling with HTML5:
        * Browser fires "events" (any significant occurance) whenever the user presses and releases a key
        * We register functions to be called when these events occur
        * We store the input state we are concerned with in an object so we don't have to worry about how it's produced (useful if we want to change the input device and handle touch events, for example)
    - Drawing graphics with HTML5 canvas:
        * We create a "canvas" element in our html code
        * We can create a "graphics context" from this canvas so we can draw graphics onto it
        * Images are loaded in the background so the browser fires an event once they're done loading; we respond to this and keep track of the loaded image
        * We can draw images using "context.drawImage" (google MDN documentation or see lesson docs for how you can use this)

* Lesson 2:
    - Animation:
        * Spritesheet: image which contains many frames of an animation placed next to each other
        * At any given time, we draw only a single frame of this image; we cycle the frame that's drawn to simulate animation
        * Sprite: an animated image; stores multiple animations and keeps track of which one is playing right now
        * Supplied `sprites.js` module which provides a few functions to create sprites, play animations, etc
    - Tilemaps:
        * Primary mechanism for storing and displaying levels in our game engine
        * Tilesheet: many regularly sized "tile" images packed into a single image
        * Tilemap: many of these tiles (portions of a tilesheet) layed out together across multiple layers etc to produce a level
        * We use "Tiled" the map editor to produce these tilemap levels
        * Provided `tilemap.js` module loads and provides functions for drawing/performing collision checks against these levels

* Lesson 3:
    - Refactoring:
        * Take all our code from `loop.js` and move it into separate files `player.js`, `input.js`, etc
    - Enemies:
        * Enemies are just sprites which fly towards the player, and then fire rockets once they're close enough
        * We create an array to keep track of all enemies, and functions to create and remove them
        * We did some trig/vectors to make enemies fly towards the player and then stop when they get close enough
        * Made enemies bounce off of each other when they get too close (also just math)
        * Talked about state machines and how we can model some AI using them

* Lesson 4:
    - Rockets:
        * Similar to enemies; just another entity
        * Learned how to draw rotated graphics with HTML5 canvas
    - Debug visulization:
        * At this point we were messing around with collision rectangles a lot so we wrote a function which drew these to the screen so we could see them better
        * Used graphics context 'fillRect' function

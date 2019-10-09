# Game Engine

A game engine can be defined as a framework for designing and creating video games [1] or as a collection of code that follows a game loop and can be modelled as a finite-state machine. In this lesson, we will be focusing on the latter definition.

## Game Loop 

![gameprogrammingpatterns.com, simple game loop diagram](https://github.com/UWCoffeeNCode/Lessons/blob/master/W18/Week%208/Game%20Engine/game-loop-simple.png)

A game loop is a specific pattern that your code follows in a loop to control the rate of gameplay [2]. The game loop consists of the following 3 parts:

### 1. Processing User Input
This is where the game accepts player commands.

Examples: Click, mouve mouse, keyboard press, etc.

### 2. Updating the Game State
This is where the game updates itself based on the player commands.

Examples: Increase speed, add health, remove enemy, calculating fall speed, etc.

### 3. Rendering the Game
This is where the game is drawn for the player to see ther result of their comamnds.

Examples: Animation of projectile, walking animation, drawing the background, etc.

## Finite-State Machine

### Turnstile Example:

![wikipedia, finite-state machine diagram](https://upload.wikimedia.org/wikipedia/commons/9/9e/Turnstile_state_machine_colored.svg)

A finite-state machine (FSM) is an abstract machine that can be in only 1 of a finite number of states at any moment [2]. The two states in the turnstile example are "locked" and "unlocked". The two inputs are "push" and "coin". An output is determined by the current state and the input given at that current state. If the state changes after an input, we call that new state the output. If the state remains the same after an input, we say that there is no outcome. For example, this occurs when you push at a locked turnstile or when you add a coin at an un-locked turnstile.

As programmers, we may use a finite-state machine to help us outline and understand the desired structure and functionalities of our project. 

### JavaScript Archery Example:

![coffee 'n code, JS archery FSM](https://github.com/UWCoffeeNCode/Lessons/blob/master/W18/Week%208/Game%20Engine/JS%20Archery%20FSM%20Diagram.jpg)

Within the context of our JavaScript Archery Project, we have 3 states:
- placing the bow
- placing the crosshair
- watching the projectile path

We also have 2 inputs:
- click mouse
- move mouse

In our project, clicking the mouse always results in an outcome while moving the mouse never has an outcome. 

## Sources: 

[1] Wikipedia (https://en.wikipedia.org/wiki/Game_engine)

[2] gameprogrammingpatterens.com (http://gameprogrammingpatterns.com/game-loop.html)

[3] Wikipedia (https://en.wikipedia.org/wiki/Finite-state_machine)

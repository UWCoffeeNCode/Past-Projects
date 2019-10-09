# Lesson 4

## 4.1 Creating and Storing our Friend

We got our board working so now its time to display the most important member of our game - the snake itself! Our snake will be constantly changing so how should we store it? The answer is through a state! Before we begin creating it, let's first ask ourselves a few questions about what we'll need to store:
- How do we know which direction to go?
- How do we know where the tail of the snake is so we can add to the body?
- How do we know where the body is so we can display it? What is a good way to store this?

Try thinking about how we could account for these cases, as well as how you would store them

...
...
...

- How do we know which direction to go?
    - We can have a direction variable which can take the values of: Up, Down, Left, or Right
- How do we know where the tail of the snake is so we can add to the body?
    - Just store the tail! :D 
- How do we know where the body is so we can display it? What is a good way to store this?
    - This seems to be a bunch of coordinates, so why don't we store it in an array?

```javascript
    this.state = {
        snake: {
          head: {
            x: 15,
            y: 15
          },
          tail: {
            x: 15,
            y: 15
          },
          direction: '',
          body: [{x:15,y:15}],
          running: false,
          alive: true,
          speed: 1
        }
    }
}
```

We will also create a new react component for our friend so that we can use it later on. Similar to earlier lessons, we will create  standard react component like this.

 ```javascript
 import React from 'react';
 
 class Snake extends React.Component{
 
     render(){
        return(
            <div id="Snake">
            
            </div>
        );
    }
}

export default Snake;
```

## 4.2 Displaying our friend

We have our friend saved, so now we just have to actually display it. This is similiar to what we did for the grid, but now we will loop through our array of the snake body and draw a green (or whatever colour you want) rectangle. We'll give you a little bit of time to work on this. Try to read ctx documentation if you are unsure of a function. We'll go over out answer together afterwards. Lets create a new function called drawSnake() to do this for us. Once we create it, we can just add it into our original drawBoard() function. 

```javascript
    drawSnake(){
      const {ctx, snake} = this.state
      ctx.fillStyle = 'green';
      snake.body.forEach(cord => {
        ctx.fillRect(cord.x * cellSize, cord.y * cellSize, 1 * cellSize, 1 * cellSize);
      })
    }
```

## 4.3 Moving our friend

If you notice, our friend currently does not move. This brings up a few questions: How can we move it? And how do we change the direction it's heading? When we think about other snake games, the first intuition we get is that we change the direction via the keyboard. The snake itself will move once every half second. 

To accomplish these tasks, we have two problems:
- How do we read keyboard input?
- How do we tell Javascript to perform an operation once every set time interval?

Lets turn to Google! 
Quick google search shows us this prebuild package for keyboard input: https://www.npmjs.com/package/react-keyboard-event-handler
We can also use this for a timer: https://www.w3schools.com/jsref/met_win_setinterval.asp

### 4.3.1 Detecting Keyboard Input

Here we use the React KeyboardEventHander to detect the arrow keys. If we wish to change the format to the common 'WASD' format we can change the array to ['w','a','s','d']. Where would we put this?

```javascript
 <KeyboardEventHandler
            handleKeys={['left', 'up', 'right', 'down', 'space']}
            onKeyEvent={(key, e) => {
                if (!this.props.snake.running && this.props.snake.alive ){
                  this.run()
                }
                this.props.changeDirection(key)
            }} />
```

Notice that there are 2 funcions that we have not seen yet, **this.run()** and **this.props.changeDirection(key)**. We will implement these later.

**QUESTION**

Based on the syntax of **this.run()** and **this.props.changeDirection(key)**. Where are they implemented? 

### 4.3.2 Acting on Input

The purpose of this function is to changes the state of the snake so that we know what direction the snake the user wants the snake to move in. From above, you can see that it is called by the KeyboardEventHandler. This means this function is called everytime you make a keypress. 

```javascript
    changeDirection (direction) {
        let newState = Object.assign({}, this.state);
        newState.snake.direction = direction;
        this.setState(newState);
        this.canvasMoveSnake();
      }
```
As you can see, there is a function call to **this.canvasMoveSnake();**. This function serves the purpose of redrawing the snake.
Something we should consider is how to move a snake? How do we move a snake with a body length of 100? 1000?

```javascript
    canvasMoveSnake(){
        const {ctx, snake} = this.state
        ctx.fillStyle = 'black';
        this.drawRect(snake.tail.x,snake.tail.y,1,1);
        ctx.fillStyle = 'green';
        this.drawRect(snake.head.x,snake.head.y,1,1);
      }
```

Here we have a helper function **drawRect(x,y,l,h)**. We will be drawing cells or rectangles on our canvas very often and instead of flooding our code with **ctx.fillRect(x * cellSize, y * cellSize, l * cellSize, h * cellSize);**. It would be a lot cleaner to use **drawRect(x,y,l,h)** throughout our code.

```javascript
    drawRect(x, y, l, h) {
        const {ctx} = this.state
        ctx.fillRect(x * cellSize, y * cellSize, l * cellSize, h * cellSize);
      }
```

### 4.3.3 Running Game

Earlier, we saw **this.run()** however, we did not know what it did. This is the overview of the code and we will be breaking it down into parts.

```javascript
    run() {
        this.props.snake.running = true;
        var running = setInterval(() => {
            const snake = this.props.snake;

            switch(snake.direction){
                case 'up':
                  snake.head.y -= 1;
                  break;
                case 'down':
                  snake.head.y += 1;
                  break;
                    case 'left':
                snake.head.x -= 1;
                  break;
                case 'right':
                  snake.head.x += 1;
                  break;
                default:
                break;
            }

            if(this.props.snake.running === false){
                clearInterval(running)
            }
            else if (snake.head.x > 29 || snake.head.y > 29 || snake.head.x < 0 || snake.head.y < 0) {
              snake.running = false
              snake.alive = false
              clearInterval(running);
            }

            this.props.changeDirection(snake.direction);
        }, 200 / this.props.snake.speed);
    }
```

Here we update the state of the snake to the running state so that we know that player has started playing the game. we have a variable
set to a **setInterval()** call. The **setInterval** will repeat code that the snake uses while the game is running. It will repear that code every **200 / this.props.snake.speed** milliseconds (in our case our default snake speed is **1** so the interval will fire **5** times per second.

```javascript
    this.props.snake.running = true;
    var running = setInterval(() => { ... }, 200 / this.props.snake.speed);
```

Here we make use of a switch statement to decide how we should move the snake. If our current direction 'up' we will decrement the head of the snake. Do you remember why moving up would require us to decrement the y value of the snake's head?

```javascript
    const snake = this.props.snake;

    switch(snake.direction){
        case 'up':
          snake.head.y -= 1;
          break;
        case 'down':
          snake.head.y += 1;
          break;
            case 'left':
        snake.head.x -= 1;
          break;
        case 'right':
          snake.head.x += 1;
          break;
        default:
        break;
    }
```

Here is something that we **MUST** implement before testing out our game. This is because if we don't implement a way to stop the **setTimeout()**, it will repeat forever and hog all of your computer's resources. 

```javascript
    if(this.props.snake.running === false){
        clearInterval(running)
    }
    else if (snake.head.x > 29 || snake.head.y > 29 || snake.head.x < 0 || snake.head.y < 0) {
      snake.running = false
      snake.alive = false
      clearInterval(running);
    }
```

Lastly, We make a call to **changeDirection** to in order to cause the snake to move accordingly on the canvas.

```javascript
    this.props.changeDirection(snake.direction);  
```

Now that we have the movement logic complete, let's not forget that we have to technically "render" the snake onto our game board even though we are just renderinga  keyboardEventHandler.
 
```javascript
     <Snake snake={this.state.snake}
        changeDirection={this.changeDirection.bind(this)}
     />
```

### 4.3.4 Challenge

At this point, the snake is not completely functional. It does not really "move" the way we want it to. Instead it will create a line tracing out it's path.

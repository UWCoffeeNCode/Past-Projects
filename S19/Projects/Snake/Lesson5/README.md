# Lesson 5: Game Logic

## 4.3.4 Snake Movement Challenge Solution

Recall from last lesson, we left you with a task to fix the problem with the snake movement. The was that moving the snake will leave a trail showing where the snake has moved. We did not provide you a solution last week but we will provide it now.

First we need to keep track of where tail of the snake is in order to "delete it". Recall, we stored properties for the tail of the snake inside the state last lesson:

```javascript
    snake: {
        head: {
            x: 15,
            y: 15
        },
        tail: {
            x: 15,
            y: 15
        },
        // ... Some other snake properties
    }
```

We will leverage this property. Notice that the ground work for "removing" the tail of the snake is already completed in **cavasMoveSnake()** with the lines:

```javascript
    ctx.fillStyle = 'black';
    this.drawRect(snake.tail.x,snake.tail.y,1,1);
```

There is a bug in this that you may discover later on.

**Question** Now, with these two now identified. What must we do in order to remove the tail of the snake?

```javascript
  // Hayden will fill in the solution here after the question as been addressed.
```

**Hint:** This goes into the **run()** function in **snake.js**.

## 5.1 Food Spawning
We want food to randomly spawn across our board. However, one thing we don't would be for the food to spawn in a position where the snake is currently on. 
Thus, our two conditions are:
1. Randomly generate x, y coordinates 
2. If that x, y exists in our snake body, generate another one 

Lets add a new field in our state to track where we currently spawn our food. Lets also make a new function called drawFood()
```
this.state = {
...
    food = {}
}
drawFood () {
  const {ctx, snake} = this.state;
  ctx.fillStyle = 'red';
  var position = {
    x: Math.floor(Math.random() * 30),
    y: Math.floor(Math.random() * 30)
  }
  while (this.exists(position)) {
    position.x = Math.floor(Math.random() * 30);
    position.y = Math.floor(Math.random() * 30);
  }
  this.setState({
    food: position
  })
  this.drawRect(position.x, position.y,1,1);
}
```
drawFood has a while loop which checks for the condition this.exists(position). What this helper will do is check if the point we randomly generated is in the snake. If so, we enter the loop and generate another random pair of x, y coordinates.

```
exists(point) {
  const {snake} = this.state;

  for (var cord in snake.body) {
    if (point.x == cord.x && point.y == cord.y) {
      return true
    }
  }
  return false
}
```

Now all we have to do is add in our drawBoard function. 

However, drawBoard only gets called once during mounting. Therefore, we have to add in the condition to spawn another food if we ate the current one already. We can add this into our moveSnake function.

```
if (snake.head.x === food.x && snake.head.y === food.y) {
  this.addBody();
  this.drawFood();
}
```

## 5.2.0 Snake Body Growth
We can create the addBody function as follows:
```
addBody() {
  const {snake} = this.state
  var newTail = {}
  switch(snake.direction){
    case 'up':
      newTail = {x: snake.tail.x, y: snake.tail.y - 1}
      break;
    case 'down':
      newTail = {x: snake.tail.x, y: snake.tail.y + 1}
      break;
    case 'left':
      newTail = {x: snake.tail.x - 1, y: snake.tail.y}
      break;
    case 'right':
      newTail = {x: snake.tail.x + 1, y: snake.tail.y}
      break;
    default:
      break;
  }
  snake.body.push(newTail)
  snake.tail = newTail
}
```

Finally, we have to update the actual snake body to represent this change. Since we shift our 
```
var newCell = {
  x: snake.head.x,
  y: snake.head.y
}

snake.body.push(newCell)
snake.tail.x = snake.body[0].x;
snake.tail.y = snake.body[0].y;
snake.body.splice(0,1);
```


## 5.2.1 Self Collision
To see if we collided with ourself, all we have to check is to see if our current head coordinate is the same as a body coordinate. We can use a package called lodash to help make this check easier (since they are objects)
```
$ npm install lodash
```
We then have to simply import it. Lodash has a class called _ which we can simply import
```
import _ from 'lodash'
```
This will allow us to easily finish our self collide function
```
selfCollide() {
  const snake = this.props.snake;
  return snake.body.some(cord => _.isEqual(cord, snake.head)) || _.isEqual(snake.head, snake.tail)
}
```
Finally, we just have to add a check inside of our run
```
if (snake.head.x > 29 || snake.head.y > 29 || snake.head.x < 0 || snake.head.y < 0 || this.selfCollide()) {
  snake.running = false
  snake.alive = false
  clearInterval(running);
}
```

## 5.3 Game Flow

Now that we have the game technically functioning. Let's implement the other essential features that makes our game a little more complicated.

### 5.3.1 Border Conditions

Last class we already started to consider the termination of the snake game. If you can recall, we added in an if condition that allowed us to exit out of the **setInterval()** if the snake hits the edges of the board. Of course, it is entirely possible to make the snake wrap around to the other side of the board if it touches the edge, but it will take a little more effort to map this behaviour. Last class we implemented this: 

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

This will stop exit out of out **setInterval()** essentailly stopping the game.

### 5.3.3 Game Over Screen

When the game has ended, we want some way for our to players to know that it is over. Simply we want to display onto the canvas the test "Game Over". There are several ways to do this, but in order to perserve the "Retro" type feel of the game, we will draw onto the canvas the words "Game Over"

```javascript
    endGame() {
        const {ctx} = this.state

        let newState = Object.assign({}, this.state);
        newState.snake.running = false;
        newState.snake.alive = false;
        this.setState(newState);

        //Horizonal Lines
        ctx.fillStyle = 'white';
        this.drawRect(5,9,4,1);
        this.drawRect(5,13,4,1);
        this.drawRect(11,9,2,1);
        this.drawRect(11,12,2,1);
        this.drawRect(22,9,3,1);
        this.drawRect(22,11,3,1);
        this.drawRect(22,13,3,1);

        //Vertical Lines
        this.drawRect(5,10,1,3);
        this.drawRect(10,10,1,4);
        this.drawRect(13,10,1,4);
        this.drawRect(15,9,1,5);
        this.drawRect(19,9,1,5);
        this.drawRect(21,9,1,5);

        //Dots
        this.drawRect(7,11,1,1);
        this.drawRect(8,12,1,1);
        this.drawRect(16,10,1,1);
        this.drawRect(17,11,1,1);
        this.drawRect(18,10,1,1);
    }
```

Here is the code to simply write the word "GAME" I will leave the word "OVER" for you guys to implement.

Now, How do we get this to display? Recall the state properties we used last week "running" and "alive". We will use these to determine if the game ended. In order to do so we will need to make use of this statement:

```javascript
    if (snake.alive === false && snake.running === false){
        this.endGame();
    }
```

**Question:** Where should we put this statement?

### 5.3.4 Auxiliary Controls

In order to make our game more replayable and customizable. We will need to implement some extra controls and fine tune our current controls.

#### 5.3.4.1 Fine Tune movement

The snake should not be able any turns that aren't 90 degrees. In order words, a snake going up should not be able to instantly start going down. It must first go either left or right before heading downwards. Also, if the snake is already moving up, we should not take in any more additional inputs that tell the snake to keep going up. Here is how we can safe guard against these types of movments

```javascript
    if (key === 'up' && (direction === 'down' || direction === 'up')) {
      return
    }
```

This if statement only handles the case stated above. You task is to implement the condtions to handle the other 3 directions.

#### 5.3.4.2 Restart Game

Games should always be restartable without having to reload the entire page. Imagine playing game where you had to turn off your system in order to replay a level. Therefore we need to implment some way for the user to restart the game. Let's set our "restart" to be activated by pressing "r". Recall the KeyboardEventHandler we used for the snake movement?

```javascript
    if(key === 'r'){
        this.resetBoard();
    }
```
  
With this we will call a function called **this.resetBoard()** which should look like this:
  
```javascript
    resetBoard(){
        this.setState(({
            // ...  Something goes here ... 
        }));
    }
```

The state that we are setting should be identical to he **STARTING** state. It is fairly simple to do so I will leave that as an exercise.
  
#### 5.3.4.3 End Game

In addition to restarting game, we should implement a way to allow the users to force a game to end even if the snake is perfectly aive. We will use the KeyboardEventHandler for the key "ESC" to handle this

```javascript
    if(key === 'esc'){
        this.endGame();
    }
```

This is similar to the restart function we implemented above except it leverages the **this.endGame()** function we created earlier.

#### 5.3.4.4 Speed Control

Lastly, in order to cater to players of varying skill levels, we would like to implement a way for our players to adjust the speed of the snake to their liking. In order to do that, we will need to assign two keys (similar ot how we assign "r" to restart and "esc" to exit) to handle increasing speed and decreasing speed. I will let you decide which keys you would like to assign these to.

Let's look back at the state we created for the game. More specifically let's focus on one convienent property - the **speed** property.

```javascript
    this.state = {
            snake: {
            // ... other properties
            speed: 1
        }
    }
```

We will use this to determine the speed in conjuction with the **setInterval()** function in **snake.js**:

```javascript
    var running = setInterval(() => { //... Some Snake Stuff }, 200 / this.props.snake.speed);
```

Now, let's create a way to speed up the snake:

```javascript
    speedUp(){
        let newState = Object.assign({}, this.state);
        newState.snake.speed = this.state.snake.speed * 2;        
        this.setState(newState);
    }
```

The speed down function is nearly identical so you can implement that yourself.

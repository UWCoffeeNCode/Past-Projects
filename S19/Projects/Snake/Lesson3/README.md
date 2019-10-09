# Lesson 3

# 2.3 Continuing from last week (Git)
1. Install git first: https://git-scm.com/downloads
2. Create a github account: https://github.com/
3. Open up terminal/command prompt
4. Set your username
```
$ git config --global user.name "Mona Lisa"
```
5. Verify you set username properly
```
$ git config --global user.name
```
6. Set your email
```
$ git config --global user.email "email@example.com"
```
7. Verify you set email properly
```
$ git config --global user.email
```
8. Follow https://help.github.com/en/articles/create-a-repo UP UNTIL "Commit your first change"
9. Navigate to your snake project
10. Add it onto git! 
```
git init
git add .
git commit -m "first commit"
git remote add origin your-url-here
git push -u origin master
```

## 3.1 Getting started
We will now finally jump in to creating our own snake game! Usually when we work on a new project, it is easiest to first get something to work with and continue building from there. In our case, we will first create a grid. So Lets first create a new class: board.js.

## 3.2 Defining constants
In any project, it is good practice to first define any constants. This is because not only does it make our code more readable, it also helps reduce errors since we will not be able to modify their value. For our game, we'll set our board size and cell size (size of each pixel) to be constants. In the future, if you ever see yourself using the same number repeatedly, it is probably a good idea to make it into a constant.
```
const boardSize = 720
const cellSize = boardSize / 30;
```

## 3.2 Canvas
Canvas is part of HTML and it allows us to draw graphics on a web page through Javascript. Think of it as We will be using this to create all our game graphics. There is so much functionality already created in the programming world but how do we know what does what? This is when we refer to google and search up website documentation. For example, we can find a tutorial on canvas over here: https://www.w3schools.com/html/html5_canvas.asp. We can then look at all the functions we have avaliable to use and choose accordingly. To initialize a canvas, we call it like any other HTML tag (as seen in the link).
```
<canvas id='gameBoard' ref="gameBoard" width={boardSize} height={boardSize} />
```
Notice how we pass in 4 parameteres:
id: Unique identifier. This allows us to "name" our canvas
ref: This creates a reference to what we want to display.
width: The width of our canvas
height: The height of our canvas

We're also going to create a new scss class so we can make our background black (just for aesthetics). Lets name it board.scss
```
#gameBoard{
    outline: 1px solid white;
}
```
Our canvas is looking for a reference called "gameBoard". However, that currently doesn't exist, so lets create it!

## 3.3 Game board
We can create a new function called drawBoard. What this function will do is create our board itself. This will be done via canvas calls. As we progress our snake game, we will add more functionaliry into drawBoard such as drawing the snakes and food. For now, let us first get a grid going. We will also introduce a new way to setState (via the code). This way differs from the way we taught last week is that we want to execute something immediately after our state is updated. 
```
drawBoard(){
  const canvas = this.refs.gameBoard
  this.setState({
    canvas: canvas,
    ctx: canvas.getContext('2d')
  }, function () {
    this.drawGrid();
  })
}
```

## 3.4 Grid
A lot of the drawing will be handled by ctx. For example, strokeStyle and fillRect() are all predefined and we can simply tell it to do the dirty work for us.
Quiz time: Why does strokeStyle not have parenthesis but fillRect() does?

```
drawGrid() {
  const {ctx} = this.state

  ctx.strokeStyle = 'grey';
  ctx.fillRect(0, 0, boardSize, boardSize)
  for (var vertical = cellSize; vertical < boardSize; vertical += cellSize){
    ctx.beginPath();
    ctx.moveTo(vertical, 0);
    ctx.lineTo(vertical, boardSize);
    ctx.stroke();
  }

  for (var horizontal = cellSize; horizontal < boardSize; horizontal += cellSize){
    ctx.beginPath();
    ctx.moveTo(0, horizontal);
    ctx.lineTo(boardSize ,horizontal);
    ctx.stroke();
  }
}
```
We finished all the code for drawing the board in drawBoard()... but we never actually called it! We now have the question of where should we call it even? Introducting React lifecycle functions. These are functions built into React that will be called whenever a certain componenet reaches a certain state. For example, there is a function that will automatically be called when the componenet is being created and when it is removed. We are intrested on when it first gets created. You can read up more about this here:https://reactjs.org/docs/react-component.html
```
componentDidMount () {
  this.drawBoard();
}
```

## 3.5 Putting it all together
Now that we have all the code ready, we just have to link it all together! If we go into App.js, we simply have to import our Board class and tell it to render inside of our render function. This will be the exercise for today! (Feel free to reach out to Hayden and Patrick for help)

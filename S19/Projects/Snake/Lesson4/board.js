import React from 'react'

const boardSize = 720
const cellSize = boardSize / 30;

class Board extends React.Component{
    constructor(props){
        super(props);
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

    drawBoard(){
        const canvas = this.refs.gameBoard
        this.setState({
          canvas: canvas,
          ctx: canvas.getContext('2d')
        }, function () {
          this.drawGrid();
          this.drawSnake();
        })
    }

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

    drawSnake(){
        const {ctx} = this.state;
        ctx.fillStyle = 'green';
        snake.body.forEach(cord => {
            ctx.drawRect(cord.x , cord.y, 1, 1)
            
        });
    }

    changeDirection (direction) {
        let newState = Object.assign({}, this.state);
        newState.snake.direction = direction;
        this.setState(newState);
        this.canvasMoveSnake();
      }

    canvasMoveSnake(){
        const {ctx, snake} = this.state
        ctx.fillStyle = 'black';
        this.drawRect(snake.tail.x,snake.tail.y,1,1);
        ctx.fillStyle = 'green';
        this.drawRect(snake.head.x,snake.head.y,1,1);

              if (snake.alive === false && snake.running === false){
        this.endGame();
      }
    }

    drawRect(x, y, l, h) {
        const {ctx} = this.state
        ctx.fillRect(x * cellSize, y * cellSize, l * cellSize, h * cellSize);
      }

    render(){
        return(
            <div>
                <canvas className='mx-auto my-5' id='gameBoard' ref="gameBoard" width={boardSize} height={boardSize} />
            </div>
        )
    }

}

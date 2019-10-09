import React from 'react';
import KeyboardEventHandler from 'react-keyboard-event-handler';

class Snake extends React.Component{

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

    render(){
        if(this.props.snake.newDirection !== '' && !this.props.snake.running && this.props.snake.alive){
            this.run()
        }
        return(
            <KeyboardEventHandler
            handleKeys={['left', 'up', 'right', 'down', 'space']}
            onKeyEvent={(key, e) => {
                if (!this.props.snake.running && this.props.snake.alive ){
                  this.run()
                }
                this.props.changeDirection(key)
            }} />
        );
    }
}

export default Snake;

# Lesson 1
## What is a Web App?
According to Wikipedia, a web app is a client-server computer program that can be ran off of a web browser. Some examples of common web applications are e-commerce sites (amazon.com) and emails applications (gmail).

Because the web is accessible from many different devices (computers, tablets, phones, etc.), we need to accommodate for most if not all devices that utilizes these browsers to a reasonable degree. We need to consider mobile compatibility for tablets and or phones. We also need to consider the compatibility of different screen resolutions. 

In our case, a 'reasonable degree' means that we should accomodate computers and tablets. In terms of phone compatibility of our game, it would be better to make an mobile version of the game instead of a web-based version of the game.

We also need to ensure that out interface is usable and intuitive. We do not want to provide an application with no instructions because the end-users will not know how to use the app. We also do not want to flood our view with too much stuff as it will cluster our interface into mess that will deter our audience. The interface must be intuitive so that users do not waste too much time learning the controls. It also must behave the way it is intended to behave, the left arrow button should NOT cause the player object to move in any direction except towards the left. Our restart button must actually restart the game.

## What will we be using?
We will be using the triple threat of technologies used accross the web. 

### HTML
We will be using HTML (a.k.a Hypertext Markup Langauge). As the name suggests, HTML is a markup langauges there are debates on whether or not HTML should be considered a programming language or not (we will not go into this). HTML is what creates the structure and layout of a web page using various different elements and attributes. Many of these elements will be seen in later lessons.

```html
<div>
  <h1>Hello </h1>
  <h2>Hello again</h2>
  <h3>Hi </h3>
  <h6>????</h6>
  <div> Yay, something new! Sorta... </div>
  <div class='makeMeRed'>
    <span>Yay something actually </span> <span>new</span>
  </div>
  <ul>
    <li> I </li>
    <li> am </li>
    <li> an </li>
    <li> unordered </li>
    <li> List </li>
    <li> :) </li>
  </ul>
  <ol>
    <li> Another </li>
    <li> list </li>
    <li> but </li>
    <li> ordered </li>
   </li>
  </ol>
  <p> Just a paragraph. <p>
  <div>
    <button id-'uselessButton'> OOOOooo a button! </button>
    <div class='makeMeRed'>
      <a href='https://waterlooworks.uwaterloo.ca/home.htm'> Click me to get needlessly stressed! </a>
    </div>
  </div>
  <img src='https://i.imgur.com/uf9YNVm.png'></img>
</div>
  
```

### CSS
CSS (a.k.a Cascading Style Sheets) will be used as well to give our project some life and colour. CSS is a style sheet language and it describes the presentation of a web page that is written in HTML. It is very versatile and can be used in many ways such as colouring elements to providing elements with animations. 

```css
#uselessButton{
  width:100%;
}

.makeMeRed{
  background-color: red;
}

p{
  font-size: 20px;
}

div span{
 border: 1px solid black;
}
```


### JavaScript
We will be using JavaScript as our primary language. JavaScript is one of the most popular dynamic programming languages used for creating and developing websites and web applications. The largest difference between dynamic and static programming langues is Dynamic typing. In Dynamic typing, the data type of each variable is only known when the program is running whereas statically typed variables are pre-determined before execution. 

### Analogy
Let's pretend that our web application is a house. We have the walls, floors, stairs, and etc., we can consider these as the elements of our application - the HTML portion. Next, we have paint, carpet, appliances, and etc., these can be considered the styling of our elements - the CSS applied onto the HTML. Finally, we have the electrical wiring, piping, ventilation, and etc. this is the hidden part that not many see - the JavaScript that works on the elements and styles. 

## Visual Studio Code
  We will be using Visual Studio Code as the IDE (Integrated Development Enviroment) for our project. This is because, it comes with a built in command terminial which will make our lives significantly easier and less painful. :)
  
  You may download it here: https://code.visualstudio.com/
  
  After you download and install it, you may play around and discover its abundance of features and use it to test out the things below!

## JavaScript 101 
  -	Declarations: Let, const, var
    ```javascript
    let variableA = 'a';
    const variableB = 'b';
    var variableC = 3;
    ```
  -	Arrays and basic array operations
  
    ```javascript
    let arr = [];
    
    arr.length; // value of 0
    
    arr[0] = 'hello';
    
    arr.length; // value of 1
    
    console.log(arr[0]); // will print 'hello' to console
    
    ````  
  - Objects and basic object operations
    ```javascript
    let car1 = {};
    car1.name = 'BMW'
    car1.colour = 'white'
    console.log(car1.name); // will print 'BMW' to console
    
    let car2 = {
      name: 'BMW'
      colour: 'white'
    };
    
    // obj2 and obj1 are the same at this point
    
    obj2.obj = obj1;
    
    // You can next objects inside of another object.
    
    ```
  - for/while loops
    ```javascript
    for ( var i = 0; i < someNumber; i++){
      // do something
    }
    
    while someBoolean{
      // also do something
    }
    ```
  -	Creating a function
    ```javascript
    function toCelsius(fahrenheit) {
      return (5/9) * (fahrenheit-32);
    }
    ```
  -	Playing with JavaScript with web development tools
    - Access it by pressing F12 on your keyboard. You can then play in the console!
  -	Power of console.log()
  
  
## React Preview (Next lesson)

###	React Components
```javascript
import React from 'react';

class comp extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      // State elements
    }
  }

  someHandler(someVariable){
    // do something
  }

  render(){
    return(
      <div id='someElement'>
        // child elements
      </div>
    )
  }
}
```

# Lesson 2: Enviroment Setup

## 2.1 Technologies

### 2.1.1 Visual Studio Code
We will be using Visual Studio Code as the IDE (Integrated Development Enviroment) for our project. This is because, it comes with a built in command terminial which will make our lives significantly easier.

You may download Visual Studio Code here: https://code.visualstudio.com/

### 2.1.2 Node.js
Node is a cross-platform JavaScript run-time enviroment. Cross platform means that it can run on Windows, MacOS, and Linux based systems. The run-time enviroment allows Node to run JavaScript Code outside of a web browser. There are many neat features and advantages that come from using node such as file operations on a server, data collection, database modification and most importantly (for us) generation of dynamic pages.

You may download Node.js here: https://nodejs.org/en/

Node also comes with a package management software called "Node Package Manager" (npm) and it is often used for JavaScript development projects. It allows for users to download free and/or premium packages from online databases. We will be leveraging some of these free packages for our project.

Please check that you have npm installed.
1. Open Visual Studio Code
2. Search for the 'terminal' menu at the top and click on 'New Terminal'
3. Type 'npm --version'

### 2.1.3 React.js
React is an open-source JavaScript library used to create user interfaces. It is maintained by Facebook primarily but since it is open-source, there are many individuals and/or organizations who maintain it or variations of it as well. React is very popular in the industry because of it capabilities in both web and mobile apps as well as its strength in building reusable user interfaces.

We can install React as well as start the structure of our application with this command:
```
npx create-react-app some-app-name
```

In the future, If you would like to update your React, you can type the command:
```
npm install react-scripts@latest
```

After all the libraries have installed and the React application structure has been completed, move into the application directory and start the application. Use these commands
```
cd .\some-app-name\
npm start
```

Now your web browser should open itself up with the URL localhost:3000 (or something similar) and you should see the default page.
Note: In your own time, if you would like to learn more about React, studying this default application is a good place to start. Naturally, if you're confused about anything you may message us via Slack.

### 2.1.4 BootStrap
BootStrap is a front-end framework for CSS. It is a very powerful and popular framework beacuse of its responsiveness to different screen sizes and ability to handle mobile web views. It has serveral CSS and JavaScript designs which eliminates the tedious work behind web design.

Install:
```
npm install boostrap
```

### 2.1.5 SASS
SASS (also known as Syntactically Awesome Style Sheet) is a Style Sheet langauge which is an extension to CSS. In fact, SASS, when passed through a complier, turns into CSS which is then used for styling our page. Thus, everything you can do in CSS can be done in SASS. However, SASS allows for the use of variables in your styling which provides more intuitive experience for developers. There are also many subtle differences between the two and many of these makes designing a lot easier and faster. For example, the ability to nest CSS classes within other classes makes the styling a lot easier to read. 

Install:
```
npm install node-sass
```

### 2.1.6 Lodash
Lodash is a JavaScript Library that provides useful utilities for common programming tasks. For example, checking if two arrays are equal. This allows us to ignore the tasks of creating these utilities ourselves which in turns saves us time. The reason we aren't going to make these ourselves is because many of these are very simple to implement but take unneccessary amount of time. Also if we implement these on our own, we are prone to errors and bugs. 

Install:
```
npm install lodash
```

## 2.2 In-Depth Look at React
### 2.2.1 How does everything display?
By convention, the 'index' page is what is usually displayed first it is sometimes referred to as the "home" page. In our case we have an 'public\index.html' file that looks somthing like this:

```html
<!DOCTYPE html>
<html lang="en">
    <head></head>
    <body>
        <div id="root"></div>
    </body>
</html>
```

There can be a lot more on this .html file but we will focus on the div element with id='root'. This element is how React generates our Components. React targets this element in the 'src\index.js' file which has the line:

```javascript
ReactDOM.render(<App />, document.getElementById('root'));
```

A "DOM" is a "Document Object Model" which is a programming interface for HTML. What this line does is that it tells React to render onto the DOM the "App" component using the HTML element with id='root'. Which we have seen in the 'index.html' code above.

The App component can be found at 'src\App.js'. It may look something like this:

```javascript
import React from 'react'

function App(){
    return(
        <div className='App'>
            {/* Do Something */}
        </div>
    )
}

export default App
```

This function is essentially one of the ways to create a component. This Component will generate the return HTML element for every instance of <App /> that is called. Within the div element we can choose to generate more Components that we can define later.

### 2.2.3 Components
React Components are the building block on any React application. Most applications will contain many of these. They accept input in the form of properties and may use these properties to dictate how a particular section of a user interface should appear. A component may look like this:

```javascript
import React from 'react'
import ComponentB from './ComponentB
import './ComponentA.scss'

class ComponentA extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            display: 'Hello World!',
            toggle: true
        }
        
        this.clickHandler = this.clickHandler.bind(this)
    }

    clickHandler(){
        let newState = Object.assign({}, this.state)
        newState.toggle = !newState.toggle
        this.setState(newState)
    }

    render(){
        return(
            <div className='ComponentA'>
                <ComponentB />
                <div>{this.state.display}</div>
                <button onClick={this.clickHandler}>
                    {this.state.toggle ? 'True' : 'False'}
                </button>
            </div>
        )
    }
}

export default ComponentA
```
### 2.2.4 Rendering
This component named 'ComponentA' will be rendered with every call to '<ComponentA />'. However, in order for another component to do so, we need to export this Component. This is done through:

```javascript
export default ComponentA
```

Also, in order to render a component in our component we must first import it. In our example, we are rendering 'ComponentB' so we would need to import this 'componentB' through:

```javascript
import ComponentB from './ComponentB'
```

It is important to note that in the return call of the render() function, we are wrapping everything in one HTML element. 
```javascript
render(){
    return(
        <div className='ComponentA'>
            <div>{this.state.display}</div>
            <ComponentB />
        </div>
    )
}
```

This is NOT a conincidence between the two examples. A component can only render one HTML element. However inside this one element, we can nest severel more HTML elements and/or components.

### 2.2.5 States
The state of a component represents what in that component can change. The state can represent many things different things such as Sub-Titles for article sections and (in our case) the score of a game. The state is also a means by which components can communicate with one another. In React, when a state changes, all components that have an instance of that state (or the part of the state that changed) must REACT to that change and update accordingly. This can be simplying changing what a displayed on the screen to generating/removing an element from the interface. The state is stored in the constructor of our component and it may look something like this:

```javascript
constructor(props){
    super(props);
    this.state = {
        display: 'Hello World!'
    }
}
```

In our state, we have a property with the key 'display' and value 'Hello World!'. By itself it does not mean much. However, we can access this property later on and render the value onto the display by doing something like this:

```javascript
<div className='ComponentA'>
    <div>{this.state.display}</div>
</div>
```

Now, when ComponentA is rendered, it will also render a div element that displays the value 'Hello World!'. If this property were to mutate into a different value later on, the component will act accordingly and display the new value.

We never change a component's state directly unlike how we access a component's state. For example, we never do this:

```javascript
this.state.display = 'Goodbye World!
```

The reason we never change the state directly is because doing so can cause weird bugs to appear and in general, it's not worth the headache. Instead, to change states we will do this.

```javascript
    let newState = Object.assign({}, this.state)
    newState.display = 'Goodbye World!'
    this.setState(newState)
```

First we make a copy fo the orginial state using Object.assign which takes an empty object and assigns the properies in this.state to it. Then we directly manipulate this newState and change the properties that it holds. Finally we set the current state to be the new state that we defined. This is approach will not cause the weird bugs that we get from directly manipulating the orgininal state.

### 2.2.6 Event Handlers
An 'event' is an interact between our page and the user that is recognized by some sort of input. For example, clicking a button is a type of event that we can act on.
Here is an example of an event handler for clicking on a button:

```javascript
clickHandler(){
    let newState = Object.assign({}, this.state)
    newState.toggle = !newState.toggle
    this.setState(newState)
}
```

This handler performs a state change between true and false boolean values. In order to call this handler, we can attach it to a button element in our component to trigger this function when the button is clicked. We can do so like this:

```javascript
<button onClick={this.clickHandler}>
    {this.state.toggle ? 'True' : 'False'}
</button>
```

This button will initially display the word 'True'. When clicked, it will toggle between displaying 'True' and 'False' This is because 'this.state.toggle' switches between true and false values. 

Side note: in this example we have a ternary operator. It is hard to explain how this works exactly however, it is easier to show you how it works:

```javascript
// Ternary Operator
this.state.toggle ? 'True' : 'False'

// the ternary operator is the same as this if-else scenario.
if (this.state.toggle == true){
    return 'true'
}
else{
    return 'false'
}
```

Back to the button. At this point, the button will not actually work. We still have one more step we must complete before we can get the handlerto trigger. That is, we still need to bind the handler to the current class (the component). We do so by doing:

```javascript
this.clickHandler = this.clickHandler.bind(this)
```

We put this line of code inside the constructor along with the state. By doing this, we are now able to access the handler through the 'this' pointer which allows us to call the handler via clicking our button.

## 2.3 Git Tutorial
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


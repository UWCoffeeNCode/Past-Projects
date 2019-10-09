# Lesson 2

Goals:
+   Install everything we need to work on our React App this term ✅
+   Learn to open and use the command line ✅
+	Set up some files we will be using this semester ✅
+	Learn some things that make React different from HTML / CSS ✅

## Downloads 🔄
To start building our React App, we will need to download the following things:
+ <a href="https://code.visualstudio.com/download">Virtual Studio Code</a>
+ <a href="https://nodejs.org/en/download/">Node.js</a>

## CommandLine 🖥
The rest of our "downloading" will take place on the command line! We will walk you through the basics of using the command line if you have never touched it before!

To open the terminal on Mac, click the spotlight search in the upper right-hand corner and search "Terminal". Hit enter to open a new terminal session.

To open the Command Prompt on Windows, search the application in your computer (Windows key > "Command Prompt"). Hit enter to open a new Command Prompt session.

The command line is like a text-only version of where all your files are stored (like Finder on a Mac). You use written commands to navigate through folders. The left side of the text tells you which folder you are currently located in

+ `ls`: lists all the files and folders in your current directory
+ `cd FOLDERNAME`: cd stands for "change directory", and this is equivalent to clicking on a folder
+ `cd ..\`: equivalent of backing out of a directory

Before we install everything else, you need to `cd` to whatever directory you would like to store your website folder code in. You do not need to create a new folder for it though - we have commands that do it for you!

Now type: `npx create-react-app website`
This will create a new folder called website, and inside it all the rudimentary code necessary to start building your React project. This may take a few minutes.

Now go `cd website`. You should see a whole bunch of folders. This is where all your code will be stored! Type `npm start` to open up a localhost server to see what is already there.

We type `npm start` whenever we start coding again to see our updates take place live on the server. A localhost server is only visible to you on your computer, right now.

## Why React
Why are we learning React now and not sticking with CSS and HTML? What is the connection from React to HTML?

React is a UI library and framework that helps manage your code for you. It allows us to build reusable components, and lets us see the updates we make to our code LIVE.  

## Folder Structure and Files

A lot of files are automatically added to your app when you first start it up.

Whenever you set up a new React file, you will see that there are files that already come with the app. These files are index.js, index.html, and style.css.

There are also the dependencies react-dom and react, which we will be getting into shortly. 

Each file has the type at the end after the period, which indicates what language it is in. So index.js is in JavaScript, index.html in HTML, style.css in CSS.

#### 📃App.js
This is our only component right now! We will get more into how React works and how it compares to HTML next week, but for now we will take you through the simplest parts of a React component.

```javascript
import React from 'react';

class App extends React.Component {
    render() {
        return (
            <div>
                YOUR HTML CODE GOES HERE
            </div>
        );
    }
}
export default App;
```


#### 📃App.css

This is our main CSS file. You can start adding your own classes here. You can also remove everything currently existing in this file. We will discuss CSS more in future lessons. 

## Assignment
Inside src, set up a components folder and an images folder, like so:

```
📁 src   
├── 📁 components   
├── 📁 images   
```
Inside the components folder, add the following empty files:
```
📁 src   
├── 📁 components  
    ├── 📃HomePage.js
    ├── 📃About.js
    ├── 📃Experience.js
├── 📁 images   
```

Add the following code to each file. Make sure you swap out where it says "HomePage" for the name of each file individually! This is creating React components. We will be discussing this much more indepth next week.

```javascript
import React from 'react';

class HomePage extends React.Component {
    render() {
        return (
            <div>
                This is the HomePage component.
            </div>
        );
    }
}

export default HomePage;
```

Inside the images folder, add any images you think you might like to use on your website! This could include logos for LinkedIn, twitter, etc, a portrait, a photo for the background, or anything else! Get creative. Remember, you can use images to represent buttons and hyperlinks as well.

## index.js: ReactDOM & JSX

**render**: the process of transforming your react components into nodes that your browser can understand and display on the screen

#### BEFORE
```javascript
import React from "react"
import ReactDOM from "react-dom"

// JSX
ReactDOM.render(WHAT I WANT TO RENDER, WHERE I WANT TO RENDER IT)
```

**NOTE**: // allows us to make comments in our JS code. It is good practice to add comments to your code as you go to help you understand your own thought processes when you look back at it. 

In our JS files, we are actually also using JSX, which is JS version of HTML. Don't worry too much about this though, we will explain as we go! :)

#### AFTER
``` javascript
import React from "react"
import ReactDOM from "react-dom"

// JSX
ReactDOM.render(<h1>Hello world!</h1>, document.getElementById("root"))
```

## index.html

You should see something like this: 
``` html
<html>
    <head>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <div id="root"></div>
        <script src="index.pack.js"></script>
    </body>
</html>
```

If you look at the div tags, you can see that there is an id called “root”. This is the id we referenced in our index.js file where we state “WHERE I WANT TO RENDER IT”. It’s like a container for our entire app. We don’t really need to touch this file just yet. 

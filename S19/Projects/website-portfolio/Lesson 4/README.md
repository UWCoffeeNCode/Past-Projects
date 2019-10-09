## Goals
+ Create website header
+ Make hyperlinks in header scrollable to different parts of the website

## React References
We need a constructor in order to create "references". References are like labels that we attach to different components we have set on the page. Every time you create a new component, it can have a unique reference. For example, last class we create an `<Icon />` component, which can be reused to make many different icons. Each of these icons can have its own unique reference! The reference keeps track of where the component is positioned on the page, and a couple of other things. We will see why this is important in a minute.

We create references using a special function called a `constructor`. It always goes right after the class ___ extends Component line - i.e. it should always be the first thing inside your component.

```javascript
constructor (props) {
    super(props);
    this.myAbout = React.createRef();
    this.myExperiences = React.createRef();
}
```

## Attaching references to components
Now, we want to attach these references to our `<About />` and `<Experience />` components. On our main App page, where we render these components, we will first want to wrap them in divs like this:

```javascript
<div>
  <About />
</div>
```

The benefit of this is that we can attach classes and references and other important things to this div to have it apply to the component. Now we can do this!

```javascript
<div ref={this.myAbout}>
  <About />
</div>
```

This means we can use this reference now to do exciting things, and it will apply them to our `<About />` component!

## Scrolling Functions
We now want to create our first React functions!! They look like this:

```javascript
scrollToAbout = () => window.scrollTo(0, this.myAbout.current.offsetTop)
scrollToExperiences = () => window.scrollTo(0, this.myExperiences.current.offsetTop)
```

And we're gonna want to put them right below our constructor line. These functions take the reference and tell the page to scroll to the top of where that div starts.

// Go through syntax of what these functions are doing a bit more

## Connect it all together
Final steps! Inside our `Homepage` component, we're gonna build our header inside the div. Inside the header, we will create a button for each of the sections we want to be able to move to. We can then use CSS to make the buttons look nice. Each button will need an onClick function.

```javascript
<button onClick={this.props.scrollToAbout}>About</button>
<button onClick={this.props.scrollToExperiences}>Experience</button>
```

Now in `App.js`, all we have to do is pass these functions down to the Homepage as props!

```javascript
<HomePage
  scrollToAbout={this.scrollToAbout}
  scrollToExperiences={this.scrollToExperiences}
/>
```

To summarize the order of how all of this goes, it's ...
1. import React from "react"
2. class ______ extends Component
3. constructor
4. functions 
5. render(), return (), etc
6. export default ______

## CSS ??
Finally, for smooth clicking, we want to add this CSS to the entire document:

```CSS
html {
  scroll-behavior: smooth;
}
```

We can use this CSS to make the buttons more transparent:
```CSS 
.headerTabs {
  background: transparent;
  border: none !important;
  cursor: pointer;
  font-size: 20px;
  padding: 0 15px;
  float: right;
  &:hover { transform: scale(1.1); }
}
```

Finally, we can use this kind of CSS to make the header stick to the top of the page, if you would like!

```CSS
.sticky {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: white;
}
```
HERE IS THE LINK FOR THE GOOGLE FONTS!! it will walk you through setting it up in your code, but do not hesitate to ask us for help!!
https://fonts.google.com/

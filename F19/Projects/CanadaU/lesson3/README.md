# Lesson 3 - Creating Front End with React

### [Project](https://github.com/MichaelAEden/DashForReddit) (in progress)
### [Slack](https://bit.ly/uwcoffeencodeslack), channel is `#canada-u`
### [Slides](https://docs.google.com/presentation/d/18XiKvAeL1BmKMvyoIWp1Ge9xaQolQqOWtoEoP4wfyjA/edit?usp=sharing)

### Objectives:

1. Learn the fundamentals of React
2. Create a user-interface using React

## Getting Started

1. Install [Node](https://nodejs.org/en/download/)
2. Go to the project folder `CanadaU` (or create a new one if you missed the last workshop).
3. From your terminal, navigate to the `CanadaU` folder (e.g., `cd ~/Desktop/CanadaU`.
<br>For help, see [this guide](https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101)(skip to "Finding Your Way Around")
4. Create a new React app:
```bash
npx create-react-app react-app
```
5. Start the app:
```bash
cd react-app
npm start
```
6. Go to <http://localhost:3000/> to see your app in action.
<br>

## React

<b>React</b> is a JavaScript library for building <b>component-based</b> user interfaces.
<br>
We'll use React for our project <b>front end</b>. It will fetch data from our back end (Flask) and present it to the user.
<br>
<br>
Go to `CanadaU/react-app/src/App.js` and replace its contents with the code below:

```javascript
import React from 'react';

function App() {
  return <p>Hello world!</p>;
}

export default App;
```

Go back to <http://localhost:3000/> and you should see it update!
<br>
To add some styling, create a file in the same `src` folder called `App.css`. Copy from [App.css](https://github.com/UWCoffeeNCode/Lessons/blob/master/F19/Projects/CanadaU/lesson3/App.css) (I won't be covering CSS in this lesson, but there are lots of tutorials online).
<br>
<br>
Edit `App.js` to use our CSS file:

```javascript
import React from 'react';

// Import our styles.
import './App.css';

function App() {
  // Here `className` is only used for styling.
  return <div className="App">Hello world!</div>;
}

export default App;
```

## HTML

If you've used HTML before, skip to the next section.
<br>
<br>
<b>Hyper Text Markup Language</b> (HTML) is a language used for creating web pages.
<br>
<br>
HTML is made up of <b>tags</b>, and each type of tag serves a different purpose.
<br>
Tags are almost always used in pairs, with one opening tag and one closing tag.
```html
<tagname>content goes here...</tagname>
```

Examples of common tags:
- The <b>header</b> (`h1`) tag displays a title.
- The <b>paragraph</b> (`p`) tag displays text.
- The <b>anchor</b> (`a`) tag displays a link.

```html
<h1>Hello world!</h1>
<p>This is a paragraph.</p>
<a href="uwaterloo.ca">click me!</a>
```

Note how the anchor tag has an `href` <b>attribute</b> which defines what the link is.
<br>
Different tags have different types of attributes
<br>
<br>
Tags can also be <b>nested</b> inside each other.

```html
<h1>Hello world!
    <a href="uwaterloo.ca">click me!</a>
</h1>
```

Try it out for yourself on [CodePen](https://codepen.io/pen/)!

```html
<h1>Hello world</h1>
<p>
    This is a paragraph.
    <a href="https://uwaterloo.ca">click me!</a>
</p>
<img src=https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png />
```

## JSX

[JSX](https://reactjs.org/docs/introducing-jsx.html) is used to embed JavaScript in HTML.
<br>
<br>
For example:

```javascript
function App() {
  return <p>One plus one is {1 + 1}</p>
}

```

Everything in the `<p>...</p>` tags is HTML.
<br>
Everything in the `{...}` is JavaScript.

## React Components

In React, each component is defined by a <b>function</b> which:
1. Might take <b>properties (props)</b> as input
2. Returns how the component should look

We currently only have an `App` component, and it doesn't do much.

Let's have it display information about a Subreddit.

```javascript
function App() {
  // NOTE: className is only used for styling.
  return (
    <div className="App">
      <h1>uWaterloo</h1>
      <p>Subscribers: 44000</p>
    </div>
  );
}
```

If we wanted to do this for multiple Subreddits, we could copy and paste the code over and over,
<br>
<b>OR</b> we can create a new component called `Subreddit` which takes `displayName`, and `subscribers` as input (in the form of <b>props</b>).

```javascript
function App() {
  return (
    <div className="App">
      <Subreddit
        displayName="uWaterloo"
        subscribers={44000}
      />
      <Subreddit
        displayName="UofT"
        subscribers={3}
      />
    </div>
  );
}

function Subreddit(props) {
  return (
    <div className="Subreddit">
      <h1>{props.displayName}</h1>
      <p>Subscribers: {props.subscribers}</p>
    </div>
  );
}
```

We use JSX to access the props and display them in HTML (e.g., `{props.displayName}`).

## Creating Components from Raw Data

When we connect our front end to our back end, we'll receive information about our subreddits as raw data.
<br>
We need to take this data and display it somehow.
<br>
<br>
For example, if our data is as below:
```json
// Subreddit 1
{
    "displayName": "uwaterloo",
    "subscribers": 44444,
    "icon": "https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png"
},
// Subreddit 2
{
    "displayName": "UofT",
    "subscribers": 3,
    "icon": "https://a.thumbs.redditmedia.com/SsZbo9uA8c68Lhc68dk59PuZkjm_gnxNBx2e14haVY8.png"
}
// and so on...
```

then we need to process it and display it as follows:

```javascript
function App(props) {
  const subreddits = [
    // Subreddit 1
    {
      displayName: 'uwaterloo',
      subscribers: 44444,
      icon:
        'https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png'
    },
    // Subreddit 2
    {
      displayName: 'UofT',
      subscribers: 3,
      icon:
        'https://a.thumbs.redditmedia.com/SsZbo9uA8c68Lhc68dk59PuZkjm_gnxNBx2e14haVY8.png'
    }
  ];

  // NOTE: the map function loops over all the data.
  return (
    <div className="App">
      {subreddits.map((subreddit, i) => (
        <Subreddit
          key={i}
          displayName={subreddit.displayName}
          subscribers={subreddit.subscribers}
        />
      ))}
    </div>
  );
}
```

## Next Steps

Now that you know the basics of React, try the following challenges.

1. Add a website title using the `h1` tag.
	- <b>Hint</b>: use `className="App-title` to give it the right style. 
2. For each subreddit, display the subreddit banner image.
    - <b>Hint</b>: use an `img` tag, and use `className="Subreddit-icon"` to display it with the right style.
    - <b>Hint</b>: pass an `icon` attribute into the `Subreddit` component the same way as `displayName` and `subscribers`. 
3. Let a user favourite a subreddit (favourites will disappear after refreshing the page).
	- <b>Hint</b>: use [component state](https://reactjs.org/docs/hooks-state.html#recap)
4. Display the top words used in a subreddit, using the data provided below.
    - <b>Hint</b>: use a [word cloud component](https://github.com/Yoctol/react-d3-cloud)

```
// uWaterloo
wordCounts: [
{ text: 'day', value: 42 },
{ text: 'busan', value: 23 },
{ text: 'waterloo', value: 20 },
{ text: 'uw', value: 19 },
{ text: 'uwaterloo', value: 18 },
{ text: 'week', value: 18 },
{ text: 'like', value: 17 },
{ text: 'goose', value: 15 },
{ text: 'people', value: 15 },
{ text: 'students', value: 13 },
{ text: 'today', value: 12 },
{ text: 'year', value: 11 }

// UofT
wordCounts: [
{ text: 'uoft', value: 38 },
{ text: 'exam', value: 17 },
{ text: 'like', value: 15 },
{ text: 'people', value: 15 },
{ text: 'test', value: 15 },
{ text: 'today', value: 13 },
{ text: 'course', value: 12 },
{ text: 'campus', value: 11 },
{ text: 'year', value: 11 },
{ text: 'students', value: 10 },
{ text: 'bad', value: 10 }
```

Some solutions are in [Solutions.js](https://github.com/UWCoffeeNCode/Lessons/blob/master/F19/Projects/CanadaU/lesson3/Solutions.js). Try to work together or ask for help if you're stuck.

Good luck!

# Lesson 4 - Tying Everything Together

### [Project](https://github.com/MichaelAEden/DashForReddit) (in progress)
### [Slack](https://bit.ly/uwcoffeencodeslack), channel is `#canada-u`
### [Slides](https://docs.google.com/presentation/d/1-DdqoydWwNtKKIsBip5cmHlWzHwYvevnvltb4KWyGXw/edit?usp=sharing)

### Objectives:

1. Build and minify React application, and serve from back end
1. Use JSON to send data from our back end to our front end
1. Use asynchronous programming to send requests from our front end to our back end

## Getting Started

<b>Note</b> some solutions are in the [python](https://github.com/UWCoffeeNCode/Lessons/blob/master/F19/Projects/CanadaU/lesson4/python) and [react](https://github.com/UWCoffeeNCode/Lessons/blob/master/F19/Projects/CanadaU/lesson4/react) folder. Try to work together or ask for help if you're stuck.

1. Go to the project folder `CanadaU` (or create a new one if you missed the last workshop).
1. From your terminal, navigate to this `CanadaU` folder.
  - <b>Windows</b>: right-click inside folder, select <i>Open Git Bash Terminal Here</i>.
  - <b>Mac</b>: open terminal, write `cd `, then drag folder into terminal.
<br>

## React Build

When you navigate to a webpage, front-end files (JavaScript, HTML, CSS files) are <b>sent to your computer</b> and displayed through the browser.
<br>
CanadaU is no different. Our React application will need to somehow be sent to users of our website.
<br>
This can be achieved by <b>building and minifying</b> our React application.
<br>
<br>
<b>Building</b> is the process of converting (compiling) our React code into a format that browsers can understand.
<br>
<b>Minifying</b> is the process of making the resulting files as small as possible.
<br>
<br>
To build (and minify) our React app:
1. From the terminal, navigate to the `react` folder (`cd ./react`)
2. Run the build script: `npm run build`. This should create and populate a new `build` folder.

<b>Note</b>: `npm` is the Node Package Manager. It manages all the external packages we need for our React application.


## Sending Front-End Resources from the Back End

Now that we have the front-end built and minified, we need to send these resources to the client (user) from our back end.

We will make changes to the Python file we created in Workshop 2.

1. Tell Flask where to obtain the front-end files.

  <b>OLD</b>:
  ```python
  app = Flask(__name__)
  ```
  <b>NEW</b>:
  ```python
  app = Flask(__name__, static_folder='../react-app/build')
  ```

2. Create an <b>endpoint</b> which sends front-end files to the client.

  ```python
  @app.route('/', defaults={'path': ''})
  @app.route('/<path:path>')
  def serve(path):
      if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
          return send_from_directory(app.static_folder, path)
      else:
          return send_from_directory(app.static_folder, 'index.html')
  ```

3. Test our changes by running our Flask app. From your terminal, navigate to the `CanadaU/python` folder and run:

  ```bash
  env FLASK_APP=app.py FLASK_DEBUG=1 flask run
  ```
  then go to <http://localhost:5000>. You should now see you're React app!


## JSON and JavaScript Objects

Recall that our front-end is written in JavaScript using the React framework.
<br>
<br>
Almost everything in JavaScript is what's called an <b>Object</b>&mdash;a set of <b>named values</b>.
<br>
For example, an object which represents the `uWaterloo` subreddit looks like:
```javascript
{
  display_name: 'uwaterloo',
  subscribers: 45678
}
```

Note that objects can <b>nest</b> (contain) other objects. For example:
```javascript
{
  display_name: 'uwaterloo',
  subscribers: 45678,
  icon: 'https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png'
  wordCounts: {
    midterm: 100,
    goose: 34
    // ...
  }
}
```

If you've used Python dictionaries before, JavaScript objects are very similar.
<br>
<br>
<b>JavaScript Object Notation (JSON)</b> is a format used for transferring data.
<br>
It is <b>very similar</b> to JavaScript objects in its notation.
<br>
For example, if our back end needs to send a subreddit to our front end, it will convert the subreddit to JSON before sending it:

```json
{
  "display_name": "uwaterloo",
  "subscribers": 45678,
  "icon": "https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png",
  "wordCounts": {
    "midterm": 100,
    "goose": 34,
  }
}
```
<br>

<b>Challenge</b>: create an endpoint which returns <b>all data about all subreddits</b> as shown below:

```json
{
  "uwaterloo": {
    "display_name": "uwaterloo",
    "subscribers": 45678,
    "icon": "https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png",
  },
  "UofT": {
    "display_name": "uwaterloo",
    "subscribers": 45678,
    "icon": "https://a.thumbs.redditmedia.com/c1iqtotu4lNlCxkJBex6SEtlikJBqt6WmKBNgMQKjS0.png",
  }
}
```

<br>
Base your endpoint off the ones we created during Workshop 2.
<br>
<br>
<b>Hint</b>: to send JSON from the back-end, use Python dictionaries. Python dictionaries are very similar in notation to JSON. For example:

```python
{ 
    'displayName': subreddit.display_name,
    # ...
},
```

## Asynchronous Requests

Generally, a given program will run instructions in order, one at a time.
<br>
If one instruction takes a long time, the entire program will stop and wait until the instruction is finished.
<br>
<br>
Sending a request from the front end to the back end can take a long time (up to a few seconds).
<br>
In our React app, if we sent a request and simply waited on the response, our application would halt for a few seconds.
<br>
In that time, the user-interface would freeze up.
<br>
To avoid this, we use <b>Asynchronous</b> programming.
<br>
<br>
<b>Asynchronous</b> programming allows us to execute slow tasks in the background while the rest of our program continues to run.
<br>
In JavaScript, we use `async`/`await` keywords to perform tasks asynchronously (in the background).

<b>Without Asynchronous Programming</b>
```javascript
function doSomething() {
  // This will take a long time...
  sendRequestToBackend();
  // If the user tries to interact with the UI, nothing will happen until the back end responds.
}
```

<b>With Asynchronous Programming</b>
```javascript
async function doSomething() {
  // This will run in the background
  await sendRequestToBackend();
  // Now the user can interact with the UI!
}
```

<b>To Learn More</b>: read [this guide](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Concepts).
<br>
<br>
To communicate with our back end asynchronously, we'll use the `fetch` function.
<br>
For example, to fetch a subreddit from our backend:
<br>
  1. Create an asynchronous function.
  ```javascript
  async function fetchSubreddits(subredditId) {
      // ...
  }
  ```
  1. Call `fetch` with our URL.
  ```javascript
  async function fetchSubreddits(subredditId) {
      const response = await fetch(`/subreddit/${subredditId}`);
      // ...
  }
  ```
  1. Check if the response was successful. If it was, extract the JSON.
  ```javascript
  async function fetchSubreddits(subredditId) {
      const response = await fetch(`/subreddit/${subredditId}`);
      if (response.ok) {
        const json = await response.json();
        // ... do something with json ...
      }
  }
  ```

<b>Note</b>: `response.json()` is also asynchronous because extracting JSON can be a slow, expensive task.
<br>
<br>
<b>To Learn More About Fetching</b>: read [the docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API).


## Using Asynchronous Requests with React Component State.

Once we've sent a request and gotten the response, we'll want to present the data to the user.
<br>
To do this, we must store the response in the React <b>component state</b>.
<br>
<br>
<b>Component State</b>: stores data which is <b>dynamic</b> (not constant).
<br>
For example, a React toggle switch will use <b>state</b> which keeps track of whether the toggle is on or off.
<br>
<br>
Once we've sent the asynchronous request, we'll need to update the component state. For this, we use the `useState` function.

1. Initialize state to be an empty object (when the component is first loaded, it won't have any data about our subreddits until the request is completed).
  ```javascript
  import React, { useState } from 'react';

  // ...

  function App(props) {
    const [subreddits, setSubreddits] = useState({});
  }
  ```

2. Fetch subreddits from the back end, and update the state accordingly.
  ```javascript
  import React, { useState } from 'react';

  // ...

  function App(props) {
    const [subreddits, setSubreddits] = useState({});

    // ...

    async function fetchSubreddits() {
      const response = await fetch(`/subreddits`);
      // Check if request was successful
      if (response.ok) {
        const json = await response.json();
        // Response JSON has format: { 'uwaterloo': { ... }, 'UofT': { ... }, ... }
        // Update the component state
        setSubreddits(json);
      }
    }
  }
  ```

<b>Challenge</b>: try to implement the above, and test it out with the endpoint you created earlier to fetch <b>all subreddits</b>.
<br>
<b>Challenge</b>: implement the word cloud component using the word count endpoint created in Workshop 2.

If you get stuck, feel free to ask me for help!

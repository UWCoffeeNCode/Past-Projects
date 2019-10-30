# Lesson 2 - Creating Back End with Python and Flask

### [Project](https://github.com/MichaelAEden/DashForReddit) (in progress)
### [Slack](https://bit.ly/uwcoffeencodeslack), channel is `#canada-u`
### [Slides](https://docs.google.com/presentation/d/18-MUzNydWRpT18ApmdO-NtWpsA37nJWxK2VkwJjHj90/edit?usp=sharing)

### Objectives:

1. Create a working server with Flask
2. Learn how to create an endpoint
3. Add error handling
4. Create your own endpoints
<br>

## Flask

<b>[Flask](https://flask.palletsprojects.com/en/1.1.x/)</b> - a web application framework.
<br>

We'll use Flask for our project <b>back end</b>.
<br>
Eventually, it will be used to provide data to our front end.

<b>Getting Started</b>

1. Create a project directory (aka folder), called `CanadaU`. Make a folder inside called `python`, for all our Python code.
1. Create a file `app.py` (remember `.py` is the extension for Python files). Copy the code from `starter_code.py`.
1. Start the Flask back-end server from the terminal. We use `FLASK_DEBUG=1` so the server automatically updates when we make changes to the code.
```bash
env FLASK_APP=<path to Python file> FLASK_DEBUG=1 flask run
```
1. Go to <http://localhost:5000/>, and you should see the description for the UWaterloo subreddit!
<br>

<b>Note</b>: `localhost` just means "this computer", and `5000` is the port we're using.

## Creating New Endpoints with Flask

<b>Endpoint</b> - URL for clients to access a certain resource.
<br>
<b>Resource</b> - data which represents something.

For example, we can create an <b>endpoint</b> at the URL `canadau.ca/subreddits/uwaterloo`.
<br>
Then if we go to this link, we'll get back a <b>resource</b> which represents the UWaterloo subreddit.

For example, let's create an endpoint to get the description of any subreddit.

```python
# When we make a new endpoint, we leave the domain out of the path.
# E.g., instead of canadau.ca/uwaterloo, we just use /uwaterloo
@app.route('/uwaterloo')
def uwaterloo():
    return reddit.subreddit('uwaterloo').description_html
```

Try going to <http://localhost:5000/uwaterloo> to test our new endpoint.

To make this work for other subreddits too, we use <b>path parameters</b>.

```python
# Use '<>' so the client can see the description of any subreddit.
@app.route('/subreddit/<subreddit_id>')
# This function has a new parameter subreddit_id!
def subreddit(subreddit_id):
    return reddit.subreddit(subreddit_id).description_html
```

Try going to <http://localhost:5000/subreddit/uwaterloo> or <http://localhost:5000/subreddit/UofT>!

## Improving Our Endpoint

What happens if we try to get the description of a subreddit which doesn't exist?

Try going to <http://localhost:5000/subreddit/totallynotafakesubreddit>. We get an error.

We should try to handle this case better.

```python
@app.route('/subreddit/<subreddit_id>')
def subreddit(subreddit_id):
    try:
    	# Try to find the subreddit.
    	description = reddit.subreddit(subreddit_id).description_html
        return (description, 200)
    except prawcore.exceptions.Redirect:
    	# If the subreddit can't be found, return an error message and error code.
        return ("Subreddit not found", 404)
```

<!-- NOTE: some people may not be familiar with try-catch statements. -->
If we find the subreddit, return the subreddit description with <b>status code `200` (Success)</b>.
<br>
Otherwise, return an error message and <b>status code `404` (Not Found)</b>.

<b>Side Note on HTTP Status Codes</b>
- Hypertext Transfer Protocol HTTP is the <b>protocol</b> (rules/standards) that we use to communicate with our back end.
- HTTP has a set of status codes to indicate whether a request succeeds or fails.
- E.g., `200` means Success, `401` means Unauthorized, `404` means Not Found
- [All Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Next Steps

Now that you know how to create endpoints, try to create the following endpoints.
We'll need these later in our project.

1. Endpoint which gets the subscriber count of any subreddit.
	- <b>Hint</b>: use the [PRAW docs](https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html)
2. Endpoint which gets the banner image of a subreddit.
	- <b>Hint</b>: instead of `subscribers`, use `banner_img`.
	- <b>Challenge</b>: display the image (use an `<img>` tag)
3. Endpoint which gets the titles of the top 10 posts of a subreddit.
    - <b>Challenge</b>: let the user specify how many posts to fetch.
4. Endpoint which gets the most common words from the top 100 posts of a subreddit.
	- <b>Challenge</b>: use spaCY to filter out certain words.

Some solutions are in `solutions.py`. Try to work together or ask for help if you're stuck.

Good luck!

## Troubleshooting

Getting Error: `ModuleNotFoundError: No module named '<flask OR praw>'`
- Install missing modules with `pip install flask` or `pip install praw`.

Getting Error: `prawcore.exceptions.ResponseException: received 401 HTTP response`
- Fill in `<client_id>`, `client_secret` with your up-to-date credentials.
```
reddit = praw.Reddit(client_id='<client ID>',
                     client_secret='<client secret>',
                     user_agent='web:CanadaU:1.0 (by /u/<reddit username>)')
```


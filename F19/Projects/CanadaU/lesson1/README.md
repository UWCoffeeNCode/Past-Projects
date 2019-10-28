# Lesson 1

### <a href="https://docs.google.com/presentation/d/1tYh3grODsCx6f9ODBeMLiW4j4e4Pk4DUxE7omVHyWYY/edit?usp=sharing">Slides</a>

## Objectives

1. Set up development tools on your computer
1. Learn <i>front end</i> vs <i>back end</i>
1. Learn what an <i>API</i> is
1. Start using the Reddit API
<br>

## Lesson

### 1. Set Up

1. Join the [Coffee N Code Slack](https://bit.ly/uwcoffeencodeslack), then join the `#canada-u` channel for project updates.
1. <b>Windows users</b>: install [Git Bash](https://git-scm.com/downloads) and use this when I say to use a terminal.
1. Install [Python](https://www.python.org/downloads/).
	- <b>Windows users</b>: during installation, <b>select the checkbox to add Python to your PATH!</b>
1. Check Python was installed properly by entering this command in your terminal:
	- <b>Windows</b>: `python -i`
	- <b>Mac</b>: `python3`
	- <b>Troubleshooting for Windows users</b>: did you add Python to your PATH, as in step 3? If not, repeat that step.
1. Install the Python Reddit API Wrapper (PRAW) and Flask by entering these commands in your terminal:
	- <b>Windows</b>: `pip install praw` and `pip install flask`
	- <b>Mac</b>: `pip3 install praw` and `pip3 install flask`
1. Download <a href="https://code.visualstudio.com">VS Code</a> if you don't already have an IDE.
	- <b>Note</b>: an IDE (integrated development environment) is an application that helps you write code.

### 2. Front End vs Back End

Front end and back end are the two parts which make up a web application.

<b>Front End</b>
- What the user sees and interacts with
- Handles presentation of data
- Fetches data from back end
- Updates data in back end

<b>Back End</b>
- Gives data to front end
- Processes data
- May include a database

### 3. Reddit API

An Application Programming Interface (API) is <b>a contract between a client and a server</b>.
<br>
This means the Reddit API will be the set of rules for how we (the <i>clients</i>) talk to Reddit (the <i>server</i>).
<br>
<br>
For example, if we send a request to get top posts from a subreddit, the API says:
- What our request should look like
- What the response (i.e., top posts) will look like

<br>
<b>Start using Reddit's API</b>:

1. Create a Reddit account (even if you already have one)
1. Go to <a href="https://www.reddit.com/prefs/apps">App Preferences</a> and click "Create App"
1. Fill in the fields:
	- <b>Name</b>: CanadaU (or whatever you want it to be)
	- <b>App type</b>: Web App
	- <b>description</b>: (whatever you want)
	- <b>about url</b>: leave this blank
	- <b>redirect url</b>: http://www.example.com/unused/redirect/uri
	and click "Create App"
1. Make note of the client id (random numbers and letters at the top of your created app) and the secret.
1. In Visual Studio Code, create a new Python file `canada_u.py` (`.py` is the file extension for Python files). Add this sample code (fill in your client ID and secret):

```python
import praw

# Create our Reddit client (lets us communicate with Reddit)
reddit = praw.Reddit(client_id='<client id>',
                     client_secret='<secret',
                     user_agent='my user agent')

# Go through the first 10 hot posts in the uwaterloo subreddit
for submission in reddit.subreddit('uwaterloo').hot(limit=10):
    print(submission.title)
```

and run it in your terminal.
<br>
Let me know if you run into any problems!

### 4. Next Steps

I've put a few examples in `praw_examples.py`, including links to the [PRAW documentation](https://praw.readthedocs.io/en/latest/index.html).

Feel free to work in teams or by yourself, and please let me know if you run into any problems or if you do anything really cool.

Good luck!

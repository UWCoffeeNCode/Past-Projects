# Lesson 1

### <a href="https://docs.google.com/presentation/d/1tYh3grODsCx6f9ODBeMLiW4j4e4Pk4DUxE7omVHyWYY/edit?usp=sharing">Slides</a>

## Intro

Hello and welcome to Coffee N Code!
<br>
My name is Michael, and I'll be guiding you through our project <i>CanadaU</i>.
<br>

## Objectives

1. Set up development tools on your computer
1. Learn <i>front end</i> vs <i>back end</i>
1. Learn what an <i>API</i> is
1. Start using the Reddit API
<br>

## Lesson

### 1. Set Up

1. Join the <a href="https://bit.ly/uwcoffeencodeslack">Coffee N Code Slack</a>, and join the `#canada-u` channel
1. Install Bash terminal if needed:
	1. <b>Windows users</b>: install <a href="https://git-scm.com/downloads">Git Bash</a> and use this when I say to use a terminal
	1. <b>Mac users</b>: use the application <b>Terminal</b> when I say to use a terminal
	- <b>Note</b>: a terminal is just a tool which lets you run commands on your computer. If this is your first time using it, don't worry.
1. Install Python <a href="https://www.python.org/downloads/">here</a>
1. Check Python and pip were installed properly by entering this command in your <b>terminal</b>:
	- <b>Windows</b>: `python -i`
	- <b>Mac</b>: `python3`
1. Install the Python Reddit API Wrapper (PRAW) and Flask:
	- <b>Windows</b>: `python -m pip install praw` and `python -m pip install flask`
	- <b>Mac</b>: `pip3 install praw` and `pip3 install flask`
1. Download <a href="https://code.visualstudio.com">VS Code</a> or <a href="https://www.sublimetext.com/3">Sublime</a> (for experienced developers who want something "lighter").
	- This will be your <b>IDE</b> (integrated development environment)
	- It's an application that helps you write code
	- If you're waiting for things to install, customize the settings and make it look pretty!

### 2. Reddit API

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

### 3. Next Steps

Check out the PRAW documentation to see what you can do.

I've put some examples in `praw_examples.py`.

Feel free to work in teams or by yourself, and please let me know if you run into any problems or if you do anything really cool.

Good luck!

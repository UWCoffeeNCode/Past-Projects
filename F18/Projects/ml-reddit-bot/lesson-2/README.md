# Lesson 2: Creating a Reddit Bot
By the end of this lesson, you will have a Python script that lets you get comments from Reddit, and use machine learning on them!

## Resources

- [Python Reddit API Wrapper](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html) (Also known as PRAW)

## Today's Schedule

- Getting a Python script to interact with Reddit

- Using that script to obtain lists of Reddit comments 

- Building a Naive Bayes classifier to distinguish comments from different threads

## Getting a Python script to interact with Reddit

1. Head over to [Reddit](https://www.reddit.com/) and click "SIGN UP" or "LOG IN" if you already have an account you want to use

2. After you are logged in, go to: https://www.reddit.com/prefs/apps. At the bottom, click "are you a developer? create an app..."

3. Name your app whatever you like. **Make sure to select your app as a "script"**. You can leave the description and about-url empty. And finally set the redirect-uri to http://www.example.com/unused/redirect/uri.

4. This should give you a client_id and client_secret. You will need these to have your Python script interact with Reddit. Now go to reddit_script.py in this GitHub folder


## Tasks: 

- Getting comments from 2 different Reddit threads

- Tagging Reddit comments and training a classifer

- Testing how the classifer preformed

See reddit_script.py for how we are going to do these tasks












import praw

# Quick start guide:
# https://praw.readthedocs.io/en/latest/getting_started/quick_start.html



"""
- - - CREATING REDDIT CLIENT - - -
"""

# NOTE: Fill in with your credentials where indicated by the '<>'
reddit = praw.Reddit(client_id='<client ID>',
                     client_secret='<client secret>',
                     user_agent='web:CanadaU:1.0 (by /u/<reddit username>)')



"""
- - - SUBREDDIT OPERATIONS - - -
"""
subreddit = reddit.subreddit("uwaterloo")

print("Subscriber Count: %d" % subreddit.subscribers)

print("Hot")
hot_submissions = subreddit.hot(limit=10)
for submission in hot_submissions:
    print("\t %s" % submission.title)

print("Top of All Time")
top_submissions = subreddit.top('all', limit=10)
for submission in top_submissions:
    print("\t %s" % submission.title)

# For more examples, see:
# https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html



"""
- - - SUBMISSION AND COMMENT OPERATIONS - - -
"""
print("Comments on Top Submission")
top_submissions = subreddit.top('all', limit=10)
top_submission = next(top_submissions)
comments = top_submission.comments
for comment in comments:
    try:
        print("\t %s" % comment.body)
    except AttributeError:
        pass

# For more examples, see:
# https://praw.readthedocs.io/en/latest/code_overview/other/commentforest.html

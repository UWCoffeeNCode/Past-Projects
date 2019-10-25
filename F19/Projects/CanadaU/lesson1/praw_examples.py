import praw

reddit = praw.Reddit(client_id='gkVVyUb93yf45Q',
                     client_secret='r77NHUBX4lkTLQvjqtVUixFTEK8',
                     user_agent='my user agent')

for submission in reddit.subreddit('uwaterloo').hot(limit=10):
    print(submission.title)

canada_universities = [
    "UofT",
    "uwaterloo",
    "uAlberta",
    "UBC",
    # And everyone's favourite
    "nipissingu"
]

for university in canada_universities:
    print("University: %s" % university)
    for submission in reddit.subreddit(university).hot(limit=10):
        print("\t %s" % submission.title)
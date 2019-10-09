# Reddit libaries
import praw

# Machine learning libaries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Initalizing Reddit object which we will use to interact with the site
reddit = praw.Reddit(
    client_id = 'Put your client ID here',  
    client_secret = 'Put your client secret here',
    user_agent = 'reddit_script by /u/spicysideprojects' # Name your user agent whatever you like
)

# If this prints, then you have successfully interacted with Reddit
if reddit.read_only:
    print("Log: Contact with Reddit has been established")
else:
    print("Log: Contact with Reddit has FAILED")

# Gets the top 10 submissions from a subreddit
lp_submission_list = list(reddit.subreddit('learnpython').hot(limit=10)) # You can choose any subreddit you want
print("Log: You have obtained submissions from /r/learnpython")

# Get a submission from /r/learnpython
lp_submission = lp_submission_list[0]
print("Log: Top /r/learnpython submission is '%s'" % lp_submission.title)

# Get the comments from the top submission
lp_comments = lp_submission.comments.list()
print("Log: You have obtained %d comments from /r/learnpython" % len(lp_comments))

# Now let's do the same thing for another subreddit
aww_submission_list = list(reddit.subreddit('aww').hot(limit=10))
print("Log: You have obtained submissions from /r/aww")

aww_submission = aww_submission_list[3]
print("Log: Top /r/aww submission is '%s'" % aww_submission.title)

aww_comments = aww_submission.comments.list()
print("Log: You have obtained %d comments from /r/aww" % len(aww_comments))

# TODO: There is a problem when using 100+ comments as some comments are stored in a MoreComments object
# Put all the comments in a corpus
# Tag the comments:
#   0 = /r/learnpython
#   1 = /r/aww
corpus = [comment.body for comment in (lp_comments[:50] + aww_comments[:50])]
y_train = [0] * len(lp_comments[:50]) + [1] * len(aww_comments[:50])

# Vectorize the corpus
vectorizer = CountVectorizer()
vectorizer.fit(corpus)
x_train = vectorizer.transform(corpus)

# Train the Naive Bayes machine learning model
classifier = MultinomialNB() 
classifier.fit(x_train, y_train)

# Get testing data
test_lp_comments = lp_submission_list[2].comments.list()[:10] 
test_aww_comments = aww_submission_list[4].comments.list()[:10]
test_comments = test_lp_comments + test_aww_comments

# Put testing data in a corpus and tag them
test_corpus = [comment.body for comment in test_comments]
y_test = [0] * len(test_lp_comments) + [1] * len(test_aww_comments)

# Vectorize testing data
x_test = vectorizer.transform(test_corpus)

# Check how the model preformed
print(classifier.predict(x_test))
print(y_test)

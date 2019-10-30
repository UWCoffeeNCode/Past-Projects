import os
from collections import Counter

import praw
import prawcore

from flask import Flask

# Create our Reddit client to communicate with Reddit
# NOTE: Remember to fill in the '<>'!
reddit = praw.Reddit(client_id='<client id>',
                     client_secret='<client secret>',
                     user_agent='web:CanadaU:1.0 (by /u/<reddit username>)')

# Create our Flask application
app = Flask(__name__)

# ENDPOINT 1: subscriber count.

@app.route('/subreddit/<subreddit_id>/subscriberCount')
def subreddit_subscriber_count(subreddit_id):
    try:
        return (reddit.subreddit(subreddit_id).subscribers, 200)
    except prawcore.exceptions.Redirect:
        return ("Couldn't find subreddit.", 404)

# ENDPOINT 2: banner image.

@app.route('/subreddit/<subreddit_id>/banner')
def subreddit_banner_image(subreddit_id):
    try:
        return (reddit.subreddit(subreddit_id).banner_img, 200)
    except prawcore.exceptions.Redirect:
        return ("Couldn't find subreddit.", 404)

# ENDPOINT 3: endpoint to get subreddit top posts.

@app.route('/subreddit/<subreddit_id>/top')
def subreddit_top_posts(subreddit_id):
    subreddit = reddit.subreddit(subreddit_id)
    # Get top 10 posts of all time
    top_posts = subreddit.top('all', limit=10)
    # Get title of each post
    top_posts_titles = [ post.title for post in top_posts ]
    # Return dictionary with response
    return { 'top_posts': list(top_posts_json) }

# ENDPOINT 4: endpoint to get most common words
#
# Before using this endpoint, install spaCy from your terminal:
# pip install spacy
# python -m spacy download en_core_web_sm
#
# Then uncomment these two lines:
# import spacy
# nlp = spacy.load("en_core_web_sm")

@app.route('/subreddit/<subreddit_id>/topWords')
def subreddit_common_words(subreddit_id):
    subreddit = reddit.subreddit(subreddit_id)
    # Get top 10 posts of all time
    top_posts = subreddit.top('month', limit=500)
    # Get title of each post
    top_posts_titles = [ post.title for post in top_posts ]
    top_posts_titles_text = " ".join(top_posts_titles)
    # Filter out irrelevant tokens
    doc = nlp(top_posts_titles_text)
    tokens = [
        token.text.lower() for token in doc
        if not token.is_stop
        and not token.is_punct
        and not token.is_digit
    ]
    word_count = Counter(tokens)
    # Use only words mentioned at least twice
    filtered_word_count = [count for count in word_count.items() if count[1] > 1]
    # Sort words by count
    sorted_word_count = sorted(filtered_word_count, key=lambda item: item[1], reverse=True)
    # Return dictionary with response
    return { 'word_count': sorted_word_count }

if __name__ == "__main__":
    app.run()

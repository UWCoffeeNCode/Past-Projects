import os
from collections import Counter

import praw
import prawcore
import spacy
from flask import Flask, request, send_from_directory

nlp = spacy.load("en_core_web_sm")

# Create our Reddit client to communicate with Reddit
# NOTE: Remember to fill in the '<>'!
reddit = praw.Reddit(client_id='<client id>',
                     client_secret='<client secret>',
                     user_agent='web:CanadaU:1.0 (by /u/<username>)')

# Create our Flask application, and specify where our React app is.
app = Flask(__name__, static_folder='../react/build')


subreddit_ids = [
    'uwaterloo',
    'UofT',
    'UBC',
    'mcgill'
]


def subreddit_exists(subreddit_id):
    try:
        reddit.subreddit(subreddit_id)
        return True
    except prawcore.exceptions.Redirect:
        return False


# - - ENDPOINTS - -


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


# Get all subreddits
@app.route('/subreddits')
def all_subreddits():
    subreddits = {}
    for subreddit_id in subreddit_ids:
        # Ignore case if subreddit does not exist.
        if subreddit_exists(subreddit_id):
            subreddit = reddit.subreddit(subreddit_id)
            subreddits[subreddit_id] = {
                'displayName': subreddit.display_name,
                'subscribers': subreddit.subscribers,
                'icon': subreddit.icon_img
            }
    return (subreddits, 200)


# Subreddit info
@app.route('/subreddit/<subreddit_id>')
def subreddit(subreddit_id):
    if subreddit_exists(subreddit_id):
        subreddit = reddit.subreddit(subreddit_id)
        return (
            { 
                'id': subreddit_id,
                'displayName': subreddit.display_name,
                'subscribers': subreddit.subscribers,
                'icon': subreddit.icon_img
            },
            200
        )
    else:
        return ("Couldn't find subreddit.", 404)


# Most common words
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
    filtered_word_count = [
        { 'text': item[0], 'value': item[1] } for item in word_count.items() if item[1] > 1
    ]
    # Sort words by count
    sorted_word_count = sorted(filtered_word_count, key=lambda item: item['value'], reverse=True)
    # Return dictionary with response
    return ({ 'wordCounts': sorted_word_count }, 200)


if __name__ == "__main__":
    app.run()

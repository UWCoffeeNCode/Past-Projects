import os

import praw
import prawcore
from flask import Flask

# Create our Reddit client to communicate with Reddit
# NOTE: Remember to fill in the '<>'!
reddit = praw.Reddit(client_id='<client ID>',
                     client_secret='<client secret>',
                     user_agent='web:CanadaU:1.0 (by /u/<reddit username>)')

# Create our Flask application
app = Flask(__name__)

# Add an endpoint to our Flask application
@app.route('/')
def serve():
    return reddit.subreddit("uwaterloo").description_html

# - - - WE WILL ADD NEW ENDPOINTS HERE - - -

if __name__ == "__main__":
    app.run()

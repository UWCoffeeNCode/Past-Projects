from flask import Flask, render_template
from flask import request, redirect, url_for
from mongo import Database

OK = "200"
BAD_REQUEST = "400"
SERVER_ERROR = "500"

DATABASE_NAME = "UserGames"
SCORES = "Scores"

app = Flask(__name__)
db = Database(DATABASE_NAME)

@app.route("/")
def index():
    return render_template("archery.html")

@app.route("/score", methods=["GET", "POST"])
def uploadScore():
    if request.method == "POST":
        user_id = "dude"
        score = request.data

        success = db.insert_one(SCORES, {user_id: score})

        return OK if success else SERVER_ERROR

    elif request.method == "GET":
        return redirect(url_for("/score"), code=302)

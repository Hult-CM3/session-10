# a basic flask app
# https://flask.palletsprojects.com/en/stable/

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hult")
def hello_hult():
    return "Hello, Hultians!"

@app.route("/scrabble")
def scrabble():
    return 
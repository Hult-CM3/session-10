from flask import Flask, render_template, request

app = Flask(__name__)

letterscores = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

@app.route("/", methods=["GET", "POST"])
def scrabble():
    if request.method == "POST":
        word = request.form.get('word')
        return scrabble_score(word)
    return render_template("scrabble.html")

def scrabble_score(word):
    word = word.strip().upper()
    score = 0
    for char in word:
        score += letterscores.get(char, 0)
    return str(score)
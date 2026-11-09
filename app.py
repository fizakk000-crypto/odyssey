
from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Game page
@app.route("/game")
def game():
    return render_template("game.html")


# Check the user's answer
@app.route("/check", methods=["POST"])
def check():

    answer = request.form.get("answer")

    if answer == "print":
        result = "Correct! You earned 10 points."
        show = "HURRAI"
    else:
        result = "Wrong answer! Try again."
        show = "Remember Napoleon"
    return render_template("result.html", result=result, show=show)

@app.route("/next_Q2")
def next_Q2():
    return render_template("quest_2.html")


@app.route("/answer_2", methods=["POST"])
def answer_2():
    answer = request.form.get("answer")

    if answer == "4":
        result = "Correct! You earned 10 points."
    else:
        result = "Wrong answer! Try again."

    return render_template("result_2.html", result=result)


@app.route("/next_Q3")
def next_Q3():
    return render_template("quest_3.html")


@app.route("/answer_3", methods=["POST"])
def answer_3():
    answer = request.form.get("answer")

    if answer == "2":
        result = "Correct! You earned 10 points."
    else:
        result = "Wrong answer! Try again."

    return render_template("result_3.html", result=result)


@app.route("/next_Q4")
def next_Q4():
    return render_template("quest_4.html")


@app.route("/answer_4", methods=["POST"])
def answer_4():
    answer = request.form.get("answer")

    if answer == "1200":
        result = "Correct! You earned 10 points."
    else:
        result = "Wrong answer! Try again."
    return render_template("result_4.html", result=result)


@app.route("/next_Q5")
def next_Q5():
    return render_template("quest_5.html")


@app.route("/answer_5", methods=["POST"])
def answer_5():
    answer = request.form.get("answer")

    if answer == "1":
        result = "Correct! You earned total 50 points."
    else:
        result = "Wrong answer! Try again."
    return render_template("result_5.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
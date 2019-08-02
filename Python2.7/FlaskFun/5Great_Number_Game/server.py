from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = "12345678iturytewwarsgfdh"

@app.route("/")
def index():
    if "correct" not in session:
        session["correct"] = random.randint(0,101)
    if "result" not in session:
        result = "nothing"
    else:
        result = session["result"]
    print result
    return render_template("index.html", result=result)

@app.route("/guessnumber", methods=["POST"])
def guess():
    print request.form
    guess = int(request.form["guess"])
    correct = session["correct"]
    if guess > correct:
        session["result"] = "high"
    elif guess < correct:
        session["result"] = "low"
    else:
        session["result"] = "correct"
    return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")
app.run(debug="TRUE")
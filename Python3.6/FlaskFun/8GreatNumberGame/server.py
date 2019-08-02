from flask import Flask, session, render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = "youadsasjdsdgjasj"

@app.route("/")
def index():
    if "number" not in session.keys():
        session['number'] = random.randint(1,101)
        session['phrase'] = "Take a guess!"
        session['color'] = "none"
    if 'guess' in session.keys():
        if session['guess'] > session['number']:
            session['phrase'] = "Too High! Guess a lower number"
            session['color'] = "red"
        elif session['guess'] < session['number']:
            session['phrase'] = "Too Low!! Guess a higher number"
            session['color'] = "red"
        else:
            session['phrase'] = "{} was the number!".format(session['number'])
            session['color'] = "green"
    print (session)

    return render_template('index.html')


@app.route("/guess", methods=["POST"])
def guess():
    session['guess'] = int(request.form["guess"])
    print (session["guess"])
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    print (session)
    return redirect("/")


app.run(debug="TRUE")
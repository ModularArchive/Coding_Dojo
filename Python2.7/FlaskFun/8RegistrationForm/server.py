from flask import Flask, render_template, request, redirect, session
import random,datetime
app = Flask(__name__)
app.secret_key = "              "

@app.route("/")
def index():

    if "gold" not in session:
        session['gold'] = 0
        session['activity'] = []
    print(session.get('activity')) # allows me to view my session to make sure not empty with error

    return render_template("index.html", gold = session.get('gold'))

@app.route("/process_money", methods=["post"])
def process():
    activity = session.get('activity')
    date = datetime.datetime.now().strftime("%Y/%m/%d %X %p")
    print date
    def process_earnings(winnings, location):
        session['gold'] = session.get('gold') + winnings
        activity.append({
            "message": "Earned {} golds from the {}}! ({})".format(winnings, location, date),
        })

    if request.form["building"] == "Farm":
        process_earnings(random.randint(10,20), request.form["building"]) 

    elif request.form["building"] == "Cave":
        process_earnings(random.randint(5,10), request.form["building"]) 

    elif request.form["building"] == "Cave":
        process_earnings(random.randint(5,10), request.form["building"])

    elif request.form["building"] == "Cave":
        game = random.randomint(1,2)
        winnings = random.randomint(0,51)
        if game == 1:
            session['gold'] = session.get('gold') - winnings
            activity.append({
            "message": "Earned {} golds from the {}}! ({})".format(winnings, location, date),
            "color":"red"
        })

@app.route("/refresh", methods=["POST"])
def you_won():

    session.clear()
    return redirect("/")

app.run(debug=True)
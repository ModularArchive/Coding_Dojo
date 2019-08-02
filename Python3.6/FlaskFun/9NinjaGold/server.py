from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime
import os
app = Flask(__name__)
app.secret_key = "It'sFreeRealEstate"

@app.route("/")
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activity'] = []
    print(session.get('activity'))
    return render_template("index.html", gold=session.get('gold'))

@app.route("/process_money", methods=["POST"])
def process_money():
    process = request.form['building']
    earned = 0

    if process == "farm":
        earned += random.randint(10,20)
        print ("earned", earned)
        session['gold'] += earned
        session['activity'].append("Earned {} gold from the {}! ({})".format(earned, process, datetime.now()))

    elif process == "cave":
        earned += random.randint(5,10)
        print ("earned", earned)
        session['gold'] += earned
        session['activity'].append("Earned {} gold from the {}! ({})".format(earned, process, datetime.now()))

    elif process == "house":
        earned += random.randint(2,5)
        print ("earned", earned)
        session['gold'] += earned
        session['activity'].append("Earned {} gold from the {}! ({})".format(earned, process, datetime.now())) #Session append and session gold += earned should be in a more modular format
#EDIT CASINO TO BE SIMPLER
    elif process == "casino":

        if session['gold'] >= 50: #If you have 50 gold or more in session
            earned = random.randint(-50,50)
            print ("earned", earned)

            if earned < 0: # if you earned less than 0 gold

                if session['gold'] - abs(earned) <= 0: #if gold is 0 or less after subtracting
                    session['gold'] = 0                 #then gold = 0
                    session['activity'].append("Entered a casino and lost all of your gold... ({})".format(datetime.now()))

                else:                                                       #else
                    print ("{} - {} > 0".format(session['gold'], earned))   #after losing money you still have gold, print gold
                    session['gold'] += earned
                    session['activity'].append("Entered a casino and lost {} gold... ({})".format(abs(earned), datetime.now()))

            else:
                session['gold'] += earned    #if earned more than 0
                session['activity'].append("Entered a casino and earned {} gold. You got lucky! ({})".format(earned, datetime.now()))

        else:   #else you don't have enough to afford the casino
            gold = session['gold']
            session['gold'] = session['gold']
            session['activity'].append("You need at least 50 gold to go to the casino! ({})".format(datetime.now()))

    return redirect('/')

@app.route("/refresh", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)
from flask import Flask, render_template,request,redirect,session
import random,datetime #Random allows you to do random.randint. datetime module is imported to help create a date time object, connected to my timestamps
app = Flask(__name__)
app.secret_key = "              "

#app.gold = 0


@app.route("/")
def index():
    session.clear() #When at home page, clear session cache so that gold and message is empty
    return render_template("index.html")


@app.route("/process_money", methods=["post"])
def ninja_gold():
    print 'Process Activities...' #note to self to ask am I really in this fuction? am I in this route?
    earn = 0 #this is initializing a variable, earn will probably change in the future but it is good to create it early on and having a starting set value
    msg ='' #Also initializing, eventually this message will be filled in, having variables determined early on is useful
    ts = datetime.datetime.now().strftime("%Y/%m/%d/%I/%M/%p") #This is a chart for time and date following along the if/elif statements
    if request.form['building'] == 'farm': #is the request.form building key equal to the string of farm, if so continue onto the next line 
        print 'Start Farm activity' #if the building key is equal to the string of farm, print Start Farm activity, frequent print statements will help you in debugging
        earn == random.randint(10,20) #this creates a random integer between 10 and 20 to be entered
        print 'earn= ', earn
        msg += 'Earned {} golds from the farm! {} '.format(earn,ts) #In this the they call msg which is an empty string with += and that's where we call the string
        #Earned {} golds from the farm! {} ' with .format(earn,ts)  meaning the earn will go into the first {} and timestamp goes into the second {}

    elif request.form['building'] == 'cave':
        print 'Start Farm activity'
        earn == random.randint(10,20)
        print 'earn = ', earn
        msg += 'Earned {} golds from the cave! {} '.format(earn,ts)

    elif request.form['building'] == 'house':
        print 'Start Farm activity'
        earn == random.randint(10,20)
        print 'earn = ', earn
        msg += 'Earned {} golds from the house! {} '.format(earn,ts)

    elif request.form['building'] == 'casino':
        print 'Start Farm activity'
        earn == random.randint(10,20)
        print 'earn = ', earn
        msg += 'Earned {} golds from the casino! {} '.format(earn,ts)

    try:
        #update gold balance by earn amount
        session['goldbalance'] += earn

    except KeyError: #there was no balance found, start it
        session['goldbalance'] = earn
    
    try:
        # update activity text area by concate msg
        session['activity'] = msg + '\n'
    except KeyError: 
        session['activity'] = msg + '\n'

    return render_template('index.html', goldbalance=session['goldbalance'], activity=session['activity'])
    #Redicted back to...

@app.route("/refresh", methods=["POST"])
def you_won():

    session.clear()
    return redirect("/")

app.run(debug=True)

#UNFINISHED HOWEVER GOT CLOSE AND FIGURED WORTH POSTING/SHARING AND MAYBE FIXING
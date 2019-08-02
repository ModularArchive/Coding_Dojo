from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'SuperSecret'

@app.route('/')
def home():
    if 'count' not in session: #If count hasn't been put into session yet ...   
        session['count'] = 0 #then it will start its count at 0
    session['count'] += 1   
    return render_template('index.html')  

@app.route('/count', methods =['POST'])
def view_count(): 
    try:
        session['count'] = session['count'] + 1 #gives +1 per visit
    except TypeError:
        session['count'] = 1
    return redirect('/')
app.run(debug=True)
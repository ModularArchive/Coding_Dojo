from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'SuperSecret'

@app.route('/')
def home():
    if 'count' not in session: #If there is no count in session 
        session['count'] = 0 #then the session count will begin at 0
    session['count'] += 1       # if count is in session and is higher or equal to 1
    return render_template('index.html')    #Redirect to index.html

@app.route('/count')
def view_count(): 
    try:
        session['count'] = session['count'] + 1 #gives +1 per visit
    except TypeError:
        session['count'] = 1
    return redirect('/')

@app.route('/count/button', methods=['POST'])
def button_count():
    try:
        session['count'] = session['count'] + 1 #gives +1 more per visit
    except TypeError:
        session['count'] = 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset(): 
    session.clear()
    return redirect('/')


app.run(debug=True)


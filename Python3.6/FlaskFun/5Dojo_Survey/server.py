from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "YoMoGuiGwaiFaiDiZao"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST']) #Allowed me to use both GET and POST methods on this page
def process():
    print ("in process route")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('process.html') #This defines session data so you can use it in display

@app.route('/danger')
def danger():
    print ("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

app.run(debug=True)
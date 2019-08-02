from flask import Flask, render_template, request, redirect, session, flash
import re

E_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
N_REGEX = re.compile(r'^[a-zA-Z]+$')
P_REGEX = re.compile(r'(?=.*[A_Z])(?=.*\d).+$')
app = Flask(__name__)
app.secret_key = "YoMoGuiGwaiFaiDiZao"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST']) #Allowed me to use both GET and POST methods on this page
def process():
    print ("in process route")
    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']

    error = False
    if len(session['email']) < 1:
        flash("Please enter an email")
        error = True
    elif not E_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        error = True

    if len(session['first_name']) < 1:
        flash("Please enter a first name")
        error = True
    elif not N_REGEX.match(request.form['first_name']):
        flash("Invalid First Name")
        error = True

    if len(session['last_name']) < 1:
        flash("Please enter a last name")
        error = True
    elif not N_REGEX.match(request.form['last_name']):
        flash("Invalid Last Name")
        error = True

    if len(session['password']) < 1:
        flash("Please enter a password")
        error = True
    elif not P_REGEX.match(request.form['password']):
        flash("Password must contain 1 upper case and 1 numeric value")
        error = True

    if (request.form['password']) != (request.form['conf_pw']):
        flash("Please match both passwords")
        error = True 
    elif not P_REGEX.match(request.form['conf_pw']):
        flash("Password must contain 1 upper case and 1 numeric value")
        error = True

    if error == True:
        return redirect('/')
    else:
        flash("Thanks for submitting your info") #This defines session data so you can use it in display
        return redirect('/')

app.run(debug=True)
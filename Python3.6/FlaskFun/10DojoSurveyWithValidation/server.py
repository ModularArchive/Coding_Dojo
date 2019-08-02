from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "YoMoGuiGwaiFaiDiZao"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST']) #Allows me to use POST methods on this page
def process():
    print ("in process route")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    error = False
    if len(session['name']) < 1:
        flash("Please enter a Name")
        error = True
    if len(session['comment']) < 1:
        flash("Please enter a Comment")
        error = True
    if len(session['comment']) > 120:
        flash("Comments must be under 120 characters")
        error = True
    if error == True:
        return redirect('/')
    else:
        return render_template('process.html') #This defines session data so you can use it in display

@app.route('/danger')
def danger():
    print ("a user tried to visit /danger. we have redirected the user to /")
    return redirect('/')

app.run(debug=True)
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "badoof"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display', methods=['GET', 'POST']) #Allowed me to use both GET and POST methods on this page
def display():
    if request.method == 'POST': #If you follow this line you are using the POST method on the form
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template('display.html', name=name, location=location, language=language, comment=comment) #This defines session data so you can use it in display
    return render_template('index.html') #If you end up on this line it means you used a GET method

app.run(debug=True)


    #"<h2>User info for %s<h2>" % username
#The @ is a decorator which is a way to wrap a function and modify its behavior



#What can happen
#all     name = request.form['name']
    #location = request.form['location']
    #language = request.form['language']
    #comment = request.form['comment']
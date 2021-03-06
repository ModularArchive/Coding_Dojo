from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = "              "

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users", methods = ["POST"])
def create_user():
    print "Got Post Info" #Keys correspond with names
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return redirect('users.html', name=name, location=location, language=language, comment=comment)

@app.route('/show')
def show_user():
    return render_template('users.html')



app.run(debug=True)

#What can happen
#all     name = request.form['name']
    #location = request.form['location']
    #language = request.form['language']
    #comment = request.form['comment']
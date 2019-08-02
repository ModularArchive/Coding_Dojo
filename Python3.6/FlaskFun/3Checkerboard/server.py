from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "              "

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<x>/<y>")
def modular(x,y):
    print (x)
    print (y)
    return render_template("modular.html", value1=int(x), value2=int(y))

#http://localhost:5000 - should display 8 by 8 checkerboard
#http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

app.run(debug="TRUE")
#Was a work in progress, stopped to continue along with the rest of the class on future assignments
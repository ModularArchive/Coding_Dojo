from flask import Flask, render_template,request,redirect,session
import random,datetime #Random allows you to do random.randint. datetime module is imported to help create a date time object, connected to my timestamps
app = Flask(__name__)
app.secret_key = "ASDKJASKDASKBND"

@app.route("/")
def index():
    session.clear() #When at home page, clear session cache so that gold and message is empty
    return render_template("index.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/process", methods=["POST"])
def process():
    session['strawberry'] = request.form['strawberry']
    session['raspberry'] = request.form['raspberry']
    session['apple'] = request.form['apple']
    return redirect("/checkout")
    
app.run(debug=True)
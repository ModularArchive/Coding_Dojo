from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = "It'sFreeRealEstate"

@app.route("/") #This sets the extension the webpage you're defining goes to
def index():    
    return render_template("index.html")#loads the index.html file


@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")


@app.route('/dojos/new')
def dojos():
    return render_template("dojos.html")

#call flask/Scripts/activate

app.run(debug=True)
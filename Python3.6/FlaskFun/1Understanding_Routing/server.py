from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = "It'sFreeRealEstate"

@app.route("/") #This sets the extension the webpage you're defining goes to
def index(): 
    print ("Hello World!")
    return render_template("index.html")#loads the index.html file


@app.route("/dojo")
def dojo():
    print ("dojo!")


@app.route('/say/<message>')
def say(message):
    print (message)
    return render_template("say.html", message=message)

@app.route('/repeat/<number>/<message>')
def repeat(number, message):
    print (number)
    print (message)
    return render_template("modular.html", number=int(number), message=message)


#call flask/Scripts/activate

app.run(debug=True)
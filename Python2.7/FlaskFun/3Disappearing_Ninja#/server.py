from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "              "

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninja():
    return render_template("ninja.html", img_source="")

@app.route('/ninja/<color>', img_source="")
def mycolor(color):
    if color in img_source == blue: #image will equal a different turtle depending on the color
        img_source = 'img/leonardo.jpg'
    elif color in img_source == orange:
        img_source = 'img/michaelangelo.jpg'
    elif color in img_source == red:
        img_source = 'img/raphael.jpg'
    elif color in img_source == "purple":
        img_source = 'img/donatello.jpg'
    else:
        img_source = 'img/notapril.png' #if no turtle april appears
    return render_template("ninja.html")

app.run(debug="TRUE")
#Was a work in progress, stopped to continue along with the rest of the class on future assignments
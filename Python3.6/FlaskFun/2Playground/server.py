from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "badoof"
# http://localhost:5000/play, have it render three beautiful looking blue boxes
# localhost:5000/play/(x), have it display the beautiful looking blue boxes x times
# localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color)
# For example, localhost:5000/play/5/green would display 5 beautiful green boxes.  Calling localhost:5000/play/35/red would display 35 beautiful red boxes.
@app.route('/play') 
def play():
    return render_template('index.html')

@app.route('/play/<x>/<color>') 
def playground(x,color):
    print (x)
    print (color)
    return render_template('modular.html', value1=int(x), col=color)




app.run(debug=True)

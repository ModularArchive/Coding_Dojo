from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our formcopy
@app.route('/')
def index():
  return render_template("index.html")

# the server is listening for a POST request to:
# localhost:5000/users
# we define the route below such that the route matches the action of our form - '/users'
# similarly we need to allow specific methods - 'POST' in this case
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    name = request.form['name']
    email = request.form['email']
    return redirect('/') # redirects back to the '/' route

app.run(debug=True) # run our server
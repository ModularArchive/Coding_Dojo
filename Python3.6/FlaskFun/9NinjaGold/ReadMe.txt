Assignment: Ninja Gold
Objectives:
Practice using session
Practice having the server use data sent by the client in a form
Practice using hidden inputs
Create a simple game to test your understanding of flask, and implement the functionality below.

For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. 
The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or 
LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

Guidelines
Refer to the wireframe below.
Have the four forms appear when the user goes to http://localhost:5000.
For the farm, your form would look something like
<form action="/process_money" method="post">
  <input type="hidden" name="building" value="farm" />
  <input type="submit" value="Find Gold!"/>
</form>
In other words, you want to include a hidden value in the form and have each form submit the form information to /process_money.
Have /process_money determine how much gold the user should have.
You should only have 2 routes -- '/' and '/process_money' (reset can be another route if you implement this feature).



Please make sure that...

when you visit, "localhost:5000/" you are seeing the page we described above (in other words, we don't want to have to go to "/gold/index" or other URL to see this app).
the forms are sent to "/process_money" and not any other URL.
the activities are stored in the session. No need to store anything in the database.
Watch this before you start the assignment

Another Helpful Information
Consider the following code:

server.py

def index():
    message = "<p class='special'>Hello</p>"
    return render_template("index.html", message=message)
templates/index.html

{{ message }}
Jinja by default will convert any html entities with "character entities" (please read https://www.w3schools.com/html/html_entities.asp).  This means that on the browser, you'll actually see the word "<p class='special'>Hello</p>" instead of just the word Hello (similarly <b> would be changed to <b> so that the browser can have it render as "<b>").  To prevent Jinja from converting html entities to "character entities" automatically, do the following instead:

{{ message|safe }}
Please see http://jinja.pocoo.org/docs/2.10/templates/#working-with-automatic-escaping and also https://stackoverflow.com/questions/12341496/jinja-2-safe-keyword.
Assignment: Great Number Game
Objectives:
Practice using session to store data about a client's history with the web app
Practice clearing a session
Practice having the server use data submitted by a client with a form
Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

In order to generate a random number you can use the "random" python module:

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
random.randrange(0, 101) # random number between 0-100
In order to remove something from the session, you must pop() it off of the session dictionary. Alternatively, you may use other built-in dictionary methods, such as clear().

# Set session like so:
session['someKey'] = 50
# Remove something from session like so:
session.pop('someKey')


Note: There are many different ways to do this assignment. When you finish the basic functionality, find a peer and compare your code!
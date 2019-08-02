Assignment: Dojo Survey
Objectives:
Practice creating a server with Flask from scratch
Practice adding routes to a Flask app
Practice having the client send data to the server with a form
Practice having the server render a template using data provided by the client
Practice how to redirect a http request to another url
Build a flask application that accepts a form submission and presents the submitted data on a results page.

The goal is to help you get familiar with sending POST requests through a form and displaying that information. Consider the below example as a guide.



When you build this, please make sure that your program meets the following criteria:

http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
http://localhost:5000/result - have this display a html with the information that was submitted by POST
http://localhost:5000/danger - have this redirect back to "/".  Before redirecting back print in the terminal/console a message: "a user tried to visit /danger.  we have redirected the user to /".
Reminders
Please remember that anything you want to submit by a form needs to have a name and value (even <select> and <textarea>.  For example, the following html form would not submit any information by post!

Wrong way
<form action='result' method='post'>
    <h2>Buy apples</h2>
    Quantity: 
    <select>
         <option>1</option>
         <option>2</option>
    </select>
    Message: <textarea></textarea>
    <input type='checkbox'> Want extra large apples?
    <p>Please select your preferred contact method:</p>
    <input type='radio'>Email
    <input type='radio'>Phone
</form>
The reason above would not submit any information via POST is because select, textarea and input are all missing names and values.  

Right Way!
To make this work where the form actually submits the information you want, you need something like this:

<form action='result' method='post'>
    <h2>Buy apples</h2>
    Quantity: 
    <select name='quantity'>
         <option value='1'>1</option>
         <option value='2'>2</option>
    </select>
    Message: <textarea name='message'></textarea>
    <input type='checkbox' name='extra_large' value='yes'> Want extra large apples?
    <p>Please select your preferred contact method:</p>
    <input type='radio' name='contact' value='email'>Email
    <input type='radio' name='contact' value='phone'>Phone
    <input type='submit' value='Submit'>
</form>
It's always a good idea to print request.form to see if the form is delivering all the information you need in your routing method.
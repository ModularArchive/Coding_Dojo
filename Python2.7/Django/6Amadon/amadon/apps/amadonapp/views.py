from django.shortcuts import render

# You cant have a method in the view file handle POST data and rendering HTML at the same time
# If anything you have a methor view handle the POST data, then redirect to another view method that can render the html

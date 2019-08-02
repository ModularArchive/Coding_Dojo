Assignment: Time Display
Objectives:
Practice setting up a Django project
Familiarity with passing data to a template
Create a Django app called time_display according to the below wireframe.

alt text

In the controller of your app called time_display - the file ...apps/time_display/views.py) - create a method named index.

When you go to the URL localhost:8000 or localhost:8000/time_display/ this should run the index() method in your controller file, (views.py). Have that method render a template that displays the current date and time.

from django.shortcuts import render, HttpResponse, redirect
def yourMethodFromUrls(request):
    context = {
        "somekey":"somevalue"
    }
    return render(request,'appname/page.html', context)
The keys of your context dictionary are available to be accessed on your page.html.

<p>{{somekey}}</p>
The above line will print out “somevalue” on your HTML!

There are many ways to get the current time in Python. For example, you could have views.py import gmtime, strftime from 'time' and pass the appropriate string to the render method. For example, your views.py could look like:

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'appname/index.html', context)
To learn more about strftime, see https://docs.python.org/3.3/library/time.html?highlight=time.strftime#time.strftime

Please also see https://stackoverflow.com/questions/466345/converting-string-into-datetime

Recognize that working with time - especially timezones - is among the more frustrating parts of computer programming. Do not spend more than 15 minutes exploring timezones. We will have numerous opportunities to discuss the challenges of timezones. Essentially, we want to store any timestamps in our database in UTC, and eventually use JavaScript to get the time from the user's browser to customize how times are displayed. For now, the easy fix is to set your Django settings to the timezone that works for you and move on. You have more important things to cover at this part of your career as a developer than timezones.
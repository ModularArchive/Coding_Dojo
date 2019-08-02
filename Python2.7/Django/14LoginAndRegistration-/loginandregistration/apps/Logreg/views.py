from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User
from datetime import datetime
import bcrypt

def index(request):
    return render(request, 'Logreg/index.html')
def register(request):
    errors = User.objects.validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash)
        request.session['first_name'] = request.POST['first_name']
        return redirect('/success')

def signin(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
        return redirect('/success')

def success(request):
    return render(request, 'Logreg/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')

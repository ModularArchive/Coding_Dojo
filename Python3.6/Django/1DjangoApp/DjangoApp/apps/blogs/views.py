from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    return render(request, 'blogs/index.html')

def new(request):
    return render(request, 'blogs/new.html')

def create(request):
    return redirect('/')

def show(request, number):
    print (number)
    print ("placeholder to display blog {}").format(number)
    return render(request, 'blogs/edit.html', number)

def edit(request, number):
    print (number)
    print ("placeholder to edit blog {}").format(number)
    return render(request, 'blogs/edit.html', number)

def delete(request, number):
    print (number)
    return redirect('/')

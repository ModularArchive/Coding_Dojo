from django.shortcuts import render, HttpResponse, redirect

from .models import *

# Create your views here.
def index(request):
    return redirect('/users')
    
def users(request):
    context = {
        'user': User.objects.all()
    }
    print (context)
    return render(request, 'semirestfulusers/index.html', context)

def new(request):
    return render(request, 'semirestfulusers/new.html')

def create(request):
    User.objects.create(name=request.POST['name'], email=request.POST['email'])
    return redirect('/users')

def show(request, number):
    if request.method == "POST":
        user = User.objects.get(id=number)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request, 'semirestfulusers/show.html', context)

def edit(request, number):
    print (number)
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request, 'semirestfulusers/edit.html', context)

def destroy(request, number):
    print (number)
    User.objects.get(id=number).delete()
    return redirect('/users')
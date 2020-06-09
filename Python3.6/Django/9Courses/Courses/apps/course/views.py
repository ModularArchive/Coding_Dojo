from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
import bcrypt, re

def index(request):
    return redirect('/course')
    
def course(request):
    context = {
        'course': Course.objects.all(),
    }
    return render(request, 'course/index.html', context)

def create(request):
    errors = Appointments.objects.app_val(request.POST)
    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/course')
    else:
        Course.objects.create(course_name=request.POST['course_name'], description=request.POST['description'])
        return redirect('/course')

def conf_destroy(request, number):
    context = {
        'course': Course.objects.get(id=number)
    }
    return render(request, 'Course/destroy.html', context)

def destroy(request, number):
    print (number)
    Course.objects.get(id=number).delete()
    return redirect('/course')
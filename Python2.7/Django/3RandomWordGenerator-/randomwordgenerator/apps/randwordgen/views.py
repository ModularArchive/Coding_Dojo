from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    randstring = {
        "string": get_random_string(length=14),
    }
    if not 'count' in request.session:
        request.session['count'] = 1
    return render(request, 'randwordgen/index.html', randstring)

def counting(request):
    request.session['count'] += 1
    return redirect('/')

def clear(request):
    del request.session['']
    return redirect('/')
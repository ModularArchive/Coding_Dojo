from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'survey/index.html')

def processing(request):
    if request.method =="POST":
        print request.POST
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        reutn redirect('/result')
    else:
        return redirect('/')       

def result(request):
    return render(request, 'survey/result.html')
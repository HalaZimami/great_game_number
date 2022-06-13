from urllib import request
from django.shortcuts import render, HttpResponse, redirect
import random  # import the random module



def index(request):
        if not 'counter' in request.session:
            request.session['counter']=0
        if not 'random' in request.session:
            request.session['random']=random.randint(1, 100)
        if not 'number' in request.session:
            request.session['number']=0
        print(request.session['random'])
        return render(request, 'index.html')

def guess(request):
    if request.method == 'POST':
        request.session['number']=int(request.POST['number'])
        request.session['counter']+=1
    return redirect('/')


def delete(request):
    if "number" in request.session:
        del request.session['number']
    if "random" in request.session:
        del request.session['random']
    if "counter" in request.session:
        del request.session['counter']
    return redirect('/')
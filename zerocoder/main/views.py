from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'caption' : 'Luchik'
    }
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')
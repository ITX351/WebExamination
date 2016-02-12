from django.shortcuts import *


def login(request):
    return render(request, 'mainApp/login.html', {})


def homepage(request):
    return render(request, 'mainApp/index.html', {})

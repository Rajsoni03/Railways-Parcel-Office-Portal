from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    params = {
        'title' : 'Home'
    }
    return render(request, 'Main/index.html', params)

def train(request):
    params = {
        'title' : 'train'
    }
    return render(request, 'Main/train.html', params)

def about(request,no):
    params = {
        'about_page_no': no
    }
    return render(request, 'Main/about.html', params)
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'Main/about.html')
        else:
            messages.info(request, "USERNAME OR PASSWORD DID NOT MATCH !!!")
            return redirect(login)
    else:
        return render(request, "Main/login.html")
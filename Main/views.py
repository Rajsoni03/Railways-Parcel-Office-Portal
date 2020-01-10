from django.shortcuts import render

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
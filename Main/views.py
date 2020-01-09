from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        'title' : 'Home'
    }
    return render(request, 'Main/index.html', params)
from django.shortcuts import render

# Create your views here.
def adminHome(request):
    return render(request, 'Admin/dashboard.html')

def login(request):
    return render(request, 'Admin/login.html')

def parcels(request):
    return render(request, 'Admin/parcels.html')

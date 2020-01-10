from django.shortcuts import render
from Main.models import Train

# Create your views here.
def dashboard(request):
    trains = Train.objects.all()
    params = {
        'trains' : trains
    }
    return render(request, 'Dashboard/dashboard.html', params)

# def adminHome(request):
#     return render(request, 'Admin/dashboard.html')

# def parcels(request):
#     return render(request, 'Admin/parcels.html')

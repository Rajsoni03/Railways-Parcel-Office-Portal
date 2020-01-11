from django.shortcuts import render
from django.contrib.auth.models import auth, User
from Main.models import Station, Train

# Create your views here.
def adminHome(request):
    return render(request, 'Admin/dashboard.html')


def login(request):
    return render(request, 'Admin/login.html')


def parcels(request):
    return render(request, 'Admin/parcels.html')


def pos(request):
    if request.method == 'POST':
        if request.POST.get('submit'):
            submit_id = request.POST.get('submit')
            user = User.objects.filter(id=submit_id)[0]
            if request.POST.get('activebtn', 'off') == 'on':
                user.is_active = True
                user.save()
            if request.POST.get('activebtn', 'off') == 'off':
                user.is_active = False
                user.save()
            if request.POST.get('staffbtn', 'off') == 'on':
                user.is_staff = True
                user.save()
            if request.POST.get('staffbtn', 'off') == 'off':
                user.is_staff = False
                user.save()

        if request.POST.get('delete'):
            delete_id = request.POST.get('delete')
            user = User.objects.filter(id=delete_id)[0]
            user.delete()
            print('DELETE')

    allCustomers = User.objects.filter(is_staff=False)
    station = []
    for i in allCustomers:
        station.append(Station.objects.filter(station_id=i.id)[0])
    print(allCustomers)
    params = {
        'allCustomers': allCustomers,
        'station': station,
    }
    return render(request, 'Admin/customers.html', params)

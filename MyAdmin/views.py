from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.admin.views.decorators import staff_member_required
from Main.models import Station, Train
from MyAdmin.models import TestData
from LiveTracking.models import LiveTracking
from Dashboard.models import Notification


# Create your views here.
@staff_member_required(login_url='/login')
def adminHome(request):
    return render(request, 'MyAdmin/dashboard.html')


@staff_member_required(login_url='/login')
def parcels(request):
    return render(request, 'MyAdmin/parcels.html')


@staff_member_required(login_url='/login')
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
    return render(request, 'MyAdmin/customers.html', params)


@staff_member_required(login_url='/login')
def train(request):
    return render(request, 'MyAdmin/train.html')


@staff_member_required(login_url='/login')
def update(request, id):
    if request.method == 'POST':
        seal_status = True if request.POST.get('seal_status', 'off') == 'on' else False
        LiveTracking(
            train_ID=request.POST['train_ID'],
            lat=request.POST['lat'],
            long=request.POST['long'],
            seal_status=seal_status,
            parcel_status=True if request.POST.get('parcel_status', 'off') == 'on' else False,
        ).save()
        if not seal_status:
            from geopy.geocoders import Nominatim
            from Main.models import Train
            geolocator = Nominatim(user_agent="raj")
            location = geolocator.reverse(f"{request.POST['lat']}, {request.POST['long']}")
            print(location.address)
            Notification(
                train_ID=request.POST['train_ID'],
                train_no=Train.objects.filter(id=request.POST['train_ID'])[0].train_no,
                lat=request.POST['lat'],
                long=request.POST['long'],
                location=location.address,
                seal_status=seal_status,
                parcels=21,
                station1='',
                station2='',
                station3='',
                msg='Seal is Braked'
            ).save()

        return redirect(f'/myAdmin/update/{id + 1}')

    test = TestData.objects.filter(id=id)[0]
    params = {
        'train_ID': test.train_ID,
        'lat': test.lat,
        'long': test.long,
        'check1': 'checked' if test.seal_status == True else '',
        'check2': 'checked' if test.parcel_status == True else '',
        'id': id + 1
    }
    return render(request, 'MyAdmin/update.html', params)

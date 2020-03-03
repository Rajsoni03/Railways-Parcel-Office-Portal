from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from LiveTracking.models import LiveTracking
from Dashboard.models import Notification
from datetime import datetime


# Create your views here.
@staff_member_required(login_url='/login')
def setLocation(request):
    if request.method == 'POST':
        seal_status = True if request.POST.get('seal_status', 'off') == 'on' else False
        LiveTracking(
            train_ID=request.POST['train_ID'],
            lat=request.POST['lat'],
            long=request.POST['long'],
            seal_status=seal_status,
            parcel_status=True if request.POST.get('parcel_status', 'off') == 'on' else False,
        ).save()
        status = True
        if not seal_status:
            from geopy.geocoders import Nominatim
            from Main.models import Train
            geolocator = Nominatim(user_agent="raj")
            location = geolocator.reverse(f"{request.POST['lat']}, {request.POST['long']}")
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
                msg='Lock is Braked'
            ).save()
            status = False
    return JsonResponse(data={'status': status})


def pi(request):
    status = False
    try:
        train_ID = request.GET.get('train_ID', None)
        lat = request.GET.get('lat', None)
        long = request.GET.get('long', None)
        seal_status = request.GET.get('seal_status', None)
        parcel_status = request.GET.get('parcel_status', None)
        rfid = request.GET.get('rfid', None)
        date = datetime.now()
        status = True
    except:
        status = False
    print(rfid)
    data = {
        'train_ID': train_ID,
        'lat': lat,
        'long': long,
        'seal_status': seal_status,
        'parcel_status': parcel_status,
        'date': date,
        'rfid': rfid,
        'status': status
    }
    return JsonResponse(data=data)

def test(request):
    return render(request, 'Main/base.html')
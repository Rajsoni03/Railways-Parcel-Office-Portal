from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Main.models import Train
from LiveTracking.models import LiveTracking
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from Parcel.models import Parcel
from random import randint
from .models import Notification, Otp
from datetime import datetime


# Create your views here.

@login_required(login_url='/login')
def dashboard(request):
    trains = Train.objects.all()

    def train_pos(request, train_id):
        train = Train.objects.all()[train_id - 1]
        stations = [
            train.station1,
            train.station2,
            train.station3,
            train.station4,
            train.station5,
            train.station6,
            train.station7,
            train.station8,
            train.station9,
            train.station10,
            train.station11,
            train.station12,
            train.station13,
            train.station14,
            train.station15,
            train.station16,
            train.station17,
            train.station18,
            train.station19,
            train.station20,
        ]
        for i in stations:
            try:
                stations.remove('0')
            except:
                pass
        return 100 * stations.index(train.train_live_station) / len(stations)

    train_range = []
    for i in trains:
        train_range.append(train_pos(request, train_id=i.id))
    params = {
        'trains': trains,
        'train_range': train_range,
        'noOfParcelSend': len(Parcel.objects.filter(parcel_from=request.user.first_name)),
        'noOfParcelRecieve': len(Parcel.objects.filter(parcel_to=request.user.first_name)),
        'noOfTrain': len(Train.objects.all()),
        'noOfNoti': len(Notification.objects.all()),
    }
    return render(request, 'Dashboard/dashboard.html', params)


@login_required(login_url='/login')
def train(request):
    params = {
        'title': 'train'
    }
    return render(request, 'Main/train.html', params)


@login_required(login_url='/login')
def track(request):
    if request.method == 'POST':
        train = Train.objects.filter(id=request.POST['train_id'])[0]
        stations = [
            train.station1,
            train.station2,
            train.station3,
            train.station4,
            train.station5,
            train.station6,
            train.station7,
            train.station8,
            train.station9,
            train.station10,
            train.station11,
            train.station12,
            train.station13,
            train.station14,
            train.station15,
            train.station16,
            train.station17,
            train.station18,
            train.station19,
            train.station20,
        ]
        for i in stations:
            try:
                stations.remove('0')
            except:
                pass

        # geolocator = Nominatim(user_agent="raj")

        liveTracking = LiveTracking.objects.filter(train_ID=request.POST['train_id'], parcel_status=True)

        list_of_green_test = []
        list_of_red_test = []

        sealStatus = True
        flug = True

        for i in liveTracking:
            if i.seal_status == True:
                if flug == False:
                    list_of_red_test.append([float(i.long), float(i.lat)])
                    flug = True
                list_of_green_test.append([float(i.long), float(i.lat)])
                sealStatus = True

            if i.seal_status == False:
                list_of_green_test.append([float(i.long), float(i.lat)])
                flug = False
                list_of_red_test.append([float(i.long), float(i.lat)])
                sealStatus = False

        all_point = list_of_green_test

        if len(all_point) == 1:
            center_point = all_point[0]
        else:
            center_point = all_point[int(len(all_point) / 2)]

        # print(center_point)

        x = [all_point[0][1], all_point[0][0]]
        y = [all_point[-1][1], all_point[-1][0]]
        distance = geodesic(x, y).km

        if distance < 2:
            map_zoom = 15
        elif distance < 4:
            map_zoom = 14
        elif distance < 8:
            map_zoom = 13
        elif distance < 16:
            map_zoom = 12
        elif distance < 32:
            map_zoom = 11
        elif distance < 64:
            map_zoom = 10
        elif distance < 128:
            map_zoom = 9
        elif distance < 256:
            map_zoom = 7
        elif distance < 512:
            map_zoom = 6
        elif distance < 1024:
            map_zoom = 5

        print(sealStatus)

        params = {
            'first_point': all_point[-1],
            'center_point': center_point,
            'map_zoom': map_zoom,
            'list_of_red': list_of_red_test,
            'list_of_green': list_of_green_test,
            'train': train,
            'seal_status': sealStatus,
            'trains': Train.objects.filter(id=request.POST['train_id'])[0],
            # 'live_station' : Train.objects.filter(id = request.POST['train_id']),
            'stations': stations
        }
        return render(request, 'Dashboard/track.html', params)
    return render(request, 'Dashboard/track.html')


def parcel_send(request):
    if request.method == 'POST':
        Parcel(phone=request.POST['phone'],
               rfid=request.POST['rfid'],
               train_id=request.POST['train_id'],
               sender_name=request.POST['sender_name'],
               sender_adhar=request.POST['reciever_adhar'],
               reciever_name=request.POST['reciever_name'],
               reciever_adhar=request.POST['reciever_adhar'],
               parcel_from=request.POST['parcel_from'],
               parcel_to=request.POST['parcel_to'],
               parcel_info=request.POST['parcel_info'],
               status='Pending',
               parcel_id=f'PR{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}',
               ).save()
        return redirect('/dashboard/recieve')
    params = {
        'train': Train.objects.all()
    }
    return render(request, 'Dashboard/parcel_send.html', params)


def parcel_recieve(request):
    params = {
        'parcels': Parcel.objects.filter(parcel_to=request.user.first_name)
    }
    return render(request, 'Dashboard/parcel_recieve.html', params)


def parcel(request, id):
    model = False
    error = False
    otpError = False
    parcel = Parcel.objects.filter(id=id)[0]
    if request.method == 'POST':
        if 'sendotp' in request.POST:
            if request.POST.get('parcel_id', None) == parcel.parcel_id and request.POST.get('reciever_adhar',
                                                                                            None) == parcel.reciever_adhar:
                if Otp.objects.filter(parcel_id=id).exists():
                    obj = Otp.objects.filter(parcel_id=id)[0]
                    obj.otp = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
                    obj.date = datetime.now()
                    obj.save()
                else:
                    Otp(parcel_id=id,
                        otp=f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}',
                        date=datetime.now()).save()

                model = True
            else:
                error = True
        if 'verify' in request.POST:
            otp = Otp.objects.filter(parcel_id=id)[0]
            print(request.POST['OTP'], otp.otp)
            if request.POST['OTP'] == otp.otp:
                print(request.POST['OTP'])
                parcel.status = 'Delivered'
                parcel.done_date = datetime.now()
                parcel.save()
            else:
                model = True
                otpError = True
        if 'resend' in request.POST:
            obj = Otp.objects.filter(parcel_id=id)[0]
            obj.otp = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
            obj.date = datetime.now()
            obj.save()
            model = True

    params = {
        'parcel': parcel,
        'model': model,
        'error': error,
        'otpError': otpError,
        'status': True if (parcel.status == "Pending") else False,
        'sender_adhar': parcel.sender_adhar[8:],
        'reciever_adhar': parcel.reciever_adhar[8:]
    }
    return render(request, 'Dashboard/parcel.html', params)


def train(request):
    return render(request, 'Dashboard/train.html')


def noti(request):
    params = {
        'notification': Notification.objects.all()
    }
    return render(request, 'Dashboard/noti.html', params)

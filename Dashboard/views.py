from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Main.models import Train
from LiveTracking.models import LiveTracking
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from Parcel.models import Parcel
from random import randint
from .models import Notification
# Create your views here.

@login_required(login_url='/login')
def dashboard(request):
    trains = Train.objects.all()

    def train_pos(request, train_id):
        train = Train.objects.all()[train_id-1]
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
        return 100 * stations.index(train.train_live_station)/len(stations)

    train_range = []
    for i in trains:
        train_range.append(train_pos(request,train_id=i.id))

    params = {
        'trains' : trains,
        'train_range' : train_range,
        'noOfParcelSend' : len(Parcel.objects.all()),
        'noOfParcelRecieve' : len(Parcel.objects.all()),
        'noOfTrain' : len(Train.objects.all()),
        'noOfNoti' : len(Notification.objects.all()),
    }
    return render(request, 'Dashboard/dashboard.html', params)

@login_required(login_url='/login')
def train(request):
    params = {
        'title' : 'train'
    }
    return render(request, 'Main/train.html', params)

@login_required(login_url='/login')
def track(request):
    if request.method == 'POST':
        train = Train.objects.filter(id = request.POST['train_id'])[0]
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

        liveTracking = LiveTracking.objects.filter(train_ID=request.POST['train_id'], parcel_status = True)

        list_of_green_test = []
        list_of_red_test = []

        sealStatus = True
        flug = True

        for i in liveTracking:
            if i.seal_status == True:
                if flug == False:
                    list_of_red_test.append([float(i.long), float(i.lat)])
                    flug = True
                list_of_green_test.append([float(i.long),float(i.lat)])
                sealStatus = True

            if i.seal_status == False:
                list_of_green_test.append([float(i.long), float(i.lat)])
                flug = False
                list_of_red_test.append([float(i.long),float(i.lat)])
                sealStatus = False
        #
        # print(list_of_green_test)
        # print(list_of_red_test)
        #
        # list_of_green =   [ [-122.48605459928514, 37.82786596829394],
        #                     [-122.48595803976059, 37.82788927246246],
        #                     [-122.4859634041786, 37.82788503534145],
        #                     [-122.48582661151886, 37.82797825194729],
        #                     [-122.4858346581459, 37.82797189627337],
        #                     [-122.48570591211319, 37.82809689109353],
        #                     [-122.48571664094925, 37.82808206121068],
        #                     [-122.48543500900269, 37.82860534241688],
        #                     [-122.4854403734207, 37.828594749716714],
        #                     [-122.48519897460936, 37.82905870855876],
        #                     [-122.48520433902739, 37.82905870855876],
        #                     [-122.48509168624878, 37.82920912381288]
        #                 ]
        #
        # list_of_red = [
        #                     [-122.48509168624878, 37.82920912381288],
        #                     [-122.48509705066681, 37.82920488676767],
        #                     [-122.48492807149889, 37.82930022022615],
        #                     [-122.4849334359169, 37.829298101706186],
        #                     [-122.48474299907684, 37.829331998018276],
        #                     [-122.4847564101219, 37.82932776098012],
        #                     [-122.48458743095398, 37.8293447091313],
        #                     [-122.48459815979002, 37.8293425906126],
        #                     [-122.48422533273697, 37.829361657278575],
        #                     [-122.48423874378203, 37.829357420242125],
        #                     [-122.48395174741744, 37.829412501697064],
        #                     [-122.48395174741744, 37.82940826466351],
        #                     [-122.48393028974533, 37.829471820141016]
        #                 ]

        all_point = list_of_green_test

        if len(all_point) == 1:
            center_point = all_point[0]
        else:
            center_point = all_point[int(len(all_point)/2)]

        # print(center_point)

        x  = [all_point[0][1], all_point[0][0]]
        y = [all_point[-1][1],all_point[-1][0]]
        distance = geodesic(x,y).km

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
            'first_point' : all_point[-1],
            'center_point': center_point,
            'map_zoom' : map_zoom,
            'list_of_red' : list_of_red_test,
            'list_of_green' : list_of_green_test,
            'train' : train,
            'seal_status' : sealStatus,
            'trains' : Train.objects.filter(id = request.POST['train_id'])[0],
            # 'live_station' : Train.objects.filter(id = request.POST['train_id']),
            'stations' : stations
        }
        return render(request, 'Dashboard/track.html', params)
    return render(request, 'Dashboard/track.html')

def parcel_send(request):
    if request.method == 'POST':
        Parcel( phone = request.POST['phone'],
                rfid = request.POST['rfid'],
                train_id = request.POST['train_id'],
                sender_name = request.POST['sender_name'],
                sender_adhar = request.POST['reciever_adhar'],
                reciever_name = request.POST['reciever_name'],
                reciever_adhar = request.POST['reciever_adhar'],
                parcel_from = request.POST['parcel_from'],
                parcel_to = request.POST['parcel_to'],
                parcel_info = request.POST['parcel_info'],
                status = 'Pending',
                parcel_id = f'PR{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}',
        ).save()
        return redirect('/dashboard/recieve')
    params = {
        'train' :  Train.objects.all()
    }
    return render(request, 'Dashboard/parcel_send.html', params)

def parcel_recieve(request):
    params = {
        'parcels' : Parcel.objects.all()
    }
    return render(request, 'Dashboard/parcel_recieve.html',params)

def parcel(request,id):
    model = False
    error = False
    parcel = Parcel.objects.filter(id=id)[0]
    if request.method == 'POST':
        if 'sendotp' in  request.POST:
            if request.POST.get('parcel_id',None) == parcel.parcel_id and request.POST.get('reciever_adhar',None) == parcel.reciever_adhar:
                model = True
            else:
                error = True
        if 'verify' in  request.POST:
            print(request.POST['OTP'])
            parcel.status = 'Delivered'
            parcel.save()
        if 'resend' in  request.POST:
            model = True

    params = {
        'parcel' : parcel,
        'model' : model,
        'error' : error
    }
    return render(request, 'Dashboard/parcel.html',params)

def train(request):
    return render(request, 'Dashboard/train.html')

def noti(request):
    params = {
        'notification': Notification.objects.all()
    }
    return render(request, 'Dashboard/noti.html', params)

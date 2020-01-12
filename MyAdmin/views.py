from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.admin.views.decorators import staff_member_required
from Main.models import Station, Train
from django.contrib import messages


# Create your views here.
@staff_member_required(login_url='/myAdmin/login')
def adminHome(request):
    return render(request, 'MyAdmin/dashboard.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        staff = auth.authenticate(username=email, password=password)
        print(staff)
        if staff is not None:
            print('ndekn')
            if staff.is_staff:
                auth.login(request, staff)
                return redirect('/myAdmin')
            else:
                messages.info(request, 'Please Enter Staff Email')
                return redirect('/myAdmin/login')
        else:
            messages.info(request, 'Email Does Not Exists')
            return redirect('/myAdmin/login')
    params = {
        'active': 'login',
    }
    return render(request, 'MyAdmin/login.html', params)

@staff_member_required(login_url='/myAdmin/login')
def parcels(request):
    return render(request, 'MyAdmin/parcels.html')

@staff_member_required(login_url='/myAdmin/login')
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

@staff_member_required(login_url='/myAdmin/login')
def train(request):
    return render(request, 'MyAdmin/train.html')

@staff_member_required(login_url='/myAdmin/login')
def track(request):
    return render(request, 'MyAdmin/track.html')
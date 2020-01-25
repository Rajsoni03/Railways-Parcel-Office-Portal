from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Station
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    params = {
        'title' : 'Home',
        'heading' : 1
    }
    return render(request, 'Main/index.html', params)

def about(request,no):
    params = {
        'about_page_no': no
    }
    return render(request, 'Main/about.html', params)

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('/myAdmin')
            return redirect('/dashboard')
        else:
            messages.info(request, "USERNAME OR PASSWORD DID NOT MATCH !!!")
            return redirect(login)
    else:
        return render(request, "Main/login.html")

def register(request):
    if request.method == "POST":
        station_code = request.POST["station_code"]
        user_name = str(request.POST["user_name"]).upper()
        email = str(request.POST["station_code"]).upper() + '@railway.com'
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            geolocator = Nominatim(user_agent="raj")
            location = geolocator.geocode(request.POST["station_name"])
            User.objects.create_user(username=email, password=password1, email=email, first_name=station_code, last_name=user_name).save()
            User.objects.filter(email=email)[0].is_active = False
            print(User.objects.filter(email=email)[0].is_active)
            Station(
                station_id      = User.objects.filter(email=email)[0].id,
                station_name    = request.POST["station_name"],
                location        = location.address,
                lat             = location.latitude,
                long            = location.longitude,
                total_train     = request.POST["total_train"],
                phone           = request.POST["phone"],
            ).save()
            return render(request, 'Main/index.html')
        else:
            messages.info(request, "both PASSWORD DID NOT MATCH !!! ")
            return redirect(register)
    else:
        return render(request, "Main/register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
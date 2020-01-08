from django.shortcuts import render

# Create your views here.
def track(request):
    return render(request, 'LiveTracking/track.html')
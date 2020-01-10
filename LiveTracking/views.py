from django.shortcuts import render

# Create your views here.
def track(request):
    if request.method == 'POST':
        print(request.POST.get('id', None))
    return render(request, 'LiveTracking/track.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def track(request):
    if request.method == 'POST':
        print(request.POST.get('id', None))
    return render(request, 'LiveTracking/update.html')
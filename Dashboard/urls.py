from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('/train', views.train),
    path('/send', views.parcel_send),
    path('/recieve', views.parcel_recieve),
    path('/noti', views.noti),
    path('/track', views.track),
    path('/parcel/<int:id>', views.parcel)
]
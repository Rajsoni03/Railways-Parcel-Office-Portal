from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome, name='home'),
    path('/parcels', views.parcels, name='parcels'),
    path('/pos', views.pos,  name='pos'),
    path('/train', views.train,  name='train'),
    path('/track', views.track,  name='track'),
    path('/login', views.login, name='login'),
    # path('contacts', views.contacts, name='contacts'),
]
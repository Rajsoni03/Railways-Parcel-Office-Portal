from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('pidata', views.setLocation),
    url('^/$', views.pi, name='pi'),
    url('^rfid/$', views.test, name='rfid'),
]

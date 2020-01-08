from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminHome),
    path('/parcels', views.parcels),
    path('/login', views.login)
]
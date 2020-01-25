from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about/<int:no>', views.about),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
]
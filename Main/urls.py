from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('train', views.train),
    path('about/<int:no>', views.about)
]
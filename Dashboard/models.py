from django.db import models
from django.utils import timezone


# Create your models here.
class Notification(models.Model):
    train_ID = models.PositiveIntegerField()
    train_no = models.PositiveIntegerField()
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    seal_status = models.BooleanField()
    parcels = models.PositiveIntegerField()
    station1 = models.CharField(max_length=10)
    station2 = models.CharField(max_length=10)
    station3 = models.CharField(max_length=10)
    msg = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = 'Notification'


class Otp(models.Model):
    parcel_id = models.CharField(max_length=10)
    otp = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = 'Otp'

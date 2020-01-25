from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class LiveTracking(models.Model):
    train_ID = models.PositiveIntegerField()
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    seal_status = models.BooleanField()
    parcel_status = models.BooleanField()
    date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = 'LiveTracking'

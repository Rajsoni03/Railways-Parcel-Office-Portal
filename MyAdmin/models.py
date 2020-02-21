from django.db import models

# Create your models here.
class TestData(models.Model):
    train_ID = models.PositiveIntegerField()
    lat = models.CharField(max_length=50)
    long = models.CharField(max_length=50)
    seal_status = models.BooleanField()
    parcel_status = models.BooleanField()
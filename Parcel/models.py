from django.db import models

statusChoices = (
    ('Pending', 'Pending'),
    ('Ordered', 'Ordered'),
    ('ShippingSoon', 'ShippingSoon'),
    ('Shipped', 'Shipped'),
    ('OutForDelivery', 'OutForDelivery'),
    ('Delivered', 'Delivered')
)


# Create your models here.
class Parcel(models.Model):
    parcel_id = models.CharField(max_length=20)
    rfid = models.CharField(max_length=20)
    train_id = models.PositiveIntegerField()
    sender_name = models.CharField(max_length=50)
    sender_adhar = models.CharField(max_length=20)
    reciever_name = models.CharField(max_length=50)
    reciever_adhar = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    parcel_from = models.CharField(max_length=20)
    parcel_to = models.CharField(max_length=20)
    parcel_info = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=statusChoices)
    date = models.DateTimeField(auto_now=True)
    done_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'Parcel'

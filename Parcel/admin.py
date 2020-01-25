from django.contrib import admin
from .models import Parcel

# Register your models here.
class ParcelAdmin(admin.ModelAdmin):
    list_display=['id','parcel_id','rfid','parcel_from','parcel_to','train_id','sender_name','reciever_name', 'date']
    list_editable=['parcel_id','rfid','parcel_from','parcel_to','train_id','sender_name','reciever_name']

admin.site.register(Parcel, ParcelAdmin)
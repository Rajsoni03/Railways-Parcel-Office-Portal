from django.contrib import admin
from .models import LiveTracking

# Register your models here.
class LiveTrackingAdmin(admin.ModelAdmin):
    list_display=['id','train_ID','lat','long','seal_status','parcel_status', 'date']
    list_editable=['train_ID','lat','long','seal_status','parcel_status']

admin.site.register(LiveTracking,LiveTrackingAdmin)
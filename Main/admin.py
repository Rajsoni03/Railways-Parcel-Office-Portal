from django.contrib import admin
from .models import Train, Station

# Register your models here.
class TrainAdmin(admin.ModelAdmin):
    list_display=['id','train_no','train_from','train_to', 'train_live_station', 'train_days', 'train_from_time', 'train_to_time']
    list_editable=['train_no','train_from','train_to','train_live_station', 'train_days']
admin.site.register(Train,TrainAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display=['id','station_id','location','lat', 'long', 'total_train']
    list_editable=['station_id','location','lat', 'long', 'total_train']
admin.site.register(Station,StationAdmin)
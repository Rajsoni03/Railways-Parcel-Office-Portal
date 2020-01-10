from django.contrib import admin
from .models import Train

# Register your models here.
class TrainAdmin(admin.ModelAdmin):
    list_display=['id','train_no','train_from','train_to', 'tarin_days', 'train_from_time', 'train_to_time']
    list_editable=['train_no','train_from','train_to', 'tarin_days']

admin.site.register(Train,TrainAdmin)
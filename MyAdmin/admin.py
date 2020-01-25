from django.contrib import admin
from .models import TestData
# Register your models here.

class TestDataAdmin(admin.ModelAdmin):
    list_display=['id','train_ID','lat','long','seal_status','parcel_status']
    list_editable=['train_ID','lat','long','seal_status','parcel_status']

admin.site.register(TestData,TestDataAdmin)
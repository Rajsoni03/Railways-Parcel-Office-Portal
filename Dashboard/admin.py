from django.contrib import admin
from .models import Notification, Otp


# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'train_ID', 'train_no', 'location', 'station1', 'station2', 'station3']
    list_editable = ['train_ID', 'train_no', 'location', 'station1', 'station2', 'station3']


admin.site.register(Notification, NotificationAdmin)


class OtpAdmin(admin.ModelAdmin):
    list_display = ['parcel_id', 'otp', 'date']
    list_editable = ['otp']


admin.site.register(Otp, OtpAdmin)

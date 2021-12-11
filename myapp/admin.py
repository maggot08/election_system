from django.contrib import admin

from myapp.models import *

# Register your models here
@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    list_display=('event_name','event_catagory','event_startdate','event_enddate')
    
from django.contrib import admin

from myapp.models import *

# Register your models here
# @admin.register(Event)
# class Eventadmin(admin.ModelAdmin):
#     list_display=('event_name','event_catagory','event_startdate','event_enddate')

admin.site.register([Event,])


@admin.register(Contestant)
class Contestantadmin(admin.ModelAdmin):
    list_display=('contestant_id','contestant_name','event','contestant_image','contestant_age','contentant_height')
    
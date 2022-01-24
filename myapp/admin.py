from django.contrib import admin

from myapp.models import *

admin.site.register([Event, Voted, Contestant, Profile])


# @admin.register(Contestant)
# class Contestantadmin(admin.ModelAdmin):
#     list_display=('contestant_id','contestant_name','event','contestant_image','contestant_age','contentant_height')
    

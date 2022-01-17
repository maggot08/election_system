
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index',views.home, name='index'),
    path('',views.home, name='index'),
    path('login',views.userlogin , name='login'),
    path('handlelogin',views.handlelogin , name='handlelogin'),
    path('signup',views.signup , name='signup'),
    path('handlesignup',views.handlesignup , name='handlesignup'),
    path('aboutus',views.aboutus , name='aboutus'),
    path('events',views.events , name='events'),
    path('howitworks',views.howitworks , name='howitworks'),
    path('contestants/<int:id>', views.contestants, name='contestantsid'),
    path('eventdetail',views.eventdetail , name='eventdetail'),
    path('contestant_profile',views.contestant_profile, name="contestant_profile"),


    path('dashboard',views.dashboard , name='dashboard'),
    path('logout',views.handlelogout , name='handlelogout'),
    path('event',views.event, name="event"),
    path('adminprofile',views.adminprofile, name="adminprofile"),
    
    path('voteresults', views.voteresults, name="voteresults"),
    path('results/<int:id>', views.results, name="results"),


    path('addevent',views.addevent, name="addevent"),
    path('editevent/<int:id>',views.editevent, name="editevent"),
    path('deleteevent/<event_id>',views.deleteevent, name="deleteevent"),
    
    path('isvoted/<int:id>',views.voted,name='voted'),
    
    
    
    path('contestanttables/<int:id>', views.contestanttables, name="contestanttables"),
    path('addcontestant',views.addcontestant, name="addcontestant"),
    path('editcontestant/<int:id>',views.editcontestant, name="editcontestant"),
    path('deletecontestant/<contestant_id>',views.deletecontestant, name="deletecontestant"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


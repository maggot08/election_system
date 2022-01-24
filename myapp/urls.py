
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

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
    path('eventdetail/<int:id>',views.eventdetail , name='eventdetail'),
    path('contestant_profile/<int:id>',views.contestant_profile, name="contestant_profile"),
    path('isvoted/<int:id>',views.voted,name='voted'),

    # Admin Dashboard urls
    
    path('dashboard',views.dashboard , name='dashboard'),
    path('logout',views.handlelogout , name='handlelogout'),
    path('adminprofile',views.adminprofile, name="adminprofile"),
    
    # Vote results urls
    
    path('voteresults', views.voteresults, name="voteresults"),
    path('results/<int:id>', views.results, name="results"),
    
    # CRUD urls

    path('event',views.event, name="event"),
    path('addevent',views.addevent, name="addevent"),
    path('editevent/<int:id>',views.editevent, name="editevent"),
    path('deleteevent/<event_id>',views.deleteevent, name="deleteevent"),

    # CRUD urls

    path('contestanttables/<int:id>', views.contestanttables, name="contestanttables"),
    path('addcontestant',views.addcontestant, name="addcontestant"),
    path('editcontestant/<int:id>',views.editcontestant, name="editcontestant"),
    path('deletecontestant/<contestant_id>',views.deletecontestant, name="deletecontestant"),

    # Reset Password urls
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="reset_password/password_reset.html"), 
        name="reset_password"),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="reset_password/password_reset_sent.html"), 
        name="password_reset_done"),
    
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_form.html"), 
        name="password_reset_confirm"),
    
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/password_reset_done.html"), 
        name="password_reset_complete"),

    #email verification
    path('token_send', views.token_send, name="token_send"),
    path('success', views.success, name="success"),
    path('verify/<auth_token>', views.verify, name="verify"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


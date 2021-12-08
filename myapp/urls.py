

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
    path('howtovote',views.howtovote , name='howtovote'),

    path('dashboard',views.dashboard , name='dashboard'),
    path('logout',views.handlelogout , name='handlelogout'),
    path('event',views.event, name="event"),
    

]
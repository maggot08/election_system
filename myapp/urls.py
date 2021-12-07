

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('index',views.home, name='index'),
    path('',views.home, name='index'),
    path('login',views.login , name='login'),
    path('signup',views.signup , name='signup'),
    path('aboutus',views.aboutus , name='aboutus'),
    path('events',views.events , name='events'),
    path('howtovote',views.howtovote , name='howtovote')

]
from django import forms
from django.db.models import fields
from django.db.models.base import Model

from myapp.models import Event
from django.forms import widgets
from django.contrib.admin.widgets import AdminDateWidget


class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields=['event_name','event_catagory','event_startdate','event_enddate']
        widgets= {
            'event_name':forms.TextInput(attrs={'class':'form-control w-50'},),
            'event_catagory':forms.TextInput(attrs={'class':'form-control  w-50'}),
            'event_startdate':forms.TextInput(attrs={'class':'form-control  w-50', 'type':'date'}),
            'event_enddate':forms.TextInput(attrs={'class':'form-control  w-50', 'type':'date'}),
        }
        
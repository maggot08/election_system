from django import forms
from django.db.models import fields
from django.db.models.base import Model

from myapp.models import *
from django.forms import widgets


class Addeventform(forms.ModelForm):
    class Meta:
        model=Event
        fields=['event_name','event_catagory', 'event_image','event_startdate','event_enddate']
        widgets= {
            'event_name':forms.TextInput(attrs={'class':'form-control w-50'},),
            'event_catagory':forms.TextInput(attrs={'class':'form-control w-50'}),
            'event_image':forms.FileInput(attrs={'class':'form-control w-50'}),
            'event_startdate':forms.TextInput(attrs={'class':'form-control w-50', 'type':'date'}),
            'event_enddate':forms.TextInput(attrs={'class':'form-control w-50', 'type':'date'}),
        }


class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields=['event_name','event_catagory', 'event_image','event_startdate','event_enddate']
        widgets= {
            'event_name':forms.TextInput(attrs={'class':'form-control w-50'},),
            'event_catagory':forms.TextInput(attrs={'class':'form-control  w-50'}),
            'event_image':forms.FileInput(attrs={'class':'form-control  w-50'}),
            'event_startdate':forms.TextInput(attrs={'class':'form-control  w-50', 'type':'date'}),
            'event_enddate':forms.TextInput(attrs={'class':'form-control  w-50', 'type':'date'}),
        }

class Contestantform(forms.ModelForm):
    class Meta:
        model=Contestant
        fields=['contestant_id','event','contestant_name','contestant_image','contestant_age','contentant_height']
        widgets= {
            'contestant_id':forms.TextInput(attrs={'class':'form-control w-50'},),
            'event':forms.Select(attrs={'class':'form-control w-50'},),
            'contestant_name':forms.TextInput(attrs={'class':'form-control w-50'},),
            'contestant_image':forms.FileInput(attrs={'class':'form-control  w-50'}),
            'contestant_age':forms.TextInput(attrs={'class':'form-control  w-50'}),
            'contentant_height':forms.TextInput(attrs={'class':'form-control  w-50'}),
        }




        
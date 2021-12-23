from django.db import models

# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=30)
    event_catagory=models.CharField(max_length=30)
    event_startdate=models.CharField(max_length=30)
    event_enddate=models.CharField(max_length=30)

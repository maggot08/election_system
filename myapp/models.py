from email.policy import default
from multiprocessing.dummy import Array
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from autoslug import AutoSlugField
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=30)
    event_catagory=models.CharField(max_length=30)
    event_image=models.ImageField(blank=True, null=True, upload_to="eventimages/")
    event_startdate=models.DateField(blank=True)
    event_enddate=models.DateField(blank=True)
    slug=AutoSlugField(populate_from='event_name')

    def __str__(self):
        return str(self.event_name)

class Contestant(models.Model):
    contestant_id=models.CharField(max_length=30, unique=True)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    contestant_name=models.CharField(max_length=30)
    contestant_image=models.ImageField(blank=True, null=True, upload_to="contestantimages/")
    contestant_age=models.CharField(max_length=30)
    contentant_height=models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.contestant_name)

class Voted(models.Model):
    is_voted=models.BooleanField(default=False)
    voting_user_id=ArrayField(models.IntegerField())
    # voting_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    count=models.IntegerField(default=0)
    contestant=models.ForeignKey(Contestant,on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.count}--{self.contestant.contestant_name}--{self.event.event_name}'





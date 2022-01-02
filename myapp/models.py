from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Event(models.Model):
    event_name=models.CharField(max_length=30)
    event_catagory=models.CharField(max_length=30)
    event_image=models.ImageField(blank=True, null=True, upload_to="eventimages/")
    event_startdate=models.CharField(max_length=30)
    event_enddate=models.CharField(max_length=30)
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
        return str(self.contestant_id)

class Voted(models.Model):
    is_voted=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=CASCADE)
    count=models.IntegerField(default=0)
    contestant=models.ForeignKey(Contestant,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.contestant)




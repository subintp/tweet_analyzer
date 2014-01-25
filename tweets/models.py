from django.db import models
import datetime
from django.utils import timezone


class Tweet(models.Model):
    
    text = models.CharField(max_length=200)
    reply = models.BooleanField(default=False)
    retweet = models.BooleanField(default=False)
    time = models.DateTimeField()
        
    def __unicode__(self): 
       return self.text


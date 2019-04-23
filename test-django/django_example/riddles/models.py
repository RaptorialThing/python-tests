from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Riddle(models.Model):
    riddle_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')

class Option(models.Model):
    riddle = models.ForeignKey(Riddle,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
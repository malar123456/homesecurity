from django.db import models

# Create your models here.
class SmokeData(models.Model):
    smoke_value = models.IntegerField()  # Store the smoke value
    timestamp = models.DateTimeField()  # Automatically store current date and time

class HumanData(models.Model):
    human_value = models.IntegerField()  
    timestamp = models.DateTimeField()  
    
class ObjectData(models.Model):
    object_value = models.IntegerField()  
    timestamp = models.DateTimeField()  
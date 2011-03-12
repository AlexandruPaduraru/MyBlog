from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.TextField(max_length=256)
    author = models.CharField(max_length=50)
    date = models.DateField()
    
class Comment(models.Model):
    text = models.TextField(max_length=256)
    author = models.CharField(max_length=50)
    date = models.DateField()
    message = models.ForeignKey(Message)
    


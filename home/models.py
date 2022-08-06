from ast import Str
from distutils.command.upload import upload
from operator import mod
from re import S
from django.db import models

# Create your models here.

class Speakers(models.Model):
    
    name = models.CharField(max_length=70)
    img  = models.ImageField(upload_to='pics')
    desc = models.TextField()

    
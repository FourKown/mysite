from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

class IKSAN (models.Model):
    Title = models.CharField(max_length=50, default = '')
    Range = models.CharField(max_length=50, default = '')
    Lat = models.FloatField(null = True)
    Lon = models.FloatField(null = True)
    
    def __str__(self):
        return self.Title

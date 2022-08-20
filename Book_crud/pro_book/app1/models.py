from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField()
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    

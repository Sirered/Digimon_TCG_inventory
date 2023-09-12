from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length= 225)
    release = models.CharField(max_length= 225)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
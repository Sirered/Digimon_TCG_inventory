from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length= 225)
    set_release = models.CharField(max_length= 225)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
from django.db import models
import datetime

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length= 225)
    code = models.CharField(max_length= 225)
    amount = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    date_added = models.DateField(default=datetime.date(2023,9,15))
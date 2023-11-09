from django.db import models
from django.contrib.auth.models import User
import datetime

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length= 225)
    code = models.CharField(max_length= 225)
    amount = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    date_added = models.DateField(default=datetime.date(2023,9,15))
    COLOR_CHOICES = [
        ("Blue", "Blue"),
        ("Red", "Red"),
        ("Green", "Green"),
        ("Yellow", "Yellow"),
        ("Purple", "Purple"),
        ("Black", "Black"),
        ("White", "White")
    ]
    color = models.CharField(max_length=11, choices=COLOR_CHOICES)
    rarity = models.CharField(max_length = 3, default='R')
from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    
class Reservation(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    guest_count = models.IntegerField()
    resevatation_date = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
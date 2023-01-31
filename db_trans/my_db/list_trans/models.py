from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.IntegerField(default=0)
    ati = models.IntegerField(default=0)
    direction = models.CharField(max_length=50) 
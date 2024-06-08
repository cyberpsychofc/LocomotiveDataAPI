from django.db import models

class Locomotive(models.Model):
    motive_power = models.CharField(max_length=50)
    gauge = models.CharField(max_length=50)
    name = models.CharField(primary_key=True, max_length=50)
    traction = models.CharField(max_length=50)
    usage = models.CharField(max_length=50)
    series = models.CharField(max_length=25)
    numbers = models.CharField(max_length=50)
    img_src = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    axles = models.CharField(max_length=50)
    numbers_built = models.IntegerField()
    production = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    status = models.CharField(max_length=25)
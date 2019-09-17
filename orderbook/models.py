from django.db import models

# Create your models here.
class equity(models.Model):
    symbol = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    price = models.FloatField()


class derivative(models.Model):
	expiry_date = 	models.DateField()
	call = 	models.BooleanField()
	price = models.FloatField()
	datetime = models.DateTimeField()
from django.db import models

# Create your models here.
class equity(models.Model):
    symbol = models.CharField(max_length=20,unique=True)
    ltp =models.FloatField(default=0.0)
    buy_watch_price =models.FloatField(default=0.0)
    sell_watch_price =models.FloatField(default=0.0)
    buy_per_change = models.FloatField(default=0.0)
    sell_per_change = models.FloatField(default=0.0)
    y_h = models.FloatField(default=0.0)
    y_l = models.FloatField(default=0.0)
    pinned = models.BooleanField(default=False) 
    
    def __str__(self):
    	return self.symbol


class derivative(models.Model):
	expiry_date = 	models.DateField()
	call = 	models.BooleanField()
	strike_price = models.FloatField()
	pinned = models.BooleanField(default=False)
	class Meta:
		unique_together = ('expiry_date', 'call','strike_price')
	def __str__(self):
		if self.call==True:
			c='call'
		else:
			c='put'
		return str(self.strike_price)+" "+c+" "+str(self.expiry_date)
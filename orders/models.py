from django.db import models

# Create your models here.
class Toppings(models.Model):
	name = models.CharField(max_length=64)
	#available = models.boolean
	#for_ = onetomanyrelationship 

class Items(models.Model):
	name = models.CharField(max_length=15, unique=True)
	category = models.CharField(max_length=10)
	extras = models.IntegerField(null=True)
	price = models.FloatField()
	price_l = models.FloatField(null=True)

	def __str__(self):
		return f"{self.name}"
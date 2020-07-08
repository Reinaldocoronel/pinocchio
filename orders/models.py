from django.db import models

# Create your models here.


class Toppings(models.Model):
	name = models.CharField(max_length=64, unique=True)
	available = models.BooleanField(default=True)
	

	def __str__(self):
		return f"{self.name}"

class Items(models.Model):
	name = models.CharField(max_length=30)
	category = models.CharField(max_length=10)
	extras = models.IntegerField(null=True)
	price = models.FloatField()
	price_l = models.FloatField(null=True)
	toppings =  models.ManyToManyField(Toppings, related_name='item')

	def __str__(self):
		return f"{self.category}: {self.name}"

	class Meta:
		unique_together = (('name','category'))


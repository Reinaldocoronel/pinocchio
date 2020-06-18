from django.db import models

# Create your models here.
class Topings(models.Model):
	name = models.CharField(max_length=64)
	#available = models.boolean
	#for_ = onetomanyrelationship 

class Items(models.Model):
	name = models.CharField(max_length=15, unique=True)
	tipe = models.CharField(max_length=10)
	extras = models.IntegerField(null=True)

class Prices(models.Model):
	price = models.FloatField()
	size  = models.CharField(max_length=4)
	item  = models.ForeignKey(Items, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.price:.2f}$"

	class Meta:
		unique_together = ['item', 'size']
from django.test import TestCase

from .models import Prices, Items
# Create your tests here.
class ModelsTestCase(TestCase):

	def setUp(self):
		m1 = Items.objects.create(name="2 topings", tipe="regular", extras=2)
		m2 = Items.objects.create(name="ceasar", tipe="salad")
		m1.prices_set.create(price=21.95, tipe='larg')
		m1.prices_set.create(price=15.20, tipe='smal')
		m2.prices_set.create(price=8.25, tipe='smal')
	
	def test_items_count(self):
		menu = Items.objects.all()
		self.assertEqual(menu.count(), 2)

	def test_items_prices_large(self):
		item = Items.objects.get(name="2 topings")
		price_larg = item.prices_set.get(tipe='larg')
		self.assertEqual(str(price_larg), "21.95$")

	def test_items_price(self):
		item = Items.objects.get(name="ceasar")
		price = item.prices_set.first()
		self.assertEqual(str(price), "8.25$")
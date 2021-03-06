from django.test import TestCase, Client

from .models import Items
# Create your tests here.
class ModelsTestCase(TestCase):

	def setUp(self):
		m1 = Items.objects.create(name="2 topings", category="regular", price=15.20, price_l=21.95, extras=2)
		m2 = Items.objects.create(name="ceasar", category="salad", price=8.25)
	
	def test_items_count(self):
		menu = Items.objects.all()
		self.assertEqual(menu.count(), 2)

	def test_items_prices_large(self):
		item = Items.objects.get(name="2 topings")
		price_larg = item.price_l
		self.assertEqual(price_larg, 21.95)

	def test_items_price(self):
		item = Items.objects.get(name="ceasar")
		price = item.price
		self.assertEqual(price, 8.25)

	def test_category_filtering(self):
		m3 = Items.objects.create(name="3 topings", category="regular", price=16.20, price_l=25.95, extras=3)
		r = Items.objects.filter(category='regular')
		self.assertEqual(r.count(), 2)


	def test_menu_parsing(self):
		c = Client()
		m3 = Items.objects.create(name="3 topings", category="regular", price=16.20, price_l=25.95, extras=3)
		response = c.get("/")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.context["categories"]), 2)
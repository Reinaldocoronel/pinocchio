from django.http import HttpResponse
from django.shortcuts import render

from .models import Items, Toppings
# Create your views here.
def index(request):
	categories = {}
	keys = Items.objects.values_list('category', flat=True).distinct()
	for key in keys:
		items = Items.objects.filter(category=key)
		categories[key]=items
	context = {
		"categories": categories
	}
	print(categories)
	return render(request, "orders/menu.html", context)
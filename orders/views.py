from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Items, Toppings
# Create your views here.
def index(request):
	categories = {}
	keys = list(Items.objects.values_list('category', flat=True).distinct())
	context = {"categories": keys}
	return render(request, "orders/menu.html", context)

@csrf_exempt
def category(request, category):
	try:
		items =  list(Items.objects.filter(category=category).values())
	#find which exception is thrown 
	except KeyError:
		return JsonResponse(status=404)
	return JsonResponse(items, safe = False)

def topping(request, item):
	item = Items.objects.get(pk=item)
	toppings = list(item.toppings.all().values())
	return JsonResponse(toppings, safe = False)

#def image(request, filename):
#	try:
#		with open(f"/static/oders/{filename}", "rb") as f:
#			return HttpResponse(f.read(), content_type="image/png")
#	except IOError:
#		response = HttpResponse(status=404)
#		return response
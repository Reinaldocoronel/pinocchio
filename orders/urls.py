from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("API/<category>", views.category, name="category"),
    path("API/toppings/<item>", views.topping, name="topping"),
]

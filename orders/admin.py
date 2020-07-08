from django.contrib import admin

from .models import Items, Toppings
# Register your models here.

class ItemsInLine(admin.StackedInline):
	model = Items.toppings.through
	extra = 1

class ToppingsAdmin(admin.ModelAdmin):
	inlines = [ItemsInLine]

class ItemsAdmin(admin.ModelAdmin):
	filter_horizontal = ("toppings",)

admin.site.register(Items, ItemsAdmin)
admin.site.register(Toppings, ToppingsAdmin)
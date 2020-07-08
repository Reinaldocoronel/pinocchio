from orders import models
import csv

def impor(comas):
	menu = open(comas)
	reader = csv.reader(menu)

	for name, category, extra, price, price_l in menu:
		item = Items.objects.create(name=name, category=category, extra=extra, price=price, price_l=price_l)

	def main():
		impor(menu.csv)

	if __name__ == "__main__":
		main()
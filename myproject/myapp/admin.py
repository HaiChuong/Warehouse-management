from django.contrib import admin
from myproject.models import Product, Import, Export, Inventory

# Register your models here.

admin.site.register(Product)
admin.site.register(Import)
admin.site.register(Export)
admin.site.register(Inventory)

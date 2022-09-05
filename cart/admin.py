from unicodedata import name
from django.contrib import admin
from cart.models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved')



admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
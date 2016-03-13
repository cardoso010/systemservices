from django.contrib import admin
from systemservices.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'value', 'quantity', 'created_at')
    list_filter = ('name', 'quantity')

admin.site.register(Product, ProductAdmin)

from django.contrib import admin

from .models import Category, Order, OrderItem, Product

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

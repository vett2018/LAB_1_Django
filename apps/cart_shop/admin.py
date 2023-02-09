#добавление модели в админку
from django.contrib import admin
from .models import CartItemShop, Product

admin.site.register(CartItemShop)
admin.site.register(Product)

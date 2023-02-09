from django.shortcuts import render
from django.views import View


class ShopView(View):

   def get(self, request):
       return render(request, 'shop/shop.html')

class ShopProductSingle(View):
   def get(self, request):
       return render(request, 'shop/product-single.html')
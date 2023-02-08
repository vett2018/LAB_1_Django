from django.shortcuts import render
from django.views import View

class IndexShopView(View):

   def get(self, request):
       return render(request, 'home/contact.html')

   def get(self, request):
       return render(request, 'home/about.html')

   context = {'data': [{'name': 'Bell Pepper',
                        'discount': 30,
                        'price_before': 120.00,
                        'price_after': 80.00,
                        'url': 'shop/images/product-1.jpg'}
                       ]
              }

   def get(self, request):
       return render(request, 'home/index.html')






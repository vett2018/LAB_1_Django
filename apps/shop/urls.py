from django.urls import path
from .views import ShopView

app_name = 'shop'


urlpatterns = [
   path('', ShopView.as_view(), name='product-single'),
   path('', ShopView.as_view(), name='shop'),

]
from django.urls import path
from .views import ShopView, ShopProductSingle

app_name = 'shop'


urlpatterns = [
   path('', ShopView.as_view(), name='shop'),
   path('product-single/', ShopProductSingle.as_view(), name='product-single'),

]
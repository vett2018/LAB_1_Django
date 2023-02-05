from django.urls import path
from .views import ViewCart

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('', ViewCart.as_view(), name='wishlist'),
]

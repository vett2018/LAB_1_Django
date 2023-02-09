from django.urls import path
from .views import ViewCart, ViewCartWishlist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('wishlist/', ViewCartWishlist.as_view(), name='wishlist'),
]

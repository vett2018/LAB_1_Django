from django.urls import path
from .views import ViewCart, ViewCartWishlist, ViewCartBuy, ViewCartDel, ViewCartAdd

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('wishlist/', ViewCartWishlist.as_view(), name='wishlist'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
   path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),

]

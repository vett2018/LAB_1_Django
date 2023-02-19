from django.urls import path
from .views import ViewCart, ViewWishlist, ViewCartBuy, ViewCartDel, ViewCartAdd, ViewDelCartWishlist, VievAddWislist

app_name = 'cart_shop'

urlpatterns = [
   path('', ViewCart.as_view(), name='cart'),
   path('wishlist/', ViewWishlist.as_view(), name='wishlist'),
   path('buy/<int:product_id>', ViewCartBuy.as_view(), name='buy'),
   path('del/<int:item_id>', ViewCartDel.as_view(), name='del_from_cart'),
   path('add/<int:product_id>', ViewCartAdd.as_view(), name='add_to_cart'),
   #path('delwishilst/<int:wishlist_id>', ViewDelCartWishlist.as_view(), name='del_from_wishlist'), # [! Ошибка]
   path('delwishilst/<int:wishlist_id>', ViewDelCartWishlist.as_view(), name='del_from_wishlist'),
   path('addwishilst/<int:product_id>', VievAddWislist.as_view(), name='add_from_wishlist'),
]

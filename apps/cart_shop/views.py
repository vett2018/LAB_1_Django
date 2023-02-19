from django.shortcuts import render
from django.views import View
from .models import CartItemShop, Cart, Product, Wishlist
from django.shortcuts import render, get_object_or_404, redirect


class ViewCart(View):
   def get(self, request):
       if request.user.is_authenticated:  # ПРОВЕРКА НА АВТОРИЗАЦИЮ
           cart_items = CartItemShop.objects.filter(cart__user=request.user)
           data = list(cart_items)
           total_price_no_discount = sum(item.product.price * item.quantity
                                         for item in data)
           total_discount = sum(item.product.price * item.product.discount * item.quantity
                                for item in data if item.product.discount is not None)/100
           total_sum = total_price_no_discount - total_discount
           context = {'cart_items': data,
                      'total_price_no_discount': total_price_no_discount,
                      'total_discount': total_discount,
                      'total_sum': total_sum,
                      }
           return render(request, 'cart_shop/cart.html', context)
       return redirect('auth_shop:login')

class VievAddWislist(View): # ДОБАВЛЕНИЕ ТОВАРА С ГЛАВНОЙ СТРАНИЦЫ В СПИСОК ЖЕЛАНИЙ
    def get(self, request, product_id):
            if request.user.is_authenticated:  # ПРОВЕРКА НА АВТОРИЗАЦИЮ
                product = get_object_or_404(Product, id=product_id)
                wishlist_user = get_object_or_404(Cart, user=request.user)
                wishlist_item = Wishlist(cart=wishlist_user, product=product)

                wishlist_items = Wishlist.objects.filter(cart__user=request.user, product__id=product_id)
                if wishlist_items:  # ПРОВЕРКА ТОВАРА ЕСТЬ ЛИ ТОВАР УЖЕ В СПИСКЕ ЖЕЛАНИЙ
                    wishlist_item = wishlist_items[0]
                    wishlist_item.quantity += 0
                else:
                    product = get_object_or_404(Product, id=product_id)
                    wishlist_user = get_object_or_404(Cart, user=request.user)
                    wishlist_item = Wishlist(cart=wishlist_user, product=product)
                wishlist_item.save()
                return redirect('home:index')
            return redirect('auth_shop:login')

class ViewWishlist(View): #ОБРАБОТЧИК СПИСКА ЖЕЛАНИЙ
    def get(self, request):
        if request.user.is_authenticated: #ПРОВЕРКА НА АВТОРИЗАЦИЮ
            cart_items_wishlist = Wishlist.objects.filter(cart__user=request.user)
            data = list(cart_items_wishlist)
            context = {'cart_items_wishlist': data,
                       }
            return render(request, 'cart_shop/wishlist.html', context)
        return redirect('auth_shop:login')

class ViewDelCartWishlist(View): #УДАЛЕНИЕ ИЗ СПИСКА ЖЕЛАНИЙ
    def get(self, request, wishlist_id):
        cart_items_wishlist = get_object_or_404(Wishlist, id=wishlist_id)
        cart_items_wishlist.delete()
        return redirect('cart_shop:wishlist')

# class ViewCartWishlist(View): #ОБРАБОТЧИК СПИСКА ЖЕЛАНИЙ [! Ошибка]
#     def get(self, request):
#         cart_items_wishlist = Wishlist.objects.filter(cart__user=request.user)
#         data = list(cart_items_wishlist)
#         context = {'cart_items_wishlist': data,
#                    }
#         return render(request, 'cart_shop/wishlist.html', context)
#
# class ViewDelCartWishlist(View): #УДАЛЕНИЕ ИЗ СПИСКА ЖЕЛАЕМОГО [! Ошибка]
#     def get(self, request):
#         def get(self, request, wishlist_id):
#             cart_items_wishlist = get_object_or_404(Wishlist, id=wishlist_id)
#             cart_items_wishlist.delete()
#             return redirect('cart_shop:wishlist')

class ViewCartDel(View): #УДАЛЕНИЕ ТОВАРА ИЗ КОРЗИНЫ
   def get(self, request, item_id):
       cart_item = get_object_or_404(CartItemShop, id=item_id)
       cart_item.delete()
       return redirect('cart_shop:cart')

class ViewCartBuy(View): # ПРЕДСТАВЛЕНИЕ ДЛЯ ОБРАБОТКИ ДОБАВЛЕНИЯ В БД И ПЕРЕХОДА В КОРЗИНУ
   def get(self, request, product_id):
       if request.user.is_authenticated:  # ПРОВЕРКА НА АВТОРИЗАЦИЮ
           #product = get_object_or_404(Product, id=product_id)
           #cart_user = get_object_or_404(Cart, user=request.user)
           #cart_item = CartItemShop(cart=cart_user, product=product)
           #cart_item.save()
           save_product_in_cart(request, product_id)
           return redirect('cart_shop:cart')
       return redirect('auth_shop:login')

class ViewCartAdd(View): #ДОБАВЛЕНИЕ ТОВАРА С ГЛАВНОЙ СТРАНИЦЫ
   def get(self, request, product_id):
       if request.user.is_authenticated:  # ПРОВЕРКА НА АВТОРИЗАЦИЮ
           #product = get_object_or_404(Product, id=product_id)
           #cart_user = get_object_or_404(Cart, user=request.user)
           #cart_item = CartItemShop(cart=cart_user, product=product)
           #cart_item.save()
           save_product_in_cart(request, product_id)
           return redirect('home:index')
       return redirect('auth_shop:login')

def save_product_in_cart(request, product_id): #ОТДЕЛЬНАЯ ФУНКЦИЯ ДОБАВЛЕНИЕ ТОВАРА В КОРЗИНУ
   cart_items = CartItemShop.objects.filter(cart__user=request.user, product__id=product_id)
   if cart_items: #ПРОВЕРКА ТОВАРА ЕСТЬ ЛИ ОН УЖЕ В КОРЗИНЕ УВЕЛИЧИВАЕМ КОЛЛИЧЕСТВО
       cart_item = cart_items[0]
       cart_item.quantity += 1
   else:
       product = get_object_or_404(Product, id=product_id)
       cart_user = get_object_or_404(Cart, user=request.user)
       cart_item = CartItemShop(cart=cart_user, product=product)
   cart_item.save()

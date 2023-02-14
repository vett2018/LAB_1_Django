"""project_lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.cart_shop.views import ViewCartWishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('other/', include('apps.common_lab_1.urls')),
    path('other/', include('apps.new_common.urls')),
    path('other/', include('apps.login_app.urls')),
    path('other/cart/', include('apps.cart.urls')),
    path('', include('apps.home.urls')),
    path('wishlist/', ViewCartWishlist.as_view()),
    path('cart/', include('apps.cart_shop.urls')),
    path('checkout/', include('apps.checkout.urls')),
    path('blog/', include('apps.blog.urls')),
    path('shop/', include('apps.shop.urls')),
    path('login/', include('apps.auth_shop.urls')),
]

from django.contrib import admin
from django.urls import path

from .views import IndexShopView, AboutShopView, ContactShopView

app_name = 'home'


urlpatterns = [
   path('contact/', ContactShopView.as_view(), name='contact'),
   path('about/', AboutShopView.as_view(), name='about'),
   path('', IndexShopView.as_view(), name='index'),
]


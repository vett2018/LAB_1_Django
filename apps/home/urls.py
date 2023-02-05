from django.contrib import admin
from django.urls import path

from .views import IndexShopView

app_name = 'home'


urlpatterns = [
   path('', IndexShopView.as_view(), name='index'),
   path('', IndexShopView.as_view(), name='contact'),
   path('', IndexShopView.as_view(), name='about'),
]


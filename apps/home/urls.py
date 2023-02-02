from django.contrib import admin
from django.urls import path

from .views import IndexShopView

urlpatterns = [
   path('', IndexShopView.as_view()),
]


from django.contrib import admin
from django.urls import path

from .views import Hello

urlpatterns = [
   path('Hello/', Hello.as_view()),
]
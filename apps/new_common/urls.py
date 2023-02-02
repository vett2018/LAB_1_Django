from django.contrib import admin
from django.urls import path

from .views import Hello

urlpatterns = [
   path('hello_world/', Hello.as_view()),
]
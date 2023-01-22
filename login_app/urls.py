from django.contrib import admin
from django.urls import path

from .views import LoginApp

urlpatterns = [
   path('LoginApp/', LoginApp.as_view()),
]
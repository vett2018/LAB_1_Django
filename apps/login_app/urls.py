from django.contrib import admin
from django.urls import path

from .views import LoginApp

urlpatterns = [
   path('login_app/', LoginApp.as_view()),
]
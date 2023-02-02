#работа с приложением, настройка маршрутизации
from django.contrib import admin
from django.urls import path

from .views import CurrentDateView
from .views import Random
from .views import IndexView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('random/', Random.as_view()),
   path('index_view/', IndexView.as_view()),
]
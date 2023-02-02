from datetime import datetime
from random import random

from django.shortcuts import render


from django.views import View
from django.http import HttpResponse


class CurrentDateView(View):
   def get(self, request):
       html = f"{datetime.now()}"
       return HttpResponse(html)

class Random(View): #класс случайное число
    def get(self, request): #метод возвращающий случайное число
        html = f"{random()}"
        random_number = random()
        return HttpResponse(html)

class Hello(View): #класс приветсвие
    def get(self, request):
        return HttpResponse("Hello, World")

class IndexView(View):
   def get(self, request):
       return render(request, 'common_lab_1/index.html')
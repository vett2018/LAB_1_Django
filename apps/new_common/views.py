from django.views import View
from django.http import HttpResponse

class Hello(View): #класс приветсвие
    def get(self, request):
        return HttpResponse("Hello, World")
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


class Login(View):
   def get(self, request):
       return render(request, "auth_shop/index.html")

   def post(self, request):
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(username=username, password=password)
           if user is not None:
               login(request, user)
               print(user)
               return redirect('home:index')
       return redirect('auth_shop:login')

"""
class LoginApp(View):
    def get (self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})
"""
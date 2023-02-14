from django.urls import path
from .views import Login

app_name = "auth_shop"

urlpatterns = [
  path('', Login.as_view(), name="login"),
]

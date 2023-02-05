from django.urls import path
from .views import CheckOut

app_name = 'checkout'

urlpatterns = [
   path('', CheckOut.as_view(), name='checkout'),
]

from django.urls import path
from orders.views import home, Register

urlpatterns = [
    path('', home , name='index.html'),
    path('register/', Register, name='register'),
]

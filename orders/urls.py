
from django.urls import path
from orders.views import home

urlpatterns = [
    path('', home , name='index.html'),

]

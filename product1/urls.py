from django.urls import path
from .views import get_info,get_product



urlpatterns = [
    path('',get_info,name='get_info'),
    path('products/<int:pk>',get_product,name='get_product')
]
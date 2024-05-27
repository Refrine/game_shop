from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('purchase/', views.purchase, name='purchase'),
]
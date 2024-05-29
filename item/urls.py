from . import views
from django.urls import path


app_name = 'item'


urlpatterns = [
    path('', views.items , name='items'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
     
]

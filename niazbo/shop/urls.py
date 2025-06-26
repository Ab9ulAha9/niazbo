from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.products , name='shop' ),
    path('cart/', views.cart, name='cart'), 
    path('order/' , include('orders.urls'))
] 
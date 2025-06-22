from django.urls import path
from . import views


urlpatterns = [
    path('', views.products , name='shop' ),
    path('cart/', views.cart, name='cart'),
]
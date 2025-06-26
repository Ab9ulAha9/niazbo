from django.urls import path
from . import views


urlpatterns = [
    path('', views.orders_create , name='orders' ),
    path('track/<uuid:token>/', views.order_status, name='track_order') ,
    path ('checkout/' , views.checkout , name='checkout' ) ,
]
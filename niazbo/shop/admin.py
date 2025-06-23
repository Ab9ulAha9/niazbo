from django.contrib import admin
from .models import Product , Cart , CartItem , discount
# Register your models here.
admin.site.register(Product)  
admin.site.register(Cart) 
admin.site.register(CartItem)
admin.site.register(discount)
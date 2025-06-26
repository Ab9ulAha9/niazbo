from django.contrib import admin
from .models import orders , shipping_fee
# Register your models here.
admin.site.register(orders)
admin.site.register(shipping_fee)
from django.contrib import admin
from .models import Product , Cart , CartItem , discount
# Register your models here.
admin.site.register(Product)  
admin.site.register(CartItem)
admin.site.register(discount)  


from django.contrib import admin
from .models import Cart
from django.utils import timezone

@admin.action(description='Delete expired carts')
def delete_expired_carts(modeladmin, request, queryset):
    now = timezone.now()
    expired = queryset.filter(expires_at=now)
    count = expired.count()
    expired.delete()
    modeladmin.message_user(request, f"{count} expired cart(s) deleted.")

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expires_at']
    actions = [delete_expired_carts]

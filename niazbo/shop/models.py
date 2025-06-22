from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField("price",  validators=[MinValueValidator(0)])
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    created_at = models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField("stock" , default=0, validators=[MinValueValidator(0)])
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    
    session_key = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return f"Cart {self.id} - Session: {self.session_key}"
    def total_price(self):
        return sum(item.rotal_price for item in self.items.all())

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField("quantity", default=1, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    @property
    def total_price(self):
        return self.product.price * self.quantity 
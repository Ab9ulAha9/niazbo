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
    
class discount (models.Model):
    discount = models.IntegerField(default=0 , validators=[MinValueValidator(0)])
    min_purchase=models.IntegerField(default=0 ,  validators=[MinValueValidator(0)] , help_text="enter the minimum  purchase at which discount starts ")
    created_at=models.DateTimeField(auto_now=True)

class Cart(models.Model):
    
    session_key = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.IntegerField(default=0 , validators=[MinValueValidator(0)]) 
    expires_at=models.DateTimeField( auto_now=True)
    def __str__(self):
        return f"Cart {self.id} - Session: {self.session_key}"
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all()) 
    @property
    def after_discount(self):
        if self.discount >0:
            return self.total_price-(self.total_price/100)*self.discount
        return self.total_price
        


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField("quantity", default=1, validators=[MinValueValidator(1)])
    
    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    @property
    def total_price(self):
        return self.product.price * self.quantity 
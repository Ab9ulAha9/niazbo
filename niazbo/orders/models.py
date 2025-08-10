from django.db import models
from shop.models import Product
from phonenumber_field.modelfields import PhoneNumberField
import uuid 

# Create your models here.
PUNJAB_DIVISIONS = [
('Bahawalpur', 'Bahawalpur'),
('Dera Ghazi Khan', 'Dera Ghazi Khan'),
('Faisalabad', 'Faisalabad'),
('Gujranwala', 'Gujranwala'),
('Lahore', 'Lahore'),
('Multan', 'Multan'),
('Rawalpindi', 'Rawalpindi'),
('Sahiwal', 'Sahiwal'),
('Sargodha', 'Sargodha'),
('other', 'other'),
]



class orders (models.Model):
    ORDER_STATUS_CHOICES = [
    ('ORDER PLACED', 'Order PLaced'),
    ('SHIPPED', 'Shipped'),
    ('OUT FOR DELIVERY' , 'Out for Deliverey') ,
    ('DELIVERED', 'Delivered'),
    ('CANCELLED', 'Cancelled'),
    ('RETURNED', 'Returned'),
    ('FAILED', 'Failed'),
    ]
    name=models.CharField(max_length=30)
    tracking_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    email=models.EmailField()
    phone_number=PhoneNumberField(region="PK")
    created_at=models.DateTimeField(auto_now_add=True)
    products=models.ManyToManyField(Product)
    address=models.TextField(max_length=50)
    division=models.CharField(max_length=50, choices=PUNJAB_DIVISIONS)
    status=models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES , default="ORDER PLACED" )
    is_paid=models.BooleanField(default=False) 
    payment=models.IntegerField(default=None , null=True) 
    def __str__ (self):
        return f"{self.status} to {self.address}" 



class shipping_fee(models.Model):
    divison=models.CharField(max_length=50, choices=PUNJAB_DIVISIONS)
    fee=models.IntegerField() 
    def __str__(self):
        return self.divison
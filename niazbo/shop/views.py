from django.shortcuts import render
from .models import Product , Cart , CartItem
from django.shortcuts import get_object_or_404
# Create your views here.

def get_cart (request):
    if not (sess_key:= request.session.session_key):
        request.session.create()
    sess_key=request.session.session_key
    cart,_=Cart.objects.get_or_create(session_key=sess_key)
    return (cart)

def cart (request ):
    cart=get_cart(request)
    return render("cart.html" , {"cart":cart}) 

def create_item (request ):
    product_id=request.POST.get('product_id')
    product=get_object_or_404(Product , id=product_id)
    crt=get_cart(request)
    item , created =CartItem.objects.get_or_create(product=product , cart=crt) 
    if not created :
        item.quantity +=1
        item.save()

def products(request):
    if request.method=="POST":
        create_item(request)
    products= Product.objects.all()
    return render(request, 'products.html' , {'products': products}) 




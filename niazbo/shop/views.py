from django.shortcuts import render
from .models import Product , Cart , CartItem , discount 
from django.shortcuts import get_object_or_404
# Create your views here.

def get_cart (request):
    if not ( request.session.session_key):
        request.session.create()
    sess_key=request.session.session_key
    cart,_=Cart.objects.get_or_create(session_key=sess_key)
    d=discount.objects.first()
    if cart.total_price>=d.min_purchase:
        cart.discount=d.discount
    else:
        cart.discount=0
    cart.save()
    return (cart)


def update_item(request , value):
    item_id=request.POST.get("item_id")
    item=get_object_or_404(CartItem , id=item_id)
    if value=="minus" :
        if item.quantity >1:
            item.quantity-=1
    elif value=="add":
        item.quantity+=1
    item.save()
    if value=="remove_form":
        item.delete()
    


def cart (request ):
    if request.method=="POST":
        value=request.POST.get("form")   
        update_item(request , value )   
    cart=get_cart(request)        
    return render(request , "cart.html" , {"cart":cart}) 


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




from django.shortcuts import render , redirect , get_object_or_404
from .forms import order_form
from django.urls import reverse
from django.core.mail import send_mail 
from shop.models import Cart  
from .models import orders , shipping_fee
# Create your views here. 



def orders_create (request): 
    if request.method=="POST":
        form=order_form(request.POST)
        if form.is_valid:
            order=form.save(commit=False) 
            cart = Cart.objects.get(session_key=request.session.session_key)
            add=shipping_fee.objects.get(divison=order.division)     
            request.session['order_data'] = {
                'name': order.name,
                'email': order.email,
                'phone_number':str( order.phone_number),
                'address': order.address,
                'division': order.division
            }
            request.session['cart_id'] = cart.id
            request.session['shipping_fee'] = float(add.fee) 

            return redirect('checkout')
    form =order_form()
    return render (request , "order_form.html" , {'form':form})




def checkout(request ): 
    order_data = request.session.get('order_data')
    shipping_fee = request.session.get('shipping_fee')
    cart_id=request.session.get('cart_id')
    cart=Cart.objects.get(id=cart_id)
    if request.method=="POST": 
        order=orders(**order_data)
        order.payment=cart.after_discount + shipping_fee 
        order.save()
        order.products.set([item.product for item in cart.items.all()])
        tracking_url = request.build_absolute_uri(reverse('track_order', kwargs={'token': str(order.tracking_token)})) 
        send_mail(
            subject='Track your order',
            message=f'Dear Customer your order is confirmed . You can track your order at: {tracking_url}', 
            from_email='niazbostore@example.com',
            recipient_list=[order.email]) 
        cart.delete() 
        return redirect ("shop")   
    else :  
        return render (request , 'checkout.html' , {'order':order_data , 'cart':cart, 'shipping_fee':shipping_fee})





def order_status(request , token):
    order=get_object_or_404(orders , tracking_token=token) 
    return render(request , 'order_status.html' , {"order":order} )
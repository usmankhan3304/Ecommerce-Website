from django.shortcuts import render,redirect
from products.models import *
# Create your views here.
from django.http import HttpResponseRedirect

from accounts.models import *

def get_products(request,slug):
    products = Products.objects.get(slug=slug)
    context={
        "products":products
    }
    if request.GET.get('size'):
        size=request.GET.get('size')
        price= products.get_product_price_by_size(size)
        print(price)
        
        context["selected_size"]=size
        context['updated_price']=price
       
    
    return render(request, 'product/products.html',context)

def add_to_cart(request,uid):
    variant=request.GET.get('variant')
    product=Products.objects.get(uid=uid)
    user=request.user#this is used to get the user information from the backend
    
    cart,_= Cart.objects.get_or_create(user=user,is_paid=False)
    cart_items= CartItem.objects.create(cart=cart, product=product)
    if variant:
        variant=request.GET.get('variant')
        size_variant=SizeVarient.objects.get(size_name=variant)
        cart_items.size_varient=size_variant
        cart_items.save()


    return redirect('/')

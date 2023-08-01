from django.shortcuts import render
from products.models import *
# Create your views here.
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
        print(context['selected_size'])
    
    return render(request, 'product/products.html',context)
    
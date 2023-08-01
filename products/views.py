from django.shortcuts import render
from products.models import *
# Create your views here.
def get_products(request,slug):
    products = Products.objects.get(slug=slug)
    for i in products.size_varient.all():
        print(i)
    context={
        "products":products
    }
    
    return render(request, 'product/products.html',context)
    
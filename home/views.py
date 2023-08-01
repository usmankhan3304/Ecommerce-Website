from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
# Create your views here.
def indeX(request):
    context={
        'products': Products.objects.all()
    }
    i= Products.objects.all()
    for i in i:
        print(i.product_name)
    
    return render (request,'home/index.html',context)
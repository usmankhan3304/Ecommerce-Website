from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
# Create your views here.
def indeX(request):
    context={
        'products': Products.objects.all()
    }
    
    
    return render (request,'home/index.html',context)
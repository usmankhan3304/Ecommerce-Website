from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def indeX(request):
    return render (request,'home/index.html')
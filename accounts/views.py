from django.shortcuts import render


from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request,"accounts/login_page.html")
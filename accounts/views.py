from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from accounts.models import *
# Create your views here.
def login_page(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email)
        print(password)
        
        user_obj=User.objects.filter(username=email)
        # print(user_obj[0].user_profile.is_email_verified)
        if not user_obj.exists():
            messages.warning(request,"user not found!")
            return HttpResponseRedirect(request.path_info)

        # if user_obj[0].user_profile.is_email_verified:
        #     pass
        user_obj=authenticate(username=email, password=password)
        if user_obj:
            login(request,user_obj)
            messages.success(request,"login successfully")
            redirect('/')
        else:
            messages.warning(request,"invalid credational")
            return HttpResponseRedirect(request.path_info)
    

    return render(request,"accounts/login_page.html")

def register_page(request):

    if request.method == "POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email)

        user=User.objects.filter(username=email)

        if user.exists():
            messages.error(request,"user already exists")
            return HttpResponseRedirect(request.path_info)
        
        user = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        user.set_password(password)
        user.save()
        messages.success(request,"An email has been sent")
        
        return HttpResponseRedirect(request.path_info)
        # return redirect('register_page')
    return render(request, "accounts/register.html")

def activate(request,email_token):
    try:
        user=UserProfile.objects.get(email_token = email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse("invalid Email token") 
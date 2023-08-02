from django.contrib import admin
from django.urls import path
from products.views import *
from accounts import views

urlpatterns = [
    path('login_page/',views.login_page, name="login_page"),
    path("register_page/",views.register_page, name="register_page"),
    path('activate/<email_token>/',views.activate,name="activate"),
    path("add-to-cart/<uid>/",add_to_cart , name="add_to_cart")
]
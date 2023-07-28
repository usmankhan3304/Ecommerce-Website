from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('login_page/',views.login_page, name="login_page")
]
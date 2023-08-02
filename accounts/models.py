
from django.db import models
from django.contrib.auth.models import User
from base.model import * 
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from base.emails import send_account_verification_email
from products.models import *
# Create your models here.
# Create your models here.
class UserProfile(BaseModel):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField( max_length=100,null=True,blank=True)
    
    profile_iamge=models.ImageField( upload_to='profile' )

    def cart_count(self):
        return CartItem.objects.filter(cart__is_paid=False,cart__user=self.user).count()

    def __str__(self):
        return self.user.first_name

class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='carts')
    is_paid=models.BooleanField(default=False)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_items")
    product=models.ForeignKey(Products, related_name="products", on_delete=models.SET_NULL, null=True)
    color_varient= models.ForeignKey(ColorVarient,  on_delete=models.SET_NULL,null=True)
    size_varient= models.ForeignKey(SizeVarient,  on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.product.product_name






@receiver(post_save, sender= User)
def send_email_token(sender,instance,created, **kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4().hex)
            print("email token is",email_token)
            print(instance)
            print(sender)
            print(created)
            UserProfile.objects.create(user=instance,email_token = email_token)#here we created the userprofile 
            email = instance.email#this email is from the
            #user model 
            send_account_verification_email(email,email_token)


    except Exception as e:
         print(e)
           
    
    

        


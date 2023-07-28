
from django.db import models
from django.contrib.auth.models import User
from base.model import * 
# Create your models here.
# Create your models here.
class UserProfile(BaseModel):
    user=models.OneToOneField(User,  on_delete=models.CASCADE, related_name="user_profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField( max_length=100,null=True,blank=True)
    profile_iamge=models.ImageField( upload_to='profile' )
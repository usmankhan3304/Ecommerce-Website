from django.db import models
from base.model import *
# Create your models here.
class Category(BaseModel):
    category_name=models.CharField(max_length=100, )
    slug= models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField( upload_to='categories' )

class Products(BaseModel):
    product_name=models.CharField( max_length=100)

    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products" )
    price=models.IntegerField()
    produtct_description= models.TextField()
    slug= models.SlugField(unique=True,null=True,blank=True)

class productsImages(BaseModel):
    product=models.ForeignKey(Products, on_delete=models.CASCADE,related_name="procuts_images")
    category_image=models.ImageField( upload_to='products_images' )

from django.db import models
from base.model import *
from django.utils.text import slugify
# Create your models here.
class Category(BaseModel):
    category_name=models.CharField(max_length=100, )
    slug= models.SlugField(unique=True,null=True,blank=True)
    category_image=models.ImageField( upload_to='categories')
    def save(self, *args, **kwargs):
       self.slug=slugify(self.category_name)
       super(Category, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.category_name
class ColorVarient(BaseModel):
    color_name=models.CharField( max_length=100)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.color_name
    
class SizeVarient(BaseModel):
    size_name=models.CharField( max_length=100)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.size_name
   
# class Size2(BaseModel):
#     size_name=models.CharField( max_length=50)
#     price=models.IntegerField()

class Products(BaseModel):
    product_name=models.CharField( max_length=100)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,related_name="products_category" )
    price=models.IntegerField()
    produtct_description= models.TextField()
    slug= models.SlugField(unique=True,null=True,blank=True)
    color_varient=models.ManyToManyField(ColorVarient,blank=True,related_name="color")
    size_varient=models.ManyToManyField(SizeVarient,blank=True,related_name="size")
    # size2=models.ManyToManyField(Size2)
    def save(self, *args, **kwargs):
       self.slug=slugify(self.product_name)
       super(Products, self).save(*args, **kwargs) # Call the real save() method
    def get_product_price_by_size(self,size):
        
        new_price=SizeVarient.objects.get(size_name = size)
        return self.price + new_price.price
        
    def __str__(self):
        return self.product_name
    
  
    
class productsImages(BaseModel):
   product=models.ForeignKey(Products, on_delete=models.CASCADE,related_name="products_images")
   image=models.ImageField( upload_to='products_images' )

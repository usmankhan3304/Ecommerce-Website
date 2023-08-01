from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class AdminCateogry(admin.ModelAdmin):
    list_display=['category_name','slug',]

# admin.site.register(Category,AdminCateogry) second way 

class ProductsImagesAdmin(admin.StackedInline):
    model= productsImages
# register the model through decorator..

@admin.register(Products)
class ProductsAdmin (admin.ModelAdmin): 
    list_display=['product_name','price','category',]
    inlines=[ProductsImagesAdmin]
    
# admin.site.register(,ProductsAdmin)
@admin.register(productsImages)
class Imageadmin(admin.ModelAdmin):
    pass
# admin.site.register(productsImages) 2nd way
@admin.register(ColorVarient)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display =['color_name','price']
#admin.site.register(Colorvarient)  

@admin.register(SizeVarient)
class SizeVarientAdmin(admin.ModelAdmin):
    list_display=['size_name','price']

# admin.site.register(SizeVarient)
# admin.site.register(Size2)
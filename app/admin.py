from re import search
from typing import OrderedDict
from unicodedata import name
from django.contrib import admin

from .models import Brands,products,Type_products
# Register your models here.

#databases
@admin.register(Type_products)
class TypesAdmin (admin.ModelAdmin):
    search_fields = ('id','name')
    list_display = ('id','name')
    ordering = ('id',)
    list_editable = ('name',)

@admin.register(Brands)
class BrandsAdmin (admin.ModelAdmin):
    search_fields = ('id','name')
    list_display = ('id','name')
    ordering = ('-id',)
    list_editable = ('name',)

@admin.register(products)
class ProductsAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    list_display = ('id','name','type_product','price','units')
    ordering =('id',) 
    list_display_links = ('name',)
    #list_filter = ('type_product',)

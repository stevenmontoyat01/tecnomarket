from django.shortcuts import render
from .models import products

# Create your views here.

def home (request):
    list_products = products.objects.all()
    data ={
        'products':list_products
    }
    return render(request,'app/home.html',data)

def contacto (request):
    return render(request,'app/contacto.html')

def galeria (request):
    return render(request,'app/Galeria.html')
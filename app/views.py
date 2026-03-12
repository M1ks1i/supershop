from itertools import product

from django.shortcuts import render

from app.models import Product, Category


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'products':products, 'categories':categories})

def category_list(request):
    pass

def product_list(request):
    pass

def product_detail(request):
    pass

def login_view(request):
    pass

def register_view(request):
    pass
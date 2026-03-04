from itertools import product

from django.shortcuts import render

from app.models import Product


def homepage(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', context={'products':products})

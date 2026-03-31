from itertools import product

from django.shortcuts import render, get_object_or_404

from app.models import Product, Category, Review


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'products':products, 'categories':categories})

def category_list(request):
    pass

def product_list(request):
    pass

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # rating = get_object_or_404(Review, pk=product_id)
    # rating = rating.rating * '4'
    review = product.review_set.all()
    return render(request, 'product_detail.html', context={'product': product, 'review':review})

def login_view(request):
    pass

def register_view(request):
    pass

def cart_detail(request):
    return render(request, 'cart.html')

def cart_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', context={'product': product})
from itertools import product

from django.shortcuts import render, get_object_or_404, redirect

from app.models import Product, Category, Review, Cart, Cartitem


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
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')



def get_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()
        session_key = request.session.session_key
    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def cart_add(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, pk=product_id)
    item, created = Cartitem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart_detail')

def cart_detail(request):
    # cart - все элементы из модели cart
    cart = get_cart(request)
    return render(request, 'cart.html', {'cart': cart})

def cart_remove(request, item_id):
    item = get_object_or_404(Cartitem, id = item_id)
    item.delete()
    return redirect('cart_detail')

def order_create(request):
    return render(request, 'cart.html')
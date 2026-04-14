"""
URL configuration for myprojectshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from itertools import product

from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

from app.views import cart_detail

admin.site.site_header = 'Мой интернет магазин'
admin.site.index_title = 'Добро пожаловать в панель управления'


urlpatterns = [
    # Главная
    path('', views.index, name='index'),

    # Список всех категорий
    path('categories/', views.category_list, name='category_list'),

    # Товары категории
    path('category/<int:category_id>/', views.product_list, name='product_list'),

    # Страница товара
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),

    # Авторизация
    path('login/', views.login_view, name='login'),

    # Регистрация
    path('register/', views.register_view, name='register'),

    # Админ-панель Django
    path('admin/', admin.site.urls),

    # Корзина
    path('cart_detail/', views.cart_detail, name='cart_detail' ),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart_remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('order_create/', views.order_create, name='order_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

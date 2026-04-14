from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=228, verbose_name='Название Товара')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Категория')
    discription = models.TextField(verbose_name='Описание Товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True,verbose_name='В налиичии ли товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(
        upload_to='productes/',
        blank=True,
        null=True,
        verbose_name='Photo'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField()

# class User(models.Model):


class CartItem(models.Model):
    # order_id = models.AutoField()
    # product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # quantity = models.IntegerField(default=1)
    # user = models.ForeignKey()
    session_key = models.CharField(max_length=40, unique=True, verbose_name='session_key')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Tovar')
    quantity = models.PositiveIntegerField(default=1,verbose_name='numbers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        verbose_name = 'cartes_element'
        verbose_name_plural = 'cart'
        unique_together = ['session_key','product']


    @property
    def total_price(self):
        # return sum(item.total_price for item in self.items.all())
        return self.product.price * self.quantity

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    def __str__(self):
        return f'{self.product.name} *{self.quantity}'

class Order(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_PAID = 'paid'
    STATUS_FAILED = 'failed'
    STATUS_DELIVERED ='delivered'
    STATUS_CHOICES = [
        (STATUS_PENDING, 'ожидает оплаты'),
        (STATUS_PAID, 'оплачено'),
        (STATUS_DELIVERED, 'доставлено'),
        (STATUS_FAILED, 'ошибка оплаты')
    ]

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,
        related_name = 'items',
        verbose_name = 'order'
    )
    product = models.ForeignKey(
        Product,
        on_delete = models.SET_NULL(),
        null = True,
        related_name = 'cart_items'
    )

    product_name = models.CharField(max_length=322)
    product_price = models.DecimalField(max_digits=10,decimal_places=2,)
    quantity = models.PositiveIntegerField(default = 1)

    class Meta:
        verbose_name = 'order_pos'
        verbose_name_plural = 'orders_poses'

    @property
    def total_price(self):
        return self.product_price * self.quantity

    def __str__(self):
        return f'{self.product.name} * {self.quantity}'
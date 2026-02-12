from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=228, verbose_name='Название Товара')
    discription = models.TextField(verbose_name='Описание Товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    in_stock = models.BooleanField(default=True,verbose_name='В налиичии ли товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

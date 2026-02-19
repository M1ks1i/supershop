from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','in_stock','created_at','category','colored']
    list_filter = ['in_stock','created_at','category']
    autocomplete_fields = ['category']
    search_fields =  ['discription','name']
    readonly_fields = ['created_at','colored']
    list_editable = ['price','in_stock']
    list_per_page = 24
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    fieldsets = (
        (
            'Main Информейшн',
            {'fields':('name','discription')}
        ),
        (
            'Цена и Наличие',
            {'fields':('price','in_stock')}
        ),
        (
            'Дополнительная Information',
            {
                'fields':('created_at',),
                'classes':('collapse',)
            }
        )
    )

    def colored(self,obj):
        if obj.in_stock :
            return format_html('<span>✅В наличии✅</span>')
        return format_html('<span>❌Нет в наличии❌</span>')
    colored.short_description = 'status'

    actions = ['make_in_stock','make_out_off_stock']

    def make_in_stock(self, request, query_set):
        query_set.update(in_stock = True)
        self.message_user(request,"Товар обозначен 'В наличии'" )
    make_in_stock.short_description = 'В наличии'

    def make_out_off_stock(self, request, query_set):
        query_set.update(in_stock = False)
        self.message_user(request,"Товар обозначен 'Не в наличии'" )
    make_out_off_stock.short_description = 'Не в наличии'

admin.site.site_title = 'Админ-панель'
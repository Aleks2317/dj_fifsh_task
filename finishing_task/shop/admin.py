from django.contrib import admin
from .models import Clients, Product, Order


@admin.action(description="Удалить address")
def reset_address(modeladmin, request, queryset):
    queryset.update(address='')


class ClientsAdmin(admin.ModelAdmin):
    list_display = ['date_registration', 'name', 'email', 'phone', 'address']
    ordering = ['-date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name (пример: Inkoli)'
    actions = [reset_address]


@admin.action(description="Онульровать total_price")
def reset_total_price(modeladmin, request, queryset):
    queryset.update(total_price=0)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'total_price', 'customer', 'products']
    ordering = ['-date_ordered']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по полю date_ordered (пример: 2024-02-23)'
    actions = [reset_total_price]


@admin.action(description="Онульровать количество продута")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'date_registration']
    ordering = ['-date_registration']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name'
    actions = [reset_quantity]


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

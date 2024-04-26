from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Clients: {self.name}, email: {self.email}, date: {self.date_registration}'


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    price = models.DecimalField(default=999999.99, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date_registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}, quantity: {self.quantity}'


class Order(models.Model):
    customer = models.ForeignKey(Clients, on_delete=models.CASCADE)  # при удалении пользователя удаляться и все его заказы
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)  # автоматическое добавление даты при создании заказа

    def __str__(self):
        return f'Order: {self.date_ordered}, price: {self.total_price}, quantity: {self.customer}'



import decimal

from django.core.management.base import BaseCommand
from shop.models import Product
from random import uniform, randint

class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count new produkt')
        parser.add_argument('name_product', type=str, help='name_product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        name_product = kwargs.get('name_product')
        for i in range(count):

            product = Product(name=f'{name_product}-{i}',
                              description=f'{name_product} wary well',
                              price=uniform(0.01, 999.99),
                              quantity=randint(1, 1000),
                              )

            product.save()
            self.stdout.write(f'{product}')

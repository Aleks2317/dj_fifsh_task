import logging
from django.shortcuts import render
from .models import Product
from .forms import ProductUpdateForm

logger = logging.getLogger(__name__)


# def shop(request):
#     logger.info(f'сработало представление index ')
#     content = {'dz': [s for s in 'Задание №6 Доработаем задачу про клиентов, '
#                                  'заказы и товары из прошлого семинара. '
#                                  'Создайте форму для редактирования товаров в базе'
#                                  'данных. Измените модель продукта, добавьте поле для'
#                                  ' хранения фотографии продукта. Создайте форму, которая'
#                                  ' позволит сохранять фото. http://127.0.0.1:8000/shop/productupgrete/'.split('.')]}
#     return render(request, 'shop/index.html', content)


def shop(request):
    if request.method == 'POST':
        logger.info('********** start product_upgrete')
        form = ProductUpdateForm(request.POST, request.FILES)
        logger.info(f'********** ProductUpdateForm(request.POST, request.FILES) : {form = }')
        message = 'Ошибка в данных'
        if form.is_valid():
            logger.info('********** work form.is_valid():')
            product = Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                date_registration=form.cleaned_data['date_registration'].__str__(),
            )
            product.save()
            message = 'Продукт сохранен сохранён'
    else:
        form = ProductUpdateForm()
        message = 'Заполните форму'
    return render(request, 'shop/product_create.html', {'form': form, 'message': message})


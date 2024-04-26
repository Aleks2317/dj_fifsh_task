import logging
from django.http import HttpResponse
from django.shortcuts import render


logger = logging.getLogger(__name__)

text = '''На GeekBrains я прошел следующие видео курсы:

Введение в программирование (лекции)
Введение в программирование (семинары)
Введение в контроль версий (лекции)
Введение в контроль версий (семинары)
Знакомство с веб-технологиями (лекции)
Знакомство с веб-технологиями (семинары)
Знакомство с языком Python (лекции)
Знакомство с языком Python (семинары)
Погружение в Python (лекции)
Погружение в Python (семинары)
Фреймворки Flask и FastAPI (лекции)
Фреймворки Flask и FastAPI (семинары)
Фреймворк Django (лекции)
Фреймворк Django (семинары) (нужно сдать последнее задание)

И еще предстоит:
Контроль версий углублённо (GIT) (лекции)
Контроль версий углублённо (GIT) (семинары)
Базы данных и SQL (лекции)
Базы данных и SQL (семинары)
Итоговая аттестация
'''


def about_me(request):
    logger.info('ABOUT page accessed')

    logger.info(f'{text = }')
    context = {
        'about': text,
    }
    return render(request, "about_me/about_me.html", context)


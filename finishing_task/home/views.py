import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def home(request):
    logger.info('home page accessed')
    context = {"title": "HOME"}
    return render(request, 'home/home.html', context)


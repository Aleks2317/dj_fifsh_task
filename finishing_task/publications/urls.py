from django.urls import path
from .views import publications
from .views import post_full
from .views import info_post
from .views import author_form
from .views import post_form
#

urlpatterns = [
    path('', publications, name='publications'),
    path('post/<int:post_id>/', post_full, name='post_full'),
    path('info_post/<int:post_id>/', info_post, name='info_post'),
    path('authorcreate/', author_form, name='author_form'),
    path('postcreate/', post_form, name='post_form')
]


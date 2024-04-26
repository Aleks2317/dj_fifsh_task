import logging
from django.shortcuts import render, get_object_or_404
from .models import Author, Post, Comment
from .forms import NewAuthorForm, NewPostForm, AuthorForm


logger = logging.getLogger(__name__)


# Главная страница
def publications(request):
    logger.info(f'сработало представление index ')

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            # return author_posts(request, int(author))
            author = get_object_or_404(Author, pk=int(form.cleaned_data['name']))
            posts = Post.objects.filter(author=author).order_by('id')
            return render(request, 'publications/author_posts.html', {'author': author, 'posts': posts})
    else:
        form = AuthorForm()
        return render(request, 'publications/index.html', {'form': form})


def post_full(request, post_id):
    logger.info(f'сработало представление post_full')
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'publications/post_full.html', {'post': post})


def info_post(request, post_id):
    logger.info(f'сработало представление info_post')
    posts = get_object_or_404(Post, pk=post_id)
    posts.count_of_views += 1
    posts.save()
    comment = Comment.objects.filter(post_id=post_id)
    content = {'posts': posts, 'comment': comment}
    return render(request, 'publications/info_post.html', content)


def author_form(request):
    if request.method == 'POST':
        logger.info('**********start author_form_create_db')
        form = NewAuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            biography = form.cleaned_data['beography']
            date_of_birth = form.cleaned_data['date_of_birth']
            author = Author(
                name=name,
                lastname=lastname,
                email=email,
                biography=biography,
                date_of_birth=date_of_birth.__str__(),
            )
            author.save()
            message = 'Автор сохранён'
    else:
        form = NewAuthorForm()
        message = 'Заполните форму'
    return render(request, 'publications/author_create_form.html', {'form': form, 'message': message})


def post_form(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            data_publication = form.cleaned_data['data_publication']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            flag_publicaton = form.cleaned_data['flag_publicaton']
            logger.info(f'{title = } {content = }'
                        f'{data_publication = } {author = } {category = } {flag_publicaton = }')
            post = Post(
                title=title,
                content=content,
                data_publication=data_publication,
                author=Author.objects.filter(pk=author).first(),
                category=category,
                flag_publicaton=flag_publicaton
            )
            post.save()
            message = 'Статья сохранена'
    else:
        form = NewPostForm()
        message = 'Создайте статью'
        title = 'Post create'
    return render(request, 'publications/post_create_form.html', {'form': form, 'message': message, 'title': title})


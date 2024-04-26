from django.db import models


class Author(models.Model):
    """ Модель - Автор. """
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)

    # определим полное имя как свойства и при необходимости вызовем его
    @property
    def fullname(self):
        return f'{self.name} {self.lastname}'

    def __str__(self):
        return f'Model - Author Name: {self.name = }, {self.lastname = }, email: {self.email = }, ' \
               f'{self.biography = },{self.date_of_birth = }'


class Post(models.Model):
    """ Модель - Статья. """
    title = models.CharField(max_length=200)
    content = models.TextField()
    data_publication = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_of_views = models.IntegerField(default=0)
    flag_publicaton = models.BooleanField(default=False)

    def __str__(self):
        return f'Post is {self.title = }, {self.content = },' \
               f' {self.data_publication = }, {self.author = }, ' \
               f'{self.category = }, {self.count_of_views = }, {self.flag_publicaton = }'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'


class Comment(models.Model):
    """ Модель - Комментарий """
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    data_comment = models.DateTimeField(auto_now_add=True)
    data_comment_remuve = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment is {self.author = }, {self.post = }, {self.data_comment = }, {self.data_comment_remuve = }'


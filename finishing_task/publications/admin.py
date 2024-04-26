from django.contrib import admin
from .models import Author, Post, Comment


@admin.action(description="Удалить биографию")
def reset_bmography(modeladmin, request, queryset):
    queryset.update(bmography='')


@admin.action(description="поменять флаг публикации на True")
def reset_flag_publicaton(modeladmin, request, queryset):
    queryset.update(flag_publicaton=True)


@admin.action(description="Удалить post")
def reset_post(modeladmin, request, queryset):
    queryset.update(post='')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'date_of_birth', 'biography']
    ordering = ['name', '-date_of_birth']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name (пример: Author_1)'
    actions = [reset_bmography]


class PostAdmin(admin.ModelAdmin):
    list_display = ['data_publication', 'title', 'category', 'flag_publicaton']
    ordering = ['flag_publicaton', '-data_publication']
    search_fields = ['title']
    search_help_text = 'Поиск по полю title (пример: Title-5)'
    actions = [reset_flag_publicaton]


class CommentAdmin(admin.ModelAdmin):
    list_display = ['data_comment_remuve', 'data_comment_remuve', 'comment', 'post']
    ordering = ['-data_comment_remuve']
    search_fields = ['data_comment']
    search_help_text = 'Поиск по полю data_comment (пример: 2024-04-15)'
    actions = [reset_post]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


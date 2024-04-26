from django import forms
from .models import Author
import datetime


class NewAuthorForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя автора',
    }))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите фамилию автора',
    }))
    date_of_birth = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'user@mail.ru'
    }))
    biography = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))


class NewPostForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Название статьи',
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'}))
    data_publication = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    author = forms.ChoiceField(choices=[(a.id, a.name) for a in Author.objects.all()])
    category = forms.ChoiceField(choices=[
        ('sports', 'Спорт'),
        ('cooking', 'Рецепты'),
        ('art', 'Искусство'),
        ('fantasy', 'Фэнтези'),
        ('documentation', 'Документация'),
        ('humor', 'Юмор')
        ])
    flag_publicaton = forms.BooleanField(label='Опубликовать', required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input'}))


class AuthorForm(forms.Form):
    name = forms.ChoiceField(label='Author', choices=[(a.id, a.name) for a in Author.objects.all()])

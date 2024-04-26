from django import forms
from .models import Product
import datetime


class ProductUpdateForm(forms.Form):

    # image = forms.ImageField(required=False,  label='Загрузить изображение')

    name = forms.ChoiceField(choices=[(a.id, a.name) for a in Product.objects.all()])
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))
    category = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    price = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    quantity = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    date_registration = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    rating = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))


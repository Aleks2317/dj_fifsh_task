from django.db import models


class Coin(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=15)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f'Name: {self.name}'


class Cube(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=15)
    result = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}'


class Number(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=15)
    result = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}'

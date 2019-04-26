from django.db import models


class Drink (models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)
    snacks = models.ManyToManyField('Snack', related_name='drinks')

    def __str__(self):
        return self.name


class Snack (models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=1000)

    def __str__(self):
        return self.name



from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ManyToManyField('Author', related_name='books')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

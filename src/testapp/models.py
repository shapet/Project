from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(
        verbose_name="Название жанра",
        max_length = 100
    ) 
    description = models.TextField(
        verbose_name="Описание жанра",
        null= True,
        blank= True
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        verbose_name="Название Книги",
        max_length = 200
        )

    genre = models.ForeignKey(
        Genre, 
        on_delete=models.PROTECT,
        verbose_name="Жанр Книги")
        
    description = models.TextField(
        verbose_name="Описание книги ",
        null= True,
        blank= True
    )
    def __str__(self):
        return self.name

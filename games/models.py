from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ManyToManyField("Genre", related_name="genres")
    year = models.IntegerField()
    rate = models.DecimalField(decimal_places=1, max_digits=10)


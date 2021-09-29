from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=23)
    slug = models.SlugField(unique = True)
    def __str__(self):
        return self.name;



class Company(models.Model):
    name = models.CharField(max_length=23)
    slug = models.SlugField(unique = True)
    def __str__(self):
        return self.name;



class Game(models.Model):
    title = models.CharField(max_length=52)
    slug = models.SlugField(unique = True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)
    ageIndication = models.PositiveIntegerField()

    def __str__(self):
        return self.title;
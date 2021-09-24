from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=23)



class Company(models.Model):
    name = models.CharField(max_length=23)



class Game(models.Model):
    title = models.CharField(max_length=23)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    ageIndication = models.PositiveIntegerField()
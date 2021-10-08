from django.db import models
from django.urls import reverse
from MyGameList.settings import DEFAULT_IMAGE;


class Genre(models.Model):
    name = models.CharField(max_length=23)
    description = models.TextField(default="")
    image = models.URLField(default=DEFAULT_IMAGE)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
          return reverse("Blog:genre_detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("name",)



class Company(models.Model):
    name = models.CharField(max_length=26)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse("Blog:company_detail", kwargs={"slug": self.slug})




class Game(models.Model):
    title = models.CharField(max_length=52)
    slug = models.SlugField(unique = True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)
    ageIndication = models.PositiveIntegerField()
    synopsis = models.TextField(default="none")
    imageUrl = models.URLField(default=DEFAULT_IMAGE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
          return reverse("Blog:game_detail", kwargs={"slug": self.slug})

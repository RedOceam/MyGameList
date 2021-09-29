from django.views.generic import ListView, DetailView
from . import models


class GameListView(ListView):
       model = models.Game

class GameDetailView(DetailView):
       model = models.Game


class GenreListView(ListView):
       model = models.Genre

class GenreDetailView(ListView):
       model = models.Genre


class CompanyListView(ListView):
       model = models.Company

class CompanyDetailView(ListView):
       model = models.Company
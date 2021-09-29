from django.urls import path
from . import views

app_name = "Blog"

urlpatterns = [
    path("game", views.GameListView.as_view(), name = "list"),
    path("game/<slug:slug>/", views.GameDetailView.as_view(), name = "detail"),

    path("genre", views.GenreListView.as_view(), name = "list"),
    path("genre/<slug:slug>/", views.GenreDetailView.as_view(), name = "detail"),

    path("company", views.CompanyListView.as_view(), name = "list"),
    path("company/<slug:slug>/", views.CompanyDetailView.as_view(), name = "detail"),
]
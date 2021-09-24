from django.contrib import admin
from Blog import models

@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )
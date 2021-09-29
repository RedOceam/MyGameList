from django.contrib import admin
from Blog import models

@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "company", )
    prepopulated_fields = {"slug": ("title",)}

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}

@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}
from django.contrib import admin

# Register your models here.
from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
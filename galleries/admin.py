from django.contrib import admin
from .models import Gallery, Photo
# Register your models here.

class PhotoInline(admin.StackedInline):
    model=Photo
    extra = 3


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin): pass
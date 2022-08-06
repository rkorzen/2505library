from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.author})"
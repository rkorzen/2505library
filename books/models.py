from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey('authors.Author', on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.author})"

    def a_first_name(self):
        return self.author.first_name
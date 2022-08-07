from django.db import models

# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='auhtors', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Bio(models.Model):
    author = models.OneToOneField('authors.Author', on_delete=models.CASCADE)
    bio = models.TextField()
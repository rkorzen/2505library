from django.db import models

# Create your models here.


class Gallery(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='galleries/')
    description = models.TextField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.title

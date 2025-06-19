from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()

    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return f"({self.name}): {self.message}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()

    def __str__(self):
        return f"({self.title}): {self.author}"

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"({self.title}): {self.author}"
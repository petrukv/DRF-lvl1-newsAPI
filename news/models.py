from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    body = models.TextField()
    location = models.CharField(max_length=50)
    publication = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} {self.title}"
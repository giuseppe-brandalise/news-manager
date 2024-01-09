from django.db import models
from news.validators import title_validator


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200, validators=[title_validator]
    )
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()
    image = models.ImageField(upload_to='img/', blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

from django.db import models
from account.models import User
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)


class Article(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, models.SET_NULL, null=True, default=None)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now())
    status = models.CharField(
        max_length=1,
        choices=[('p', 'publish'), ('d', 'draft')],
        default='d',
        blank=False,
    )

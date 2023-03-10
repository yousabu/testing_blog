from django.urls import reverse
from email.policy import default
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        # return reverse('article-details', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="default code")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding') 

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article-details', args=(str(self.id)))
        return reverse('home')

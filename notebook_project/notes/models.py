from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name='notes')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='notes',
                               blank=True, null=True)

    def __str__(self):
        return self.title
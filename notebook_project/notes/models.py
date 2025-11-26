from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=20, help_text="筆記標題")
    content = models.TextField(max_length=200, help_text="內容")
    created_at = models.DateTimeField(auto_now=True, help_text="建立時間")
    category = models.ForeignKey(Category, 
                                 on_delete=models.CASCADE, 
                                 related_name='notes',
                                 help_text="分類")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='notes',
                               blank=True, null=True,
                               help_text="作者")

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
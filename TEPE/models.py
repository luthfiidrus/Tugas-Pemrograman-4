from django.db import models

# Create your models here.

class Comment(models.Model):
    penulis = models.CharField(max_length=20, default="Unknown")
    komen = models.TextField()
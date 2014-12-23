from django.db import models

# Create your models here.

class Memo(models.Model):
    title = models.TextField()

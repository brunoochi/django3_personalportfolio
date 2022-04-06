from django.db import models

# Project blog
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images')
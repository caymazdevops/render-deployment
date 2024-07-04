from django.db import models
from django.contrib.auth.models import User

class Sport(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class SportImage(models.Model):
    sport = models.ForeignKey(Sport, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sports/')


from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    
 
# class Removie(models.Model):
#     removie_genre = models.CharField(max_length=100)

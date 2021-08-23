from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    pass


class Post(models.Model):

    title = models.CharField(max_length=25)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

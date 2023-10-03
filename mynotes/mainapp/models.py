from django.contrib.auth.models import AbstractUser
from django.db import models


class Notes(models.Model):
    Text = models.TextField()


class User(AbstractUser):
    Note = models.ForeignKey(Notes, on_delete=models.CASCADE)



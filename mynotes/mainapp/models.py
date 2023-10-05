from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    def create_user(self, username, first_name, last_name, email, password1):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password1)
        self.save()


class Notes(models.Model):
    Text = models.TextField()
    User = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    def create_note(self, text, user):
        self.Text = text
        self.User = user
        self.save()








from django.db import models
from django.contrib import auth
import uuid

auth.signals.user_logged_in.disconnect(auth.models.update_last_login)

class User(models.Model):
    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=100, default=uuid.uuid4)

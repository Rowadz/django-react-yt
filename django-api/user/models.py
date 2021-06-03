from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(blank=True, unique=True)

    REQUIRED_FIELDS = ['username']

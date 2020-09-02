from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from webauth.managers import UserManager


class Employee(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, verbose_name=_('email address'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

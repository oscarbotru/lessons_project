from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    phone = models.CharField(max_length=25, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватарка')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


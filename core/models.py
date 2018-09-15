from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        abstract = False
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

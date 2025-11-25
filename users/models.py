from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_num = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    tg_name = models.CharField(
        max_length=50, verbose_name="Телеграм ник", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", null=True, blank=True
    )
    token = models.CharField(
        max_length=100, verbose_name="Токен", blank=True, null=True
    )
    owner = models.ForeignKey

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

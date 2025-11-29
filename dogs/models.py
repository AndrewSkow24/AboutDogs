from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Breed(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", help_text="Введите название породы"
    )
    description = models.TextField(
        verbose_name="Описание породы", help_text="Опишите породу "
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


# Create your models here.
class Dog(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Имя", help_text="Введите кличку собаки"
    )
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        related_name="dogs",
        verbose_name="порода",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="dogs/photo", verbose_name="Фото", blank=True, null=True
    )
    date_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите дату рождения",
        blank=True,
        null=True,
    )
    view_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", default=0
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]
        permissions = [
            ("can_edit_breed", "Может менять породу"),
            ("can_edit_description", "Может менять описание"),
        ]

    def __str__(self):
        return self.name


class Parent(models.Model):
    dog = models.ForeignKey(
        Dog,
        related_name="parents",
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Собака",
    )
    name = models.CharField(
        max_length=255, verbose_name="Имя", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        related_name="parents_dog",
        verbose_name="порода",
        help_text="Введите породу собаки",
        blank=True,
        null=True,
    )
    year_born = models.PositiveIntegerField(
        verbose_name="Год рождения",
        help_text="Укажите год рождения",
        default=0,
        **NULLABLE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Предок"
        verbose_name_plural = "Предки"

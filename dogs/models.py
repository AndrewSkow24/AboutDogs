from django.db import models


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

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
        ordering = ["breed", "name"]

    def __str__(self):
        return self.name

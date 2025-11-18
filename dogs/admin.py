from django.contrib import admin
from .models import Dog, Breed


# Register your models here.
@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "breed"]
    list_filter = [
        "breed",
    ]
    search_fields = ["name"]

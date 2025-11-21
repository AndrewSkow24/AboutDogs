from django.urls import path
from . import views

urlpatterns = [
    path("", views.dogs_list, name="dogs_list"),
    path("dogs/<int:pk>/", views.dogs_details, name="dogs_detail"),
]

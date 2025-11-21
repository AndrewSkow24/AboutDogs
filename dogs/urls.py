from django.urls import path
from . import views

urlpatterns = [
    # Create
    path("dogs/create/", views.DogCreateView.as_view(), name="dog_create"),
    # Read
    path("", views.DogListView.as_view(), name="dog_list"),
    path("dogs/<int:pk>/", views.DogDetailView.as_view(), name="dog_detail"),
    # Update
    path("dogs/<int:pk>/update/", views.DogUpdateView.as_view(), name="dog_update"),
    # Delete
    path("dogs/<int:pk>/delete/", views.DogDeleteView.as_view(), name="dog_delete"),
]

from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Dog
from .forms import DogForm


class DogListView(ListView):
    model = Dog
    # шаблон по правилам должен быть app_name/<model_name>_<action>


class DogDetailView(DetailView):
    model = Dog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class DogCreateView(CreateView):
    model = Dog
    # fields = ("name", "breed", "date_birth", "photo")
    form_class = DogForm
    success_url = reverse_lazy("dog_list")


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm
    success_url = reverse_lazy("dog_list")

    def get_success_url(self):
        return reverse("dog_detail", args=[self.kwargs.get("pk")])


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy("dog_list")

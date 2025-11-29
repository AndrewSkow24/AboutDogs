from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms.models import inlineformset_factory
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Dog, Parent
from .forms import DogForm, ParentForm, DogModeratorForm
from users.models import User


class DogListView(ListView):
    model = Dog
    # шаблон по правилам должен быть app_name/<model_name>_<action>


class DogDetailView(LoginRequiredMixin, DetailView):
    model = Dog

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner or self.request.user.is_staff:
            self.object.view_counter += 1
            self.object.save()
            return self.object
        else:
            raise PermissionDenied


class DogCreateView(LoginRequiredMixin, CreateView):
    model = Dog
    # fields = ("name", "breed", "date_birth", "photo")
    form_class = DogForm
    success_url = reverse_lazy("dog_list")

    def form_valid(self, form):
        dog = form.save()
        dog.owner = self.request.user
        dog.save()
        return super().form_valid(form)

        return super().form_valid(form)


class DogUpdateView(LoginRequiredMixin, UpdateView):
    model = Dog
    form_class = DogForm
    success_url = reverse_lazy("dog_list")

    def get_success_url(self):
        return reverse("dog_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        DogFormset = inlineformset_factory(Dog, Parent, ParentForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = DogFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = DogFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return DogForm
        if user.has_perm("dogs.can_edit_breed") and user.has_perm(
            "dogs.eidt_description"
        ):
            return DogModeratorForm
        else:
            raise PermissionDenied


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy("dog_list")

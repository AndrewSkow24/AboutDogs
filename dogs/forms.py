from django.utils import timezone

from django import forms
from django.forms import BooleanField

from .models import Dog, Parent


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class DogForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ["view_counter", "owner"]


class ParentForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = "__all__"

    def clean_year_born(self):
        year_born = self.cleaned_data["year_born"]
        print(year_born)

        current_year = timezone.now().year
        print("Текущий год:", current_year)

        timedelta = current_year - year_born
        print("Разность", timedelta)
        if timedelta >= 100:
            raise forms.ValidationError("Слишком старая собака")
        return year_born

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password1",
            "password2",
        ]


class UserProfileView(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "phone_num", "tg_name", "avatar")

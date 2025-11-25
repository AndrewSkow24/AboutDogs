from django.urls import path
from .apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", views.UserRegisterView.as_view(), name="registration"),
    path("profile/", views.UserProfileView.as_view(), name="profile"),
    path(
        "email_confirm/<str:token>/",
        views.email_verification,
        name="email_confirm",
    ),
]

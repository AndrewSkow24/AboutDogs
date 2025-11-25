from django.shortcuts import get_object_or_404, redirect

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .models import User
from .forms import UserRegistrationForm, UserProfileView
import secrets


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        # генерируется токен, токен отправляется на почту,
        # при верном токене пользователь становится активным
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email_confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке, чтобы подтвердить почту  {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileView
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from forms import RegisterForm


class Login(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    pass


class UserRegister(CreateView):
    model = get_user_model()
    template_name = 'core/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('core:profile')


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

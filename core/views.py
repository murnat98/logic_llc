from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class Login(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    pass


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

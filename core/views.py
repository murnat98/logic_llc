from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class Login(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'core/profile.html'

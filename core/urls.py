from django.urls import path

from views import Login, UserProfile

app_name = 'core'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', UserProfile.as_view(), name='profile'),
]

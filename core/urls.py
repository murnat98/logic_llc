from django.urls import path

from views import Login, UserProfile, Logout, UserRegister

app_name = 'core'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', UserProfile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),
]

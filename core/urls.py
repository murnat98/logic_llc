from django.urls import path

from views import Login, UserProfile, Logout

app_name = 'core'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('', UserProfile.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name='logout'),
]

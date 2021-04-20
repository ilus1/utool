from django.urls import path
from .views import profile_view

app_name = 'users'

urlpatterns = [
    path('profile/', profile_view, name='account_profile'),
]
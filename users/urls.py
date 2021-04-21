from django.urls import path
from .views import ProfilePageView

app_name = 'users'

urlpatterns = [
    path('', ProfilePageView.as_view(), name='profile'),
]
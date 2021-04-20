from django.views.generic import TemplateView
from django.shortcuts import render

def profile_view(request):
    return render(request, 'templates/account/profile.html')
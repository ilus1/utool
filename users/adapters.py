from django.urls.base import reverse_lazy
from allauth.account.adapter import DefaultAccountAdapter
from .models import MyUserModel
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.name = data["name"]
        user.surname = data["surname"]
        user.email = data["email"]
        user.cpf = data['cpf']
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user.save()
        return user


""" 
        try:
            MyUserModel.objects.get(cpf=user.cpf)
            messages.error(request, 'CPF já foi cadastrado.')
            redirect(reverse_lazy('pages:list'))
        except ObjectDoesNotExist:
            pass """
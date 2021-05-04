from django import forms
from django.db import models
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator
from django.contrib import messages

from .models import MyUserModel
from tools.models import Tool
from .utils import validate_cpf


class UserChangeForm(UserChangeForm):
    cpf = forms.CharField(validators=[validate_cpf])
    name = forms.CharField(label="Nome", max_length='50', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z]*', message='Nome deve conter apenas letras, numeros e espacos.', code='erro')])
    surname = forms.CharField(label="Sobrenome", max_length='700', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Sobrenome deve conter apenas letras, numeros e espacos.', code='erro')])
    tools = models.ForeignKey(Tool, on_delete=models.CASCADE)

    class Meta(UserChangeForm.Meta):
        model = MyUserModel
    
    def save(self, request):
        user = super(UserChangeForm, self).save(request)
        user.cpf = self.cleaned_data['cpf']
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.save()
        return user



class UserCreationForm(SignupForm):
    cpf = forms.CharField(validators=[validate_cpf])
    name = forms.CharField(label="Nome", max_length='50', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z]*', message='Nome deve conter apenas letras, numeros e espacos.', code='erro')])
    surname = forms.CharField(label="Sobrenome", max_length='700', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Sobrenome deve conter apenas letras, numeros e espacos.', code='erro')])


    class Meta(UserCreationForm.Meta):
        model = MyUserModel
    
    def save(self, request):
        user = super(UserCreationForm, self).save(request)
        user.cpf = self.cleaned_data['cpf']
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.save()
        messages.success(request, 'Você foi cadastrado com sucesso!')
        return user

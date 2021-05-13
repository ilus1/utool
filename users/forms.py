from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import SignupForm
from django.core.validators import RegexValidator
from django.contrib import messages

from .models import MyUserModel
from .utils import validate_cpf


class UserCreationForm(SignupForm):
    cpf = forms.CharField(
        max_length=11, 
        help_text='Deverá conter apenas números', 
        validators=[validate_cpf],
        label="CPF"
    )
    name = forms.CharField(
        label="Nome", 
        max_length='50', 
        validators=[RegexValidator(regex='^[a-zA-Z]{3}[a-zA-Z]*$', 
            message='Nome deve conter pelo menos 3 caracteres, apenas letras.', 
            code='erro')]
    )
    surname = forms.CharField(
        label="Sobrenome", 
        max_length='700', 
        validators=[RegexValidator(regex='^[a-zA-Z]{3}[a-zA-Z]*$', 
            message='Sobrenome deve conter apenas letras e espaços.', 
            code='erro')]
    )

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

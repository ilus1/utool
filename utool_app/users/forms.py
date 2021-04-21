from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms as form
from allauth.account.forms import SignupForm
from .models import MyUser
from .utils import validate_cpf
from django.core.validators import RegexValidator

class UserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = MyUser

class UserCreationForm(SignupForm):
    cpf = form.CharField(validators=[validate_cpf])
    nome = form.CharField(max_length='50', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z]*', message='Nome deve conter apenas letras, numeros e espacos.', code='erro')])
    sobrenome = form.CharField(max_length='700', validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Sobrenome deve conter apenas letras, numeros e espacos.', code='erro')])

    class Meta(UserChangeForm.Meta):
        model = MyUser
    
    def save(self, request):
        user = super(UserCreationForm, self).save(request)
        user.cpf = self.cleaned_data['cpf']
        user.nome = self.cleaned_data['nome']
        user.sobrenome = self.cleaned_data['sobrenome']
        user.save()
        return user
from django.contrib.auth.models import AbstractUser
from .utils import validate_cpf
from django.db.models import CharField
from django.core.validators import RegexValidator
from django.db import models


class MyUser(AbstractUser):
    nome = models.CharField(max_length=50, validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Nome deve conter apenas letras e numeros.', code='erro')])
    sobrenome = models.CharField(max_length=700, validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Sobrenome deve conter apenas letras, numeros e espacos.', code='erro')])
    cpf = models.CharField(max_length=11, help_text='Devera conter apenas numeros', unique=True, validators=[validate_cpf])
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=5, validators=[RegexValidator(regex='[0-9]+', message='Deve conter apenas numeros maiores que 0', code='erro')])
    complemento = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=2,
        default='DF',
    )
    
    first_name = False
    last_name = False
    REQUIRED_FIELDS = []
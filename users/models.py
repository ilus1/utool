from django.contrib.auth.models import AbstractUser
from .utils import validate_cpf
from django.db import models
from django.core.validators import RegexValidator
from tools.models import Tool


class MyUserModel(AbstractUser):
    name = models.CharField(verbose_name="nome", max_length=50, validators=[RegexValidator(regex='[0-9a-zA-Z]{3}[0-9a-zA-Z]*', message='Nome deve conter apenas letras e numeros.', code='erro')])
    surname = models.CharField(verbose_name="sobrenome", max_length=700, validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', message='Sobrenome deve conter apenas letras, numeros e espacos.', code='erro')])
    cpf = models.CharField(max_length=11, help_text='Devera conter apenas numeros', unique=True, validators=[validate_cpf])
    adress = models.CharField(verbose_name="endereco", max_length=50)
    number = models.CharField(verbose_name="numero", max_length=5, validators=[RegexValidator(regex='[0-9]+', message='Deve conter apenas numeros maiores que 0', code='erro')])
    complement = models.CharField(verbose_name="complemento", max_length=30)
    district = models.CharField(verbose_name="bairro", max_length=30)
    zip_code = models.CharField(verbose_name="cep", max_length=8)
    city = models.CharField(verbose_name="cidade", max_length=30)
    state = models.CharField(
        verbose_name="estado",
        max_length=2,
        default='DF',
    )
    
    first_name = False
    last_name = False
    REQUIRED_FIELDS = []
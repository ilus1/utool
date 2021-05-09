from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utils import validate_cpf

class MyUserModel(AbstractUser):
    name = models.CharField(
        verbose_name="nome", 
        max_length=50, 
        validators=[RegexValidator(regex='[0-9a-zA-Z]{3}[0-9a-zA-Z]*', 
        message='Nome deve conter apenas letras e numeros.', 
        code='erro')]
    )
    surname = models.CharField(
        verbose_name="sobrenome", 
        max_length=700, 
        validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', 
        message='Sobrenome deve conter apenas letras, numeros e espacos.', 
        code='erro')]
    )
    cpf = models.CharField(
        max_length=11, 
        help_text='Devera conter apenas numeros', 
        unique=True, 
        validators=[validate_cpf]
    )
    adress = models.CharField(
        verbose_name="endereco", 
        max_length=50
    )
    number = models.CharField(
        verbose_name="numero", 
        max_length=5, 
        validators=[RegexValidator(regex='[0-9]+', 
        message='Deve conter apenas numeros maiores que 0', 
        code='erro')]
    )
    complement = models.CharField(
        verbose_name="complemento", 
        max_length=30,
        blank=True
    )
    district = models.CharField(
        verbose_name="bairro", 
        max_length=30
    )
    zip_code = models.CharField(
        verbose_name="cep", 
        validators=[RegexValidator(regex='7[0-3][0-9]{3}-[0-9]{3}', 
        message='CEP estar no formato xxxxx-xxx, e ser um CEP do DF', 
        code='erro')],
        max_length=9
    )
    city = models.CharField(max_length=20, choices=(
        ('Aguas Claras', 'Aguas Claras'),
        ('Brazlandia', 'Brazlandia'),
        ('Candangolandia', 'Candangolandia'),
        ('Ceilandia', 'Ceilandia'),
        ('Cruzeiro', 'Cruzeiro'),
        ('Fercal', 'Fercal'),
        ('Gama', 'Gama'),
        ('Guara', 'Guara'),
        ('Itapoa', 'Itapoa'),
        ('Jardim Botanico', 'Jardim Botanico'),
        ('Lago Norte', 'Lago Norte'),
        ('Lago Sul', 'Lago Sul'),
        ('Nucleo Bandeirante', 'Nucleo Bandeirante'),
        ('Paranoa', 'Paranoa'),
        ('Park Way', 'Park Way'),
        ('Planaltina', 'Planaltina'),
        ('Plano Piloto', 'Plano Piloto'),
        ('Samambaia', 'Samambaia'),
        ('Taguatinga', 'Taguatinga'),
        ('Recanto das Emas', 'Recanto das Emas'),
        ('Riacho Fundo 1', 'Riacho Fundo 1'),
        ('Riacho Fundo 2', 'Riacho Fundo 2'),
        ('Santa Maria', 'Santa Maria'),
        ('SCIA', 'SCIA'),
        ('SIA', 'SIA'),
        ('Sao Sebastiao', 'Sao Sebastiao'),
        ('Sobradinho', 'Sobradinho'),
        ('Sobradinho 2', 'Sobradinho 2'),
        ('Sudoeste', 'Sudoeste'),
        ('Varjao', 'Varjao'),
        ('Vicente Pires', 'Vicente Pires'),
    ),)
    state = models.CharField(
        verbose_name="estado",
        max_length=2,
        default='DF',
    )

    first_name = False
    last_name = False
    REQUIRED_FIELDS = []


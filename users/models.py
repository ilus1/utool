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
    zip_code = models.CharField(
        verbose_name="cep", 
        validators=[RegexValidator(regex='7[0-3][0-9]{3}-[0-9]{3}', 
        message='CEP estar no formato xxxxx-xxx, e ser um CEP do DF', 
        code='erro')],
        max_length=9
    )
    city = models.CharField(max_length=20, verbose_name = "cidade", choices=(
        ('aguas_claras', 'Águas Claras'),
        ('brazlandia', 'Brazlândia'),
        ('candangolandia', 'Candangolândia'),
        ('ceilandia', 'Ceilândia'),
        ('cruzeiro', 'Cruzeiro'),
        ('fercal', 'Fercal'),
        ('gama', 'Gama'),
        ('guara', 'Guará'),
        ('itapoa', 'Itapoã'),
        ('jardim_botanico', 'Jardim Botânico'),
        ('lago_norte', 'Lago Norte'),
        ('lago_Sul', 'Lago Sul'),
        ('nucleo_bandeirante', 'Núcleo Bandeirante'),
        ('paranoa', 'Paranoá'),
        ('park_way', 'Park Way'),
        ('planaltina', 'Planaltina'),
        ('plano_piloto', 'Plano Piloto'),
        ('samambaia', 'Samambaia'),
        ('taguatinga', 'Taguatinga'),
        ('recanto_das_emas', 'Recanto das Emas'),
        ('riacho_fundo_1', 'Riacho Fundo 1'),
        ('riacho _fundo_2', 'Riacho Fundo 2'),
        ('santa_maria', 'Santa Maria'),
        ('SCIA', 'SCIA'),
        ('SIA', 'SIA'),
        ('sao_sebastiao', 'São Sebastiao'),
        ('sobradinho', 'Sobradinho'),
        ('sobradinho_2', 'Sobradinho 2'),
        ('sudoeste', 'Sudoeste'),
        ('varjao', 'Varjão'),
        ('vicente pires', 'Vicente Pires'),
    ),)
    
    district = models.CharField(
        verbose_name="bairro", 
        max_length=30
    )

    state = models.CharField(
        verbose_name="estado",
        max_length=2,
        default='DF',
    )

    first_name = False
    last_name = False
    REQUIRED_FIELDS = []


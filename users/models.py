from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .utils import validate_cpf

class MyUserModel(AbstractUser):
    name = models.CharField(
        verbose_name="nome", 
        max_length=50, 
        validators=[RegexValidator(regex='[0-9a-zA-Z]{3}[0-9a-zA-Z]*', 
            message='Nome deve conter apenas letras e números.', 
            code='erro')]
    )
    surname = models.CharField(
        verbose_name="sobrenome", 
        max_length=700, 
        validators=[RegexValidator(regex='[0-9a-zA-Z ]{3}[0-9a-zA-Z ]*', 
            message='Sobrenome deve conter apenas letras, números e espaços.', 
            code='erro')]
    )
    cpf = models.CharField(
        max_length=11, 
        help_text='Deverá conter apenas números', 
        unique=True, 
        validators=[validate_cpf],
        verbose_name="CPF"
    )
    adress = models.CharField(
        verbose_name="endereço", 
        max_length=50
    )
    number = models.CharField(
        verbose_name="número", 
        max_length=5, 
        validators=[RegexValidator(regex='[0-9]+', 
            message='Deve conter apenas números maiores que 0', 
            code='erro')]
    )
    complement = models.CharField(
        verbose_name="complemento", 
        max_length=30,
        blank=True
    )
    zip_code = models.CharField(
        verbose_name="CEP", 
        validators=[RegexValidator(regex='7[0-3][0-9]{3}-[0-9]{3}', 
        message='CEP deve estar no formato xxxxx-xxx, e ser um CEP do DF', 
            code='erro')],
            max_length=9
    )
    district = models.CharField(
        max_length=20, 
        verbose_name = "bairro", 
        choices=(
            ('Águas Claras', 'Águas Claras'),
            ('Brazlândia', 'Brazlândia'),
            ('Candangolândia', 'Candangolândia'),
            ('Ceilândia', 'Ceilândia'),
            ('Cruzeiro', 'Cruzeiro'),
            ('Fercal', 'Fercal'),
            ('Gama', 'Gama'),
            ('Guará', 'Guará'),
            ('Itapoã', 'Itapoã'),
            ('Jardim Botânico', 'Jardim Botânico'),
            ('Lago Norte', 'Lago Norte'),
            ('Lago Sul', 'Lago Sul'),
            ('Núcleo Bandeirante', 'Núcleo Bandeirante'),
            ('Paranoá', 'Paranoá'),
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
            ('São Sebastião', 'São Sebastião'),
            ('Sobradinho', 'Sobradinho'),
            ('Sobradinho 2', 'Sobradinho 2'),
            ('Sudoeste', 'Sudoeste'),
            ('Varjão', 'Varjão'),
            ('Vicente Pires', 'Vicente Pires'),)
    )

    state = models.CharField(
        verbose_name="estado",
        max_length=2,
        default='DF'
    )

    first_name = False
    last_name = False
    REQUIRED_FIELDS = []


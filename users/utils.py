from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import re

def validate_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        raise ValidationError(
            _('CPF inválido, o CPF deve conter apenas números.'),
            params={'cpf': cpf},
        )

    firts_nine_of_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(firts_nine_of_cpf[index]) * reverse  

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            firts_nine_of_cpf += str(d)

    sequence = firts_nine_of_cpf == str(firts_nine_of_cpf[0]) * len(cpf)

    if cpf != firts_nine_of_cpf or sequence:
        raise ValidationError(
            _('%(cpf)s não e um CPF válido.'),
            params={'cpf': cpf},
        )

from wtforms.validators import ValidationError
import re


def validate_cpf(form, field,formatacao=False):

    cpf = field.data
    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) and formatacao:
        raise ValidationError(f'Número de CPF inválido')

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in cpf if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11:
        raise ValidationError(f'Número de CPF inválido')




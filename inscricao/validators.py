from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email


ZERO_ERROR = "Este campo não pode ser zero."
PHONE_INVALID = "Numero de telemovel é invalido."
SESSAO_MIN_ERROR = "É necessário inscrever em pelo menos 1 sessão."


def email_validator(value):
    return validate_email(value)

def not_zero_validator(value):
    if value == 0 or value == None:
        raise ValidationError(ZERO_ERROR)


def telefone_validator(value):
    if len(str(value)) < 9:
        raise ValidationError(PHONE_INVALID)
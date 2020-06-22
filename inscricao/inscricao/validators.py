from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email

ALMOCOS_FULL = "Existem apenas _NUM_ almoços disponiveis"
LESS_THEN_ZERO_ERROR = "Não pode ser menor que 0"
NUMBER_ERROR = "Precisa de ser um numero."
ZERO_ERROR = "Não pode ser 0."
PHONE_INVALID = "Numero de telemovel é invalido."
SESSAO_MIN_ERROR = "É necessário inscrever em pelo menos 1 sessão."
EMAIL_ERROR = "O email não é valido."
ANO_ESCOLA_ERROR = "Ano da turma inválido."
TRANSPORTE_FULL = "Existem apenas _NUM_ lugares restantes"

def smaller_zero_validator(value):
    if(not str(value).isdigit()):
        raise ValidationError(NUMBER_ERROR)
    if value < 0:
        raise ValidationError(LESS_THEN_ZERO_ERRO)
def email_validator(value):
    try:
        validate_email(value)
    except:
        raise ValidationError(EMAIL_ERROR)

def not_zero_validator(value):
    if(not str(value).isdigit()):
        raise ValidationError(NUMBER_ERROR)
    if value == 0 or value == None:
        raise ValidationError(ZERO_ERROR)


def telefone_validator(value):
    if(not str(value).isdigit()):
        raise ValidationError(NUMBER_ERROR)
    val = str(value)
    if len(val) != 9:
        raise ValidationError(PHONE_INVALID)

def escola_ano_validator(value):
    if(not str(value).isdigit()):
        raise ValidationError(NUMBER_ERROR)
    val = str(value)
    if value > 12 or value < 0:
        raise ValidationError(ANO_ESCOLA_ERROR)
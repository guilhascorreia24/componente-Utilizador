import django_filters
from django_filters import DateFilter
from .models import *

class TarefaFilter(django_filters.FilterSet):

    sessao_idsessao = django_filters.ChoiceFilter(choices =
	[(sessao.__id__(), sessao.atividade_idatividade.titulo) for sessao in Sessao.objects.all()])

    CHOICES = (
        ('1', 'Concluida'),
        ('0', 'Pendente')
    )

    concluida = django_filters.ChoiceFilter(choices=CHOICES)

    class Meta:
        model = Tarefa
        exclude = ['coordenador_utilizador_idutilizador','concluida','colaborador_utilizador_idutilizador','sessao_idsessao','dia_dia','hora_inicio']
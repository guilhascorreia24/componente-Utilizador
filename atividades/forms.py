from django.forms import ModelForm
from atividades import models


class Form_Create_Sessao(ModelForm):
    class Meta:
        model = models.Sessao
        fields = ['nrinscritos','horario_horainicio']

class Form_Create_Atividades(ModelForm):
    class Meta:
        model = models.Atividade
        fields = ['titulo','capacidade','duracao','descricao','espaco_idespaco']
    


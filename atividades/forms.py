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
    
class Form_Responsaveis(ModelForm):

    def fill(self, idinscricao):
        self.cleaned_data['idinscricao'] = idinscricao
        
    class Meta:
        model = models.Responsaveis
        fields = ['nome','email']

class Form_Inscricao(ModelForm):
    class Meta:
        model = models.Inscricao
        fields = ['ano','local','areacientifica']

class Form_InscricaoColetiva(ModelForm):

    def fill(self, idUtilizador, idEscola, idInscricao):
        self.cleaned_data['participante_utilizador_idutilizador'] = idUtilizador
        self.cleaned_data['escola_idescola'] = idEscola
        self.cleaned_data['inscricao_idinscricao '] = idInscricao

    class Meta:
        model = models.InscricaoColetiva
        fields = ['turma']

class Form_Escola(ModelForm):
    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']
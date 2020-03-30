from django.forms import ModelForm,modelformset_factory,Form
from django import forms
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

    def save(self, idinscricao):
        base = super(Form_Responsaveis, self).save(commit=False)
        base.idinscricao = idinscricao
        return base.save()

    class Meta:
        model = models.Responsaveis
        fields = ['nome','email']

class Form_Inscricao(ModelForm):
    class Meta:
        model = models.Inscricao
        fields = ['ano','local','areacientifica']

class Form_InscricaoColetiva(ModelForm):
    def save(self, idUtilizador, idEscola, idInscricao):
        base = super(Form_InscricaoColetiva, self).save(commit=False)
        base.participante_utilizador_idutilizador= idUtilizador
        base.escola_idescola = idEscola
        base.inscricao_idinscricao = idInscricao
        return base.save()

    class Meta:
        model = models.InscricaoColetiva
        fields = ['turma']

class Form_Escola(ModelForm):
    class Meta:
        model = models.Escola
        fields = ['nome','local','telefone','email']

class Form_Transportes(Form):
    numero_transportes_penha=forms.IntegerField(label="Penha Numero de Passageiros")
    numero_transportes_gambleas = forms.IntegerField(label="Gambelas Numero de Passageiros")
    partida = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())
    chegada = forms.ModelChoiceField(queryset=models.HorarioHasDia.objects.all())

    def save(self, inscricao):
        base = super(Form_Transportes, self).save(commit=False)
        base.inscricao_idinscricao = inscricao
        return base.save()
    class Meta:
        mode = models
        fields = ['transporte_has_horario_id_transporte_has_horario']


class CustomForm:
    def __init__(self,request = 0):
        self.responsaveis = modelformset_factory(models.Responsaveis,form = Form_Responsaveis,extra=2)
        if request != 0 and request.method == 'POST':
            self.escola = Form_Escola(request.POST,prefix="escola")
            self.inscricao = Form_Inscricao(request.POST,prefix="inscricao")
            self.inscricao_coletiva = Form_InscricaoColetiva(request.POST,prefix="coletivo")
            self.responsaveis = self.responsaveis(request.POST)
        else:
            self.escola = Form_Escola(prefix="escola")
            self.inscricao = Form_Inscricao(prefix="inscricao")
            self.inscricao_coletiva = Form_InscricaoColetiva(prefix="coletivo")
    
    def is_valid(self):
        return all([self.escola.is_valid(), self.inscricao.is_valid(), self.responsaveis.is_valid()])#self.inscricao_coletiva.is_valid())

    def save(self):
        escola = self.escola.save()
        inscricao = self.inscricao.save()
        
        for each in self.responsaveis:
            each.save(inscricao)
        return self



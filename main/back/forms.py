from django.forms import *
from .models import *
from datetime import datetime, date
from django.db.models.fields import BLANK_CHOICE_DASH
from datetime import datetime
from django import forms

class DateInput(forms.DateInput):
    input_type = 'time'

class ExampleForm(forms.ModelForm):
	hora_inicio = forms.DateField(widget=DateInput)

class TarefasFormGroup(ModelForm):
	
	colaborador_utilizador_idutilizador = ChoiceField(choices = [("","Nenhum Colaborador Atribuido")] +
	[(colab.__id__(), colab.utilizador_idutilizador.nome) for colab in Colaborador.objects.all()], required=False)

	dia_dia = ChoiceField(choices = [("", "Nenhuma Dia Selecionado")] +
	[(di.__id__(), di.dia) for di in Dia.objects.all()], required=False)

	campus = ChoiceField(choices = [("", "Nenhum Campus Selecionado")] +
	[(campus.idcampus, campus.nome) for campus in Campus.objects.all()], required=False)

	class Meta:
		model = Tarefa
		exclude = ['sessao_idsessao','buscar','levar', 'dia_dia','concluida', 'coordenador_utilizador_idutilizador', 'colaborador_utilizador_idutilizador']
		widgets = {
				  'nome' : TextInput(attrs={'class': 'input'}),
				  'hora_inicio' : DateInput(attrs={'class': 'input'}),
				}	

class TarefasFormAtividade(ModelForm):
	
	colaborador_utilizador_idutilizador = ChoiceField(choices = [("","Nenhum Colaborador Atribuido")] +
	[(colab.__id__(), colab.utilizador_idutilizador.nome) for colab in Colaborador.objects.all()], required=False)

	atividade_idatividade = ChoiceField(choices = [("", "Nenhuma Atividade Selecionada")] +
	[(actv.__id__(), actv.titulo) for actv in Atividade.objects.all()])


	class Meta:
		model = Tarefa
		exclude = ['buscar','sessao_idsessao','levar', 'dia_dia','concluida', 'coordenador_utilizador_idutilizador', 'colaborador_utilizador_idutilizador']
		widgets = {
				  'nome' : TextInput(attrs={'class': 'input'}),
				  }		
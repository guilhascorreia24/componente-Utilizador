from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from django import forms
from tarefas import models

class Form_Disponibilidade(ModelForm):

    def save(self, colaborador_utilizador_idutilizador):
        base = super(Form_Disponibilidade, self).save(commit=False)
        base.colaborador_utilizador_idutilizador = colaborador_utilizador_idutilizador
        base.save()
        return base

    class Meta:
        model = models.Disponibilidade
        fields = ['dia_dia','horario_hora','horario_hora1','tipo_de_tarefa']

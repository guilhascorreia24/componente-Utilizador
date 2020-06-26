from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from django import forms
from tarefas import models

class Form_Disponibilidade(ModelForm):

    def save(self,**kwargs):

        tudo = models.Disponibilidade.objects.filter(colaborador_utilizador_idutilizador = self.colaborador)
        for um in tudo:
            if self.cleaned_data['dia_dia'] == um.dia_dia and self.cleaned_data['horario_hora'] == um.horario_hora and self.cleaned_data['horario_hora1'] == um.horario_hora1 and self.cleaned_data['tipo_de_tarefa'] == um.tipo_de_tarefa:
                return None

        base = super(Form_Disponibilidade, self).save(commit=False)
        base.colaborador_utilizador_idutilizador = self.colaborador
        base.save()
        return base

    def save_user(self, colaborador):
        self.colaborador = colaborador

    def clean(self):
        super().clean()
        time = self.cleaned_data['horario_hora']
        time2 = self.cleaned_data['horario_hora1']
        if time.hora >= time2.hora:
            raise ValidationError({'horario_hora1': "Hora inválida"})

    class Meta:
        model = models.Disponibilidade
        fields = ['dia_dia','horario_hora','horario_hora1','tipo_de_tarefa']
        

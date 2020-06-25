from django import forms
from django.forms.models import ModelMultipleChoiceField
from blog.models import Atividade, Utilizador, Espaco, Campus, UnidadeOrganica, Departamento, Paragem
from django.forms import TextInput


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = [
            "titulo",
            "descricao",
            "publico_alvo",
            "capacidade",
            "duracao",
            "tematica",
        ]


class SalaForm(forms.ModelForm):
    class Meta:
        model = Espaco
        campus_idcampus = forms.ModelMultipleChoiceField(queryset=Campus.objects.all(), to_field_name="nome")
        fields = ['nome', 'img', 'campus_idcampus']


class UoForm(forms.ModelForm):
    class Meta:
        model = UnidadeOrganica
        campus_idcampus = forms.ModelMultipleChoiceField(queryset=Campus.objects.all(), to_field_name="nome")
        fields = ['sigla', 'campus_idcampus']


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        unidade_organica_iduo = forms.ModelMultipleChoiceField(queryset=UnidadeOrganica.objects.all(), to_field_name="sigla")
        fields = ['nome', 'unidade_organica_iduo']


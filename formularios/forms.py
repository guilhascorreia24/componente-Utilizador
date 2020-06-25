from django import forms
from blog.models import Utilizador,DiaAberto,Curso,UnidadeOrganica,Campus
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms.models import ModelChoiceField
from django.core import signing
import hashlib
import datetime

class cursoForm(forms.ModelForm):
    unidade_organica_iduo=forms.ModelChoiceField(queryset=UnidadeOrganica.objects.all(), to_field_name="sigla", required = False)
    nome=forms.CharField(max_length=255, required = False)
    
    class Meta:
        model=Curso
        fields=['unidade_organica_iduo','nome']
    
        

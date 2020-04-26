from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notificacao
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Utilizador

class UserRegisterForm(forms.Form):
    Destinatario=forms.IntegerField(label="Destinatario")
    Descricao=forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "30", 'rows': "3", }))


    class Meta:
        model=Notificacao
        fields=['Descricao','idutilizadorenvia','Destinatario']

    def save(self,request):
        data = self.cleaned_data 
        Not = Notificacao(descricao=data['Descricao'],idutilizadorenvia=request.session['user_id'],utilizadorrecebe=data['Destinatario'])
        Not.save()
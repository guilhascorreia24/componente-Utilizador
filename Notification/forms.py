from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notificacao
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Utilizador

class NotificationForm(forms.Form):

    Destinatario=forms.EmailField(label="Destinatario")
    Assunto=forms.CharField(label="Assunto")
    Descricao=forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "30", 'rows': "3", }))

    class Meta:
        model=Notificacao
        fields=['Descricao','Assunto','idutilizadorenvia','Destinatario']

    def save(self,request):
        Not = Notificacao(descricao=request.POST['Descricao'],assunto=request.POST['Assunto'],idutilizadorenvia=request.session['user_id'],utilizadorrecebe=request.POST['Destinatario'])
        Not.save()
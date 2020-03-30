from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notificacao
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class UserRegisterForm(forms.Form):
    Destinatario=forms.IntegerField(label="Destinatario")
    Descricao=forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "30", 'rows': "3", }))
    

    class Meta:
        model=Notificacao
        fields=['Descricao','Destinatario']
    
    def save(self):
        data = self.cleaned_data
        #Not = Notificacao(descricao=data['Descricao'],idutilizadorenvia=get_user_model(),utilizadorrecebe=data['Destinatario'])
        Not = Notificacao(descricao=data['Descricao'],idutilizadorenvia='999',utilizadorrecebe=data['Destinatario'])
        Not.save()

'''class UserCheckForm(forms.Form):
    Target_ID = forms.IntegerField(label="Ver notificações")


    class Meta:
        model = Notificacao
        fields=['Target_ID']

    def save(self):
        data = self.cleaned_data
        Check = Notificacao(Checkk = data['Target_ID'])
        Check.save()'''
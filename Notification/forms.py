from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Notificacao
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Utilizador

my_default_errors = {
    'required': 'Campo vazio',
    'invalid': 'Demasiado longo',
    'except':'Demasiado longo',
}

class NotificationForm(forms.Form):

    Destinatario=forms.CharField(label="Destinatario")
    Assunto=forms.CharField(label="Assunto",error_messages=my_default_errors)
    Descricao=forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "30", 'rows': "3", }),error_messages=my_default_errors)

    class Meta:
        model=Notificacao
        fields=['Descricao','Assunto','idutilizadorenvia','Destinatario']
    
    def clean(self):
        super().clean()
        if len(self.cleaned_data['Assunto'])>45:
            raise ValidationError({'Assunto':"Demasiado longo"})
    
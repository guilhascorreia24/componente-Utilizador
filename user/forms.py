from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizador,DiaAberto
from django.core import validators
from django.core.exceptions import ValidationError
from django.core import signing
import hashlib
import datetime


class UserRegisterForm(forms.Form):
    name=forms.CharField(max_length=255,label="Nome")
    email = forms.EmailField(max_length=255,label="Email")
    telefone=forms.CharField(max_length=255,label="Telefone/Telemovel")
    password1=forms.CharField(max_length=255,label="Password",widget=forms.PasswordInput())
    password2=forms.CharField(max_length=255,label="Password Confirm",widget=forms.PasswordInput())
    funcao=forms.IntegerField(label="funcao")
    curso=forms.IntegerField(label="curso",required=False)
    Preferencias=forms.CharField(max_length=45,label="preferencia",widget=forms.Textarea)
    UO=forms.IntegerField(label="UO",required=False)
    departamento=forms.IntegerField(label="departamento",required=False)


    class Meta:
        model=Utilizador
        fields=['idutilizador','nome','email','telefone','password','funcao']
    
    def save(self):
        data = self.cleaned_data
        if DiaAberto.objects.filter(ano=datetime.date.today().year).exists():
            ano=DiaAberto.objects.get(ano=datetime.date.today().year)
            ano=DiaAberto.objects.get(ano=datetime.datetime.now().year)
        else:
            ano=None
        user=Utilizador(nome=data['name'],
            email=data['email'],telefone=data['telefone'],password=hashlib.sha256(data['password1'].encode('utf-8')).hexdigest(),validada=5,dia_aberto_ano=ano) # encriptar passe quando estiveresmos quse a acabr
        user.save()
    

class AuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=255,label="email")
    password=forms.CharField(max_length=255,label="password",widget=forms.PasswordInput())

    class Meta:
        model=Utilizador
        fields=['email','password']

class ModifyForm(forms.Form):
    name=forms.CharField(max_length=255,label="Nome")
    email = forms.EmailField(max_length=255,label="Email")
    telefone=forms.CharField(max_length=255,label="Telefone/Telemovel")
    funcao=forms.CharField(max_length=45,label="funcao")
    UO=forms.CharField(max_length=45,label="uo")
    dep=forms.CharField(max_length=45,label="dep")
    curso=forms.CharField(max_length=45,label="curso")
    ano=forms.IntegerField(label="ano")
    preferencia=forms.CharField(max_length=45,label="preferencia")

    class Meta:
        model=Utilizador
        fields=['name','email','telefone','funcao','UO','curso','dep','preferencia','ano']
    
    def save(self):
        data = self.cleaned_data
        user=Utilizador(nome=data['name'],
            email=data['email'],telefone=data['telefone'],validada=data['funcao'])
        user.save()
    
class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, required=False,max_length=255,label="Password1")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False,max_length=255,label="Password2")

    class Meta:
        model=Utilizador
        fields=['password','confirm_password']

class EmailSender(forms.Form):
        email = forms.EmailField(max_length=45,label="Email")
        
        class Meta:
            model=Utilizador
            fields=['email']

class DeleteUser(forms.Form):
    iduser=forms.IntegerField()
    
    class Meta:
        model=Utilizador
        fields=['iduser']



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizador
from django.core import validators
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    name=forms.CharField(max_length=255,label="Nome")
    username=forms.CharField(max_length=255,label="username")
    email = forms.EmailField(max_length=255,label="Email")
    telefone=forms.CharField(max_length=255,label="Telefone/Telemovel")
    password1=forms.CharField(max_length=255,label="Password",widget=forms.PasswordInput())
    password2=forms.CharField(max_length=255,label="Password Confirm",widget=forms.PasswordInput())
    funcao=forms.IntegerField(label="funcao")

    class Meta:
        model=Utilizador
        fields=['idutilizador','nome','email','telefone','password','username','funcao']
    
    def save(self):
        data = self.cleaned_data
        user=Utilizador(nome=data['name'],username=data['username'],
            email=data['email'],telefone=data['telefone'],password=data['password2'],validada=data['funcao'])
        user.save()
    

class AuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=255,label="email")
    password=forms.CharField(max_length=255,label="password",widget=forms.PasswordInput())

    class Meta:
        model=Utilizador
        fields=['email','password']

class ModifyForm(forms.Form):
    name=forms.CharField(max_length=255,label="Nome")
    username=forms.CharField(max_length=255,label="username")
    email = forms.EmailField(max_length=255,label="Email")
    telefone=forms.CharField(max_length=255,label="Telefone/Telemovel")
    funcao=forms.CharField(max_length=45,label="funcao")
    UO=forms.CharField(max_length=45,label="uo")
    dep=forms.CharField(max_length=45,label="dep")
    curso=forms.CharField(max_length=45,label="curso")

    class Meta:
        model=Utilizador
        fields=['name','username','email','telefone','funcao','UO','curso','dep']
    
    def save(self):
        data = self.cleaned_data
        user=Utilizador(nome=data['name'],username=data['username'],
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



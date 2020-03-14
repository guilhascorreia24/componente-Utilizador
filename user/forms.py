from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Utilizador
from django.core import validators


class UserRegisterForm(forms.Form):
    name=forms.CharField(max_length=45,label="Nome")
    username=forms.CharField(max_length=45,label="username")
    email = forms.EmailField(max_length=45,label="Email")
    telefone=forms.CharField(max_length=45,label="Telefone/Telemovel")
    password1=forms.CharField(max_length=45,label="Password",widget=forms.PasswordInput(),
                                validators = [validators.MinLengthValidator(6)])
    password2=forms.CharField(max_length=45,label="Password Confirm",widget=forms.PasswordInput())

    class Meta:
        model=Utilizador
        fields=['idutilizador','nome','email','telefone','password','username']
    
    def save(self):
        data = self.cleaned_data
        user=Utilizador(nome=data['name'],username=data['username'],
            email=data['email'],telefone=data['telefone'],password=data['password1'])
        user.save()
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password

class AuthenticationForm(forms.Form):
    email = forms.EmailField(max_length=45,label="email")
    password=forms.CharField(max_length=45,label="password",widget=forms.PasswordInput())

    class Meta:
        model=Utilizador
        fields=['email','password']
    
    


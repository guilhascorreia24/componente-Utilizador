from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm
from .models import Utilizador
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() and Utilizador.objects.filter(email=request.POST['email'], telefone=request.POST['telefone']).exists() is False:
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registo feito com Sucesso!')
            return redirect('blog-home')
        else:
            error=False
            error1=False
            error2=False
            if Utilizador.objects.filter(email=request.POST['email'], telefone=request.POST['telefone']).exists():
                error="Email ja existe"
            if 1<len(request.POST['password1'])<6:
                error1="password muito curta"
            if request.POST['password1']!=request.POST['password2']:
                error2="Passwords nao coincidem"
            return render(request,'register.html',{'form':form,'error1':error,'error2':error1,'error3':error2})
    form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})

def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request.POST)
        if request.POST['email'] is not None and request.POST['password'] is not None:
            if Utilizador.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
                user=authenticate(email=request.POST['email'],password=request.POST['password'])
               # print(Utilizador.objects.get(email=request.POST['email']).idutilizador)
                username=Utilizador.objects.get(email=request.POST['email']).username
                messages.success(request, f"Bem-vindo {username}")
                request.session['user_id']=Utilizador.objects.get(email=request.POST['email']).idutilizador
                return redirect('blog-home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request = request,template_name = "login.html",context={"form":form})

def logout_request(request):
    request.session['user_id']=None
    messages.info(request, "Logged out successfully!")
    return redirect("blog-home")
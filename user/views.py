from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm
from .models import Utilizador, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
    del request.session['user_id']
    messages.info(request, "Logged out successfully!")
    return redirect("blog-home")

def delete_user(request):
    username = Utilizador.objects.get(request.session['user_id'])
    Utilizador.delete(username)
    messages.success(request,"User deleted")

    if not Utilizador.objects.get(username).exists():
        messages.error(request, "User does not exist")    
        return render(request, 'blog-home.html')
    
    return render(request, 'blog-home.html')
    


def modify_user(request):
    if not Participante.objects.filter(request.session['user_id']).name.exist():
        username = Utilizador.objects.get(request.session['user_id'])
        Utilizador.username = username 
    elif Participante.objects.filter(request.session['user_id']).exist():
        messages.error(request,"Username already taken")
        return render(request,'profile.html')
    
      # anda discord
    #email
    
    #telefone
    #password
    #nome

def profile(request):
    id=request.session['user_id']
    name=Utilizador.objects.get(Utilizadorid=id).name
    email=Utilizador.objects.get(Utilizadorid=id).email
    telefone=Utilizador.objects.get(Utilizadorid=id).telefone
    if Participante.objects.filter(utilizador_idutilizador=id).exist():
        funcao="Participante"
        return render(request,'profile.html',{'nome':name,'email':email,'telefone':telefone,'funcao':funcao})
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exist():
        funcao ="docente Univesitario"
        IDUO=ProfessorUniversitario.objects.get(utilizador_utilizadorid=id).unidade_organica_iduo
        return render(request,'profile.html',{'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'Iduo':IDUO})
    elif Administrador.objects.filter(utilizador_utilizadorid=id).exist():
        funcao="administardor"
        return render(request,'profile.html',{'nome':name,'email':email,'telefone':telefone,'funcao':funcao})
    elif Coordenador.objects.filter(utilizador_utilizadorid=id).exist():
        funcao="Coordenador"
        idUO=Coordenador.objects.get(utilizador_utilizadorid=id).unidade_organica_iduo
        return render(request,'profile.html',{'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'Iduo':IDUO})
    elif Colaborador.objects.filter(utilizador_utilizadorid=id).exist():
        ano=Colaborador.objects.get(utilizador_utilizadorid=id).dia_aberto_ano
        funcao="Colaborador"
        curso=Colaborador.objects.get(utilizador_utilizadorid=id).curso
        return render(request,'profile.html',{'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'ano':ano,'curso':curso})





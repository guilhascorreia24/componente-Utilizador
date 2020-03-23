from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm, ModifyForm, Recoveryform
from .models import Utilizador, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, DjangoSession


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() and Utilizador.objects.filter(email=request.POST['email'], telefone=request.POST['telefone']).exists() is False:
            form.save()
            print(Utilizador.objects.get(email=request.POST['email']).idutilizador)
            part=Participante(pk=Utilizador.objects.get(email=request.POST['email']).idutilizador)
            part.save()
            messages.success(request, f'Registo feito com Sucesso!')
            return redirect('blog-home')
        else:
            error='Preencha este campo.'
            error3='Preencha este campo.'
            error1='Preencha este campo.'
            error2='Preencha este campo.'
            if  Utilizador.objects.filter(email=request.POST['email']).exists():
                error="Email ja existe"
            if Utilizador.objects.filter(telefone=request.POST['telefone']).exists():
                error3="telefone ja existe"

            if 1<len(request.POST['password1'])<6:
                error1="password muito curta"

            if request.POST['password1']!=request.POST['password2']:
                error2="Passwords nao coincidem"
            return render(request,'register.html',{'form':form,'error1':error,'error2':error1,'error3':error2,'error4':error3})
    form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})

def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request.POST)
        if request.POST['email'] != '' and request.POST['password'] != '':
            if Utilizador.objects.filter(email=request.POST['email'],password=request.POST['password']).exists():
                username=Utilizador.objects.get(email=request.POST['email']).username
                messages.success(request, f"Bem-vindo {username}")
                request.session['user_id']=Utilizador.objects.get(email=request.POST['email']).idutilizador
                r= redirect('blog-home')
                if 'check' in request.POST and request.POST['check']=='1' :
                   r.set_cookie('cookie_id',request.session['user_id'],7 * 24 * 60 * 60)
                return r
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request = request,template_name = "login.html",context={"form":form})

def logout_request(request):
    r=redirect("blog-home")
    del request.session['user_id']
    if 'cookie_id' in request.COOKIES :
        r.delete_cookie('cookie_id')
    messages.info(request, "Logged out successfully!")
    return r

def delete_user(request):
    username = Utilizador.objects.get(request.session['user_id'])
    username.delete()
    messages.success(request,"User deleted")

    if not Utilizador.objects.get(username).exists():
        messages.error(request, "User does not exist")    
        return render(request, 'blog-home.html')
    
    return render(request, 'blog-home.html')
    
def recovery_request(request):
    #if request.method=="POST":
      #  if Utilizador.objects.filter(email=request.POST['email']).exists():
            
    form=Recoveryform()
    return render(request,"reset.html",{"form":form})

def modify_user(request):
    if not Participante.objects.filter(request.session['user_id']).name.exist():
        username = Utilizador.objects.get(request.session['user_id'])
        Utilizador.username = username 
    elif Participante.objects.filter(request.session['user_id']).exist():
        messages.error(request,"Username already taken")
        return render(request,'profile.html')
    
     
    #email
    
    #telefone
    #password
    #nome


def profile(request):
    id=request.session['user_id']
    name=Utilizador.objects.get(idutilizador=id).nome
    if Utilizador.objects.get(idutilizador=id).username == '':
        username=Utilizador.objects.get(idutilizador=id).nome
    else:
        username=Utilizador.objects.get(idutilizador=id).username
    email=Utilizador.objects.get(idutilizador=id).email
    telefone=Utilizador.objects.get(idutilizador=id).telefone
    form=ModifyForm()
    if Participante.objects.filter(utilizador_idutilizador=id).exists():
        funcao="Participante"
        return render(request,'profile.html',{"form":form,'nome':name,'username':username,'email':email,'telefone':telefone,'funcao':funcao})
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao ="docente Univesitario"
        IDUO=ProfessorUniversitario.objects.get(utilizador_utilizadorid=id).unidade_organica_iduo
        return render(request,'profile.html',{"form":form,'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'Iduo':IDUO})
    elif Administrador.objects.filter(utilizador_utilizadorid=id).exists():
        funcao="administardor"
        return render(request,'profile.html',{"form":form,'nome':name,'email':email,'telefone':telefone,'funcao':funcao})
    elif Coordenador.objects.filter(utilizador_utilizadorid=id).exists():
        funcao="Coordenador"
        idUO=Coordenador.objects.get(utilizador_utilizadorid=id).unidade_organica_iduo
        return render(request,'profile.html',{"form":form,'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'Iduo':IDUO})
    elif Colaborador.objects.filter(utilizador_utilizadorid=id).exists():
        ano=Colaborador.objects.get(utilizador_utilizadorid=id).dia_aberto_ano
        funcao="Colaborador"
        curso=Colaborador.objects.get(utilizador_utilizadorid=id).curso
        return render(request,'profile.html',{"form":form,'nome':name,'email':email,'telefone':telefone,'funcao':funcao,'ano':ano,'curso':curso})





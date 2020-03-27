from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm, ModifyForm, PasswordChangeForm, EmailSender
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.core import signing
from .models import Departamento, Utilizador, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, DjangoSession

#----------------------------------------------registo user--------------------------------
def password_check(passwd):   
    SpecialSym =['$', '@', '#', '%'] 
    val = True
      
    if len(passwd) < 6: 
        val='comprimento deve ser pelo menos 6' 
        return val
          
    if len(passwd) > 20: 
        val='comprimento não deve ser superior a 20'
        return val
          
    if not any(char.isdigit() for char in passwd): 
        val='A palavra-passe deve ter pelo menos um número'
        return val
          
    if not any(char.isupper() for char in passwd): 
        val='A palavra-passe  deve ter pelo menos uma letra maiúscula'
        return val
          
    if not any(char.islower() for char in passwd): 
        val='A palavra-passe  deve ter pelo menos uma letra minúscula'
        return val
          
    return val

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        print(request.POST)
        if form.is_valid() and not Utilizador.objects.filter(email=request.POST['email']).exists() and  not Utilizador.objects.filter(telefone=request.POST['telefone']).exists() and password_check(request.POST['password1']) is True:
            form.save()
            part = Participante(pk=Utilizador.objects.get(
                email=request.POST['email']).idutilizador)
            part.save()
            # criar notificaçao para validacao
            messages.success(request, f'Registo feito com Sucesso!')
            return redirect('blog-home')
        else:
            error=False
            error3=False
            error2=False
            error1=False
            if request.POST['email'] is None:
                error = 'Preencha este campo.'
            if request.POST['telefone'] is None:    
                error3 = 'Preencha este campo.'
            if request.POST['password1'] is None:
                error1 = 'Preencha este campo.'
            if request.POST['password2'] is None:
                error2 = 'Preencha este campo.'
            if Utilizador.objects.filter(email=request.POST['email']).exists():
                error = "Email ja existe"
            if Utilizador.objects.filter(telefone=request.POST['telefone']).exists():
                error3 = "telefone ja existe"
            if request.POST['password1'] != request.POST['password2']:
                error2 = "Passwords nao coincidem"
            if password_check(request.POST['password1']):
                error1 = password_check(request.POST['password1'])
            return render(request, 'register.html', {'form': form, 'error1': error, 'error2': error1, 'error3': error2, 'error4': error3})
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

#*----------------------------------------------------------login---------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if request.POST['email'] != '' and request.POST['password'] != '':
            if Utilizador.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
                username = Utilizador.objects.get(
                    email=request.POST['email']).username
                messages.success(request, f"Bem-vindo {username}")
                request.session['user_id'] = Utilizador.objects.get(
                    email=request.POST['email']).idutilizador
                r = redirect('blog-home')
                if 'check' in request.POST and request.POST['check'] == '1':
                    r.set_cookie(
                        'cookie_id', request.session['user_id'], 7 * 24 * 60 * 60)
                return r
            else:
                messages.error(request, "Username e/ou palavra-passe")
    else:
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form})


def logout_request(request):
    r = redirect("blog-home")
    del request.session['user_id']
    if 'cookie_id' in request.COOKIES:
        r.delete_cookie('cookie_id')
    messages.info(request, "saiste com sucesso")
    return r

#----------------------------------------------remover user-----------------------------------
def delete_user(request):
    username = Utilizador.objects.get(request.session['user_id'])
    username.delete()
    messages.success(request, "User deleted")

    if not Utilizador.objects.get(username).exists():
        messages.error(request, "Utilizador nao existe")
        return render(request, 'blog-home.html')

    return render(request, 'blog-home.html')

#--------------------------------------alterar user---------------------------------------------
def modify_data(request):
    id = request.session['user_id']
    name = request.POST['name']
    username = request.POST['username']
    email = request.POST['email']
    telefone = request.POST['telefone']
    t=Utilizador.objects.get(pk=id)
    t.nome=name
    t.username=username
    t.email=email
    t.telefone=telefone
    t.save()
    if ProfessorUniversitario.objects.filter(pk=id).exists():
        IDUO = ProfessorUniversitario.objects.get(pk=id).unidade_organica_iduo
    elif Coordenador.objects.filter(pk=id).exists():
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
    elif Colaborador.objects.filter(pk=id).exists():
        ano = Colaborador.objects.get(pk=id).dia_aberto_ano
        curso = Colaborador.objects.get(pk=id).curso
    




def modify_user(request,form,name,username,email,telefone,id):
    IDUO=False
    ano=False
    curso=False
    if Participante.objects.filter(pk=id).exists():
        funcao = "Participante"
    elif Administrador.objects.filter(pk=id).exists():
        funcao = "administardor"
    elif ProfessorUniversitario.objects.filter(pk=id).exists():
        funcao = "docente Univesitario"
        IDUO = ProfessorUniversitario.objects.get(pk=id).unidade_organica_iduo
    elif Coordenador.objects.filter(pk=id).exists():
        funcao = "Coordenador"
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
    elif Colaborador.objects.filter(pk=id).exists():
        ano = Colaborador.objects.get(pk=id).dia_aberto_ano
        funcao = "Colaborador"
        curso = Colaborador.objects.get(pk=id).curso
    return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso,'iduo':IDUO})


def profile(request):
    id = request.session['user_id']
    name = Utilizador.objects.get(idutilizador=id).nome
    if Utilizador.objects.get(idutilizador=id).username == '':
        username = Utilizador.objects.get(idutilizador=id).nome
    else:
        username = Utilizador.objects.get(idutilizador=id).username
    email = Utilizador.objects.get(idutilizador=id).email
    telefone = Utilizador.objects.get(idutilizador=id).telefone
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if "persona" in request.POST:
            return modify_user(request,form,name,username,email,telefone,id)
        else:
            return modify_data(request)
    else:
        form = ModifyForm()
    idUO=False
    ano=False
    curso=False
    if Participante.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Participante"
    elif Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "administardor"
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "docente Univesitario"
        depid = ProfessorUniversitario.objects.get( utilizador_idutilizador=id).departamento_iddepartamento
        dep= Departamento.ocjects.get(pk=depid).nome
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        idUO = Coordenador.objects.get( utilizador_utilizadorid=id).unidade_organica_iduo
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        ano = Colaborador.objects.get(utilizador_utilizadorid=id).dia_aberto_ano
        funcao = "Colaborador"
        curso = Colaborador.objects.get(utilizador_idutilizador=id).curso
    return render(request, 'profile.html', {"form": form, 'nome': name,'UO':idUO,'username': username, 'email': email, 'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso})

#--------------------------------------------recuperaçao de password---------------------------------
def change_password(request, id):
    id_deccryp=signing.loads(id)
    if request.method=='POST':
        form=PasswordChangeForm(request.POST)
        passwd=request.POST['password']
        if form.is_valid and password_check(passwd) is True:
            t=Utilizador.objects.get(pk=id_deccryp)
            t.password=passwd
            t.save()
            messages.success(request, f'Password alterada com sucesso')
            return redirect('blog-home')
        else:
            print(password_check(passwd))
            messages.error(request,password_check(passwd))
            if request.POST['confirm_password']!=passwd:
                error=True
                return render(request,"reset_password.html",{"form":form,"error":error})
    else:
        form=PasswordChangeForm()
    return render(request,"reset_password.html",{"form":form})


def reset(request):
    sub = EmailSender()
    if request.method == 'POST':
        sub = EmailSender(request.POST)
        recepient = request.POST['email']
        if Utilizador.objects.filter(email=recepient).exists():
            subject = 'Recuperação da Palavra-Passe'
            p=Utilizador.objects.get(email=recepient).idutilizador
            id = signing.dumps(p)
            message = 'Para recuperar a sua palavra-passe re-introduza uma palavra-passe nova, no seguinte link:http://127.0.0.1:8000/login/recuperacao_password/'+id+'/'
            send_mail(subject, message, 'a61098@ualg.pt', [recepient])
            messages.success(request, f'Verifique o seu email')
            return render(request, 'reset.html', {'form': sub})
        else:
            messages.error(request, f'Email incorreto')
    return render(request, 'reset.html', {'form': sub})
#-------------------------------------------------validacoes---------------------------------------------------------------
def validacoes(request):
    if request.POST == 'POST':
        if Coordenador.objects.filter(utilizador_utilizadorid=request.session['user_id']).exists():
            user = Utilizador.objects.get(validada=1)
    return render(request, "validacoes.html", {"users": user})

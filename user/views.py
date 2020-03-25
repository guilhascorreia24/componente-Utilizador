from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm, ModifyForm, PasswordChangeForm, EmailSender
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from .models import Utilizador, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, DjangoSession


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
            print(str(form.is_valid()) +" "+ str(Utilizador.objects.filter(email=request.POST['email']).exists()) +" "+  str(Utilizador.objects.filter(telefone=request.POST['telefone']).exists()) +" "+ str(password_check(request.POST['password1'])))
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
            error1 = password_check(request.POST['password1'])
            return render(request, 'register.html', {'form': form, 'error1': error, 'error2': error1, 'error3': error2, 'error4': error3})
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


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


def delete_user(request):
    username = Utilizador.objects.get(request.session['user_id'])
    username.delete()
    messages.success(request, "User deleted")

    if not Utilizador.objects.get(username).exists():
        messages.error(request, "Utilizador nao existe")
        return render(request, 'blog-home.html')

    return render(request, 'blog-home.html')


def modify_user(request):
    if not Participante.objects.filter(request.session['user_id']).name.exist():
        username = Utilizador.objects.get(request.session['user_id'])
        Utilizador.username = username
    elif Participante.objects.filter(request.session['user_id']).exist():
        messages.error(request, "Username already taken")
        return render(request, 'profile.html')


def profile(request):
    id = request.session['user_id']
    name = Utilizador.objects.get(idutilizador=id).nome
    if Utilizador.objects.get(idutilizador=id).username == '':
        username = Utilizador.objects.get(idutilizador=id).nome
    else:
        username = Utilizador.objects.get(idutilizador=id).username
    email = Utilizador.objects.get(idutilizador=id).email
    telefone = Utilizador.objects.get(idutilizador=id).telefone
    form = ModifyForm()
    if request.method == 'POST':
        if request.POST['persona'] == "1":
            if Participante.objects.filter(utilizador_idutilizador=id).exists():
                funcao = "Participante"
                return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'username': username, 'email': email, 'telefone': telefone, 'funcao': funcao})
            elif Administrador.objects.filter(utilizador_idutilizador=id).exists():
                funcao = "administardor"
                return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao})
            elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
                funcao = "docente Univesitario"
                IDUO = ProfessorUniversitario.objects.get(
                    utilizador_utilizadorid=id).unidade_organica_iduo
                return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'Iduo': IDUO})
            elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
                funcao = "Coordenador"
                idUO = Coordenador.objects.get(
                    utilizador_utilizadorid=id).unidade_organica_iduo
                return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'Iduo': IDUO})
            elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
                ano = Colaborador.objects.get(
                    utilizador_utilizadorid=id).dia_aberto_ano
                funcao = "Colaborador"
                curso = Colaborador.objects.get(
                    utilizador_utilizadorid=id).curso
                return render(request, 'profile_modify.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso})
    if Participante.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Participante"
        return render(request, 'profile.html', {"form": form, 'nome': name, 'username': username, 'email': email, 'telefone': telefone, 'funcao': funcao})
    elif Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "administardor"
        return render(request, 'profile.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao})
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "docente Univesitario"
        IDUO = ProfessorUniversitario.objects.get(
            utilizador_idutilizador=id).unidade_organica_iduo
        return render(request, 'profile.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'Iduo': IDUO})
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        idUO = Coordenador.objects.get(
            utilizador_utilizadorid=id).unidade_organica_iduo
        return render(request, 'profile.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'Iduo': IDUO})
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        ano = Colaborador.objects.get(
            utilizador_utilizadorid=id).dia_aberto_ano
        funcao = "Colaborador"
        curso = Colaborador.objects.get(utilizador_idutilizador=id).curso
        return render(request, 'profile.html', {"form": form, 'nome': name, 'email': email, 'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso})


def change_password(request, id):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Palavra atualizada co sucesso')
            return redirect('')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


def reset(request):
    sub = EmailSender()
    if request.method == 'POST':
        sub = EmailSender(request.POST)
        recepient = request.POST['email']
        if Utilizador.objects.filter(email=recepient).exists():
            subject = 'Recuperação da Palavra-Passe'
            id = make_password(
                str(Utilizador.objects.get(email=recepient).idutilizador))
            message = 'Para recuperar a sua palavra-passe re-introduza uma palavra-passe nova, no seguinte link: <a href=http://127.0.0.1:8000/' + \
                id+'>http://127.0.0.1:8000/'+id+'</a>'
            send_mail(subject, message, 'a61098@ualg.pt', [recepient],fail_silently=False)
            messages.success(request, f'Verifique o seu email')
            return render(request, 'reset.html', {'form': sub})
        else:
            message.error(request, f'Email incorreto')
    return render(request, 'reset.html', {'form': sub})

def change_pass(request):
    form=


def validacoes(request):
    if request.POST == 'POST':
        if Coordenador.objects.filter(utilizador_utilizadorid=request.session['user_id']).exists():
            user = Utilizador.objects.get(validada=1)
    return render(request, "validacoes.html", {"users": user})

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm, ModifyForm, PasswordChangeForm, EmailSender, DeleteUser
from django.core.mail import send_mail
from django.core import signing
from .models import UnidadeOrganica, DiaAberto,Departamento, Utilizador, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, DjangoSession, Curso
from django.db.models import CharField, Value
import datetime
import re

def user(request):
    funcao=None
    if 'user_id' in request.session:
        id1=request.session['user_id']
        if Participante.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "Participante"
        elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "docente Univesitario"
        elif Administrador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "administardor"
        elif Coordenador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "Coordenador"
        elif Colaborador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "colab"
        id=signing.dumps(id1)
    return funcao
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

def type_user(data,user_id):
    t=True
    #print(data['departamento']==0)
    #print(type(data['departamento']))
    if data['funcao']=='1':
        if len(data['curso'])>0 and user_id is not None:
            colab=Colaborador(pk=user_id,curso=data['curso'],preferencia=data['Perferencias'],dia_aberto_ano=DiaAberto.objects.get(pk=datetime.date.today().year))
            colab.save()
        elif len(data['curso'])==0:
            t=1
            return t
    elif data['funcao']=='2' :
        if data['UO']!=0 and user_id is not None:
            #print("\n"+t)
            Coord=Coordenador(pk=user_id,unidade_organica_iduo=UnidadeOrganica.objects.get(pk=data['UO']))
            Coord.save()
        elif data['UO']==0:
            t=2
            #print("\n"+t)
            return t
    elif data['funcao']=='3' :
        if data['departamento']!='0' and user_id is not None:
            DC=ProfessorUniversitario.objects.create(pk=user_id,departamento_iddepartamento=Departamento.objects.get(pk=data['departamento'].split("_")[1]))
        elif data['departamento']=='0':
            t=3
            return t
    elif data['funcao']=='4':
        if user_id is not None:
            admin=Administrador(pk=user_id)
            admin.save()
        else:
            t=4
            return t
    return t


def validateEmail(email):
    return re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)

def dep():
    deps=Departamento.objects.all().annotate(value=Value("",CharField()))
    for dep in deps:
        uo=dep.unidade_organica_iduo
        dep.value=str(uo.pk)+"_"+str(dep.pk)
        print(dep.value)
    return deps

def curso():
    deps=Curso.objects.all().annotate(value=Value("",CharField()))
    for dep in deps:
        uo=dep.unidade_organica_iduo
        dep.value=str(uo.pk)+"_"+str(dep.pk)
        print(dep.value)
    return deps

def register(request):
    UOs=UnidadeOrganica.objects.all()
    deps=dep()
    cursos=curso()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        data=request.POST
        print(form.is_valid())
        if len(data['name'])>0 and len(data['username'])>0 and len(data['email'])>0 and len(data['password1'])>0 and validateEmail(data['email']) and type_user(data,None) and request.POST['password1']==request.POST['password2'] and not Utilizador.objects.filter(email=request.POST['email']).exists() and  not Utilizador.objects.filter(telefone=request.POST['telefone']).exists() and password_check(request.POST['password1']) is True:
            form.save()
            user_id=Utilizador.objects.get(email=request.POST['email']).idutilizador
            type_user(data,user_id)
            part = Participante(pk=user_id)
            part.save()
            messages.success(request, f'Registo feito com Sucesso!')
            return redirect('blog-home')
        else:
            error=False
            error3=False
            error2=False
            error1=False
            if request.POST['email']=="":
                error = 'Preencha este campo.'
            if request.POST['telefone']=="":    
                error3 = 'Preencha este campo.'
            if request.POST['password1']=="":
                error1 = 'Preencha este campo.'
            if request.POST['password2'] =="":
                error2 = 'Preencha este campo.'
            if Utilizador.objects.filter(email=request.POST['email']).exists():
                error = "Email ja existe"
            elif not validateEmail(data['email']):
                error="Formato do email errado."
            if Utilizador.objects.filter(telefone=request.POST['telefone']).exists():
                error3 = "telefone ja existe"
            if request.POST['password1'] != request.POST['password2']:
                error2 = "Passwords nao coincidem"
            if not password_check(request.POST['password1']):
                error1 = password_check(request.POST['password1']) 
            return render(request, 'register.html', {'form': form,'cursos':cursos,'UOs':UOs,'deps':deps,'error1': error, 'error2': error1, 'error3': error2, 'error4': error3,'error5':type_user(data,None)})
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form,'UOs':UOs,'deps':deps,'cursos':cursos,"func":user(request)})

#*----------------------------------------------------------login---------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        tentatives=int(request.POST['tentatives'])
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
                tentatives-=1
                messages.error(request, f"Username e/ou palavra-passe. Tem mais {tentatives} tentativas")
        else:
            tentatives-=1
            messages.error(request, f"Username e/ou palavra-passe. Tem mais {tentatives} tentativas")
    else:
        tentatives=5
        form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"form": form,"tentatives":tentatives})


def logout_request(request):
    r = redirect("blog-home")
    del request.session['user_id']
    if 'cookie_id' in request.COOKIES:
        r.delete_cookie('cookie_id')
    messages.info(request, "saiste com sucesso")
    return r

#----------------------------------------------remover user-----------------------------------
def delete_user(request,id):
    id=signing.loads(id)
    Utilizador.objects.filter(pk=id).delete()
    Participante.objects.filter(pk=id).delete()
    Administrador.objects.filter(pk=id).delete()
    Coordenador.objects.filter(pk=id).delete()
    Colaborador.objects.filter(pk=id).delete()
    ProfessorUniversitario.objects.filter(pk=id).delete()
    return redirect("profile_list")

#--------------------------------------alterar user---------------------------------------------
def modify_user(request,id):
    id=signing.loads(id)
    name = Utilizador.objects.get(idutilizador=id).nome
    me=request.session['user_id']
    if request.method=='POST':
        form=ModifyForm(request.POST)
        if request.POST['name']!="" and request.POST['username']!="" and request.POST['email']!="" and not Utilizador.objects.filter(email=request.POST['email']).exists() and not Utilizador.objects.filter(telefone=request.POST['telefone']).exists() and request.POST['telefone']!="" and validateEmail(request.POST['email']):
            t=Utilizador.objects.get(pk=id)
            t.nome=request.POST['name']
            t.username=request.POST['username']
            t.email=request.POST['email']
            t.telefone=request.POST['telefone']
            t.save()
            return redirect('blog-home')
        else:
            error=False
            error3=False
            data=request.POST
            username=data['username']
            telefone=data['telefone']
            funcao=data['funcao']
            email=data['email']
            curso=False
            dep=False
            UO=False
            if 'curso' in data:
                curso=data['curso']
            if 'dep' in data:
                dep=data['dep']
            if 'UO' in data:
                UO=data['UO']
            if request.POST['email']=="":
                error = 'Preencha este campo.'
            if request.POST['telefone']=="":    
                error3 = 'Preencha este campo.'
            if Utilizador.objects.filter(email=request.POST['email']).exists() and Utilizador.objects.get(email=request.POST['email']).idutilizador!=id:
                error = "Email ja existe"
            if Utilizador.objects.filter(telefone=request.POST['telefone']).exists() and Utilizador.objects.get(telefone=request.POST['telefone']).idutilizador!=id:
                error3 = "telefone ja existe"
            return render(request, 'profile_modify.html', {'email':email,'UO':UO,'username':username,'telefone':telefone,'funcao':funcao,'curso':curso,'dep':dep,"form": form,'error4':error3,"error1":error,'me':signing.dumps(me),'id':signing.dumps(id),'nome':name})
    else:
        form = ModifyForm()
        if Utilizador.objects.get(idutilizador=id).username == '':
            username = Utilizador.objects.get(idutilizador=id).nome
        else:
            username = Utilizador.objects.get(idutilizador=id).username
        email = Utilizador.objects.get(idutilizador=id).email
        telefone = Utilizador.objects.get(idutilizador=id).telefone
    UO=False
    dep=False
    ano=False
    curso=False
    funcao=False
    if Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Administardor"
    elif Participante.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Participante"
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Docente Univesitario"
        depid = ProfessorUniversitario.objects.get(utilizador_idutilizador=id).departamento_iddepartamento
        dep= Departamento.objects.get(pk=depid.pk).nome
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
        UO=UnidadeOrganica.objects.get(pk=IDUO.pk).sigla
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        ano = Colaborador.objects.get(utilizador_utilizadorid=id).dia_aberto_ano
        funcao = "Colaborador"
        curso = Colaborador.objects.get(utilizador_idutilizador=id).curso
    return render(request, 'profile_modify.html', {"form": form, 'nome': name,'UO':UO,'username': username, 'email': email, 
                    'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso,'dep':dep,"me":signing.dumps(me),'id':signing.dumps(id),'func':user(request)})

def profile(request,id):
    id=signing.loads(id)
    name = Utilizador.objects.get(idutilizador=id).nome
    me=request.session['user_id']
    form = ModifyForm()
    if Utilizador.objects.get(idutilizador=id).username == '':
        username = Utilizador.objects.get(idutilizador=id).nome
    else:
        username = Utilizador.objects.get(idutilizador=id).username
    email = Utilizador.objects.get(idutilizador=id).email
    telefone = Utilizador.objects.get(idutilizador=id).telefone
    UO=False
    dep=False
    ano=False
    curso=False
    funcao=False
    if Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "administardor"
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Docente Univesitario"
        depid = ProfessorUniversitario.objects.get(utilizador_idutilizador=id).departamento_iddepartamento
        dep= Departamento.objects.get(pk=depid.pk).nome
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
        UO=UnidadeOrganica.objects.get(pk=IDUO.pk).sigla
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        ano = Colaborador.objects.get(utilizador_utilizadorid=id).dia_aberto_ano
        funcao = "Colaborador"
        curso = Colaborador.objects.get(utilizador_idutilizador=id).curso
    return render(request, 'profile.html', {"form": form, 'nome': name,'UO':UO,'username': username, 'email': email, 
                    'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso,'dep':dep,"me":signing.dumps(me),'id':signing.dumps(id),'func':user(request)})

def profile_list(request):
    funcao=user(request)
    me=Utilizador.objects.get(pk=request.session['user_id'])
    users=Utilizador.objects.all().annotate(cargo=Value('',CharField()),estado=Value('Pendente',CharField()),UO=Value('-',CharField()))
    for u in users:
        if Coordenador.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Coordenador"
            u.UO=UnidadeOrganica.objects.get(pk=Coordenador.objects.get(pk=u.idutilizador).unidade_organica_iduo).sigla
            if u.validada==2:
                u.estado="Validado"
        elif Colaborador.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Colaborador"
            u.UO=UnidadeOrganica.objects.get(pk=Curso.objects.get(pk=Colaborador.objects.get(pk=u.idutilizador).curso_idcurso).unidade_organica_iduo).sigla
            if u.validada==1:
                u.estado="Validado"
        elif ProfessorUniversitario.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Docente Universitario"
            dep=ProfessorUniversitario.objects.get(pk=u.idutilizador).departamento_iddepartamento
            u.UO=UnidadeOrganica.objects.get(pk=dep.pk).sigla
            if u.validada==3:
                u.estado="Validado"
        elif Administrador.objects.filter(pk=u.pk).exists():
            u.cargo="Administrador"
            if u.validada==4:
                u.estado="Validado"
        u.idutilizador=signing.dumps(u.idutilizador)
    id=signing.dumps(request.session['user_id'])
    return render(request,"list_users.html",{"users":users,"funcao":funcao,"id":id,'me':me})
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
def validacoes(request,acao,id):
    id=signing.loads(id)
    user=Utilizador.objects.get(pk=id)
    if acao==1:
        if Colaborador.objects.filter(pk=id).exists():
            user.validada=1
            Participante.objects.filter(pk=id).delete()
        elif Coordenador.objects.filter(pk=id).exists():
            user.validada=2
            Participante.objects.filter(pk=id).delete()
        elif ProfessorUniversitario.objects.filter(pk=id).exists():
            user.validada=3
            Participante.objects.filter(pk=id).delete()
        elif Administrador.objects.filter(pk=id).exists():
            user.validada=4
            Participante.objects.filter(pk=id).delete()
        user.save()
    else:
        user.validada=5
        user.save()
    return redirect('profile_list')

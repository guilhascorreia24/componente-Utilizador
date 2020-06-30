from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm, AuthenticationForm, ModifyForm, PasswordChangeForm, EmailSender, DeleteUser
from django.core.mail import message, send_mail
from django.core import signing
from .models import UnidadeOrganica, DiaAberto,Departamento, Utilizador, Participante, ProfessorUniversitario, Administrador,Coordenador, Colaborador, DjangoSession, Curso, InscricaoColetiva, InscricaoIndividual, Atividade,Tarefa, Campus, Disponibilidade
from django.db.models import CharField, Value, IntegerField
from Notification import views as noti_views
from Notification import views as noti_not_checked
import datetime
import re
import hashlib
from cryptography.fernet import Fernet
import base64
import logging
import traceback
import json
from django.conf import settings
from Notification.views import *
from django.views.decorators.csrf import csrf_exempt
import hashlib

def encrypt(txt):
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        return encrypted_text
def decrypt(txt):
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
        return decoded_text


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
        id=encrypt(id1)
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

def type_user(data,user_id,request):
    t=True
    #print(data['departamento']==0)
    #print(type(data['departamento']))
    if data['funcao']=='1':
        if data['curso']!='0' and user_id is not None:
            curso_id=Curso.objects.get(pk=data['curso'].split("_")[1])
            colab=Colaborador(pk=user_id,curso_idcurso=curso_id)
            colab.save()
        elif data['UO']=='0' or data['curso']=='0':
            t=1
            return t
    elif data['funcao']=='2' :
        if data['UO']!=0 and user_id is not None:
            #print("\n"+t)
            Coord=Coordenador(pk=user_id,unidade_organica_iduo=UnidadeOrganica.objects.get(pk=data['UO']))
            Coord.save()
        elif data['UO']=='0':
            t=2
            #print("\n"+t)
            return t
    elif data['funcao']=='3' :
        if data['departamento']!='0' and user_id is not None:
            DC=ProfessorUniversitario.objects.create(pk=user_id,departamento_iddepartamento=Departamento.objects.get(pk=data['departamento'].split("_")[1]))
        elif data['UO']=='0' or data['departamento']=='0':
            t=3
            return t
    elif data['funcao']=='4':
        if user_id is not None:
            admin=Administrador(pk=user_id)
            #if len(Administrador.objects.all())==0:
             #   Utilizador.objects.filter(pk=user_id).update(validada=4)
            admin.save()
        else:
            t=4
            return t
    elif data['funcao']=='0':
        if user_id is not None:
            part = Participante(pk=user_id)
            part.save()
            Utilizador.objects.filter(pk=user_id).update(validada=0)
            noti_views.new_noti(request,user_id,'Bem-vindo','Seja bem-vindo ao site do dia aberto')
    return t


def validateEmail(email):
    return bool(re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email))

def dep():
    deps=Departamento.objects.all().annotate(value=Value("",CharField()))
    for dep in deps:
        uo=dep.unidade_organica_iduo
        dep.value=str(uo.pk)+"_"+str(dep.pk)
       # print(dep.value)
    return deps

def curso():
    deps=Curso.objects.all().annotate(value=Value("",CharField()))
    for dep in deps:
        uo=dep.unidade_organica_iduo
        dep.value=str(uo.pk)+"_"+str(dep.pk)
        #print(dep.value)
    return deps

def register(request):
    me=None
    #print("enter"+str(not('user_id' in request.session) and not('type' in request.session)))
    if 'user_id' in request.session and request.session['type']!=4:
        context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
        return render(request,"not_for-u.html",context)
    elif ('user_id' in request.session) and ('type' in request.session):
        if request.session['type']!=4:
            ontext={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
            return render(request,"not_for-u.html",context)
    if 'user_id' in request.session:
        me=request.session['user_id']
    UOs=UnidadeOrganica.objects.all()
    deps=dep()
    cursos=curso()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        data=request.POST
        form.is_valid()
        #print(data)
        #print(len(data['name'])>0)
        #print(len(data['email'])>0)
        #print(len(data['password1'])>0)
        #print(validateEmail(data['email']))
        #print(type_user(data,None))
        #print(request.POST['password1']==request.POST['password2'])
        #print(not Utilizador.objects.filter(email=request.POST['email']).exists())
        #print(not Utilizador.objects.filter(telefone=request.POST['telefone']).exists())
        #print(password_check(request.POST['password1']))
        if (len(data['name'])>0 and len(data['name'])<255) and (len(data['email'])>0 and len(data['email'])<255) and (len(data['password1'])>0 and len(data['password1'])<255) and validateEmail(data['email']) and (type_user(data,None,request) is True or type_user(data,None,request) == 4) and request.POST['password1']==request.POST['password2'] and not Utilizador.objects.filter(email=request.POST['email']).exists() and password_check(request.POST['password1']) is True:
            form.save()
            user_id=Utilizador.objects.get(email=request.POST['email']).idutilizador
            type_user(data,user_id,request)
            if 'user_id' in request.session:
                validacoes(request,1,user_id)
            messages.success(request, f'Registo efetuado com Sucesso!')
            return redirect('blog:blog-home')
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
            if request.POST['password1'] != request.POST['password2']:
                error2 = "Passwords nao coincidem"
            if password_check(request.POST['password1']) != True:
                error1 = password_check(request.POST['password1']) 
            return render(request, 'register.html', {'me':me,"func":user(request),'form': form,'cursos':cursos,'UOs':UOs,'deps':deps,'error1': error, 'error2': error1, 'error3': error2, 'error4': error3,'error5':type_user(data,None,request),'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'p':1})
    form = UserRegisterForm()
    return render(request, 'register.html', {'form': form,'UOs':UOs,'deps':deps,'cursos':cursos,"func":user(request),'me':me,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'p':1})

#*----------------------------------------------------------login---------------------------------------
def login_request(request):
    if 'user_id' in request.session:
        context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
        return render(request,"not_for-u.html",context)
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        tentatives=int(request.POST['tentatives'])
        #print(request.POST['email'])
        #print(request.POST['password'])
        #print(tentatives)
        if request.POST['email'] != '' and request.POST['password'] != '':
            #print(signing.dumps(request.POST['password']))
            if Utilizador.objects.filter(email=request.POST['email'], password=hashlib.sha256(request.POST['password'].encode('utf-8')).hexdigest()).exists():
                username = Utilizador.objects.get( email=request.POST['email'])
                if username.validada != int(5):
                    messages.success(request, f"Bem-vindo {username.nome}")
                    user = Utilizador.objects.get(email=request.POST['email'])
                    request.session['user_id'] = user.idutilizador
                    request.session['type'] = user.validada
                    request.session['id_encrypt']=user.pk
                    #print(request.session['user_id'])
                    r = redirect('blog:blog-home')
                    if 'check' in request.POST and request.POST['check'] == '1':
                        Utilizador.objects.filter(pk=request.session['user_id']).update(remember_me=encrypt(request.session['user_id']))
                        r.set_cookie('cookie_id', encrypt(request.session['user_id']), 7 * 24 * 60 * 60)
                    return r
                else:
                    tentatives-=1
                    messages.error(request, f"Sua conta ainda não está validada")
            else:
                tentatives-=1
                messages.error(request, f"Username e/ou palavra-passe. Tem mais {tentatives} tentativas")
        else:
            tentatives-=1
            messages.error(request, f"Username e/ou palavra-passe. Tem mais {tentatives} tentativas")
    else:
        tentatives=5
        form = AuthenticationForm()
    if tentatives<0:
        tentatives=5
    return render(request=request, template_name="login.html", context={"form": form,"tentatives":tentatives,'p':2})


def logout_request(request):
    r = redirect("blog:blog-home")
    if 'user_id' in request.session:
        print(request.session['user_id'])
        del request.session['user_id']
        del request.session['type']
    if 'cookie_id' in request.COOKIES:
        Utilizador.objects.filter(remember_me=request.COOKIES['cookie_id']).delete()
        r.delete_cookie('cookie_id')
    print(request.session)
    messages.success(request, "Até a proxima")
    return r

#----------------------------------------------remover user-----------------------------------
def delete_user(request,id):
    u=Utilizador.objects.filter(pk=id)
    admin=Administrador.objects.filter(pk=id)
    prof=ProfessorUniversitario.objects.filter(pk=id)
    coord=Coordenador.objects.filter(pk=id)
    part=Participante.objects.filter(pk=id)
    colab=Colaborador.objects.filter(pk=id)
    if Utilizador.objects.get(pk=id).validada == 5:
        u.delete()
    if admin.exists() and not(DiaAberto.objects.filter(administrador_utilizador_idutilizador=id).exists()):
        u.delete()
        admin.delete()
        messages.success(request, f'Utilizador eliminado com sucesso')
    elif prof.exists() and (not Atividade.objects.filter(professor_universitario_utilizador_idutilizador=id).exists()):
        u.delete()
        prof.delete()
        messages.success(request, f'Utilizador eliminado com sucesso')
    elif part.exists() and (not InscricaoColetiva.objects.filter(participante_utilizador_idutilizador=id).exists() or not InscricaoIndividual.objects.filter(participante_utilizador_idutilizador=id).exists()):
        u.delete()
        part.delete()
        messages.success(request, f'Utilizador eliminado com sucesso')
    elif (coord.exists()  and not Tarefa.objects.filter(coordenador_utilizador_idutilizador=id).exists()):
        u.delete()
        coord.delete()
        messages.success(request, f'Utilizador eliminado com sucesso')
    elif colab.exists() and not Tarefa.objects.filter(colaborador_utilizador_idutilizador=id).exists():
        u.delete()
        colab.delete()
        messages.success(request, f'Utilizador eliminado com sucesso')
    else:
        messages.success(request, f'Impossivel de eliminar o utilizador')
        if admin.exists() and (DiaAberto.objects.filter(administrador_utilizador_idutilizador=id).exists()):
            messages.success(request,f'Utilizador esta responsavel por Dia(s) Aberto(s)')
        elif prof.exists() and (Atividade.objects.filter(professor_universitario_utilizador_idutilizador=id).exists()):
            messages.success(request,f'Utilizador tem Atividades associadas')
        elif part.exists() and ( InscricaoColetiva.objects.filter(participante_utilizador_idutilizador=id).exists() or  InscricaoIndividual.objects.filter(participante_utilizador_idutilizador=id).exists()):
            messages.success(request,f'Utilizador tem inscrição associadas')
        elif (coord.exists()  and  Tarefa.objects.filter(coordenador_utilizador_idutilizador=id).exists()):
            messages.success(request,f'Utilizador tem Tarefa associadas')
        elif colab.exists() and  Tarefa.objects.filter(colaborador_utilizador_idutilizador=id).exists():
            messages.success(request,f'Utilizador tem Tarefa associadas')
    return redirect("profile_list")

#--------------------------------------alterar user---------------------------------------------
def modify_user(request,id):
    #print(id!=request.session['user_id'] or not(Administrador.objects.filter(pk=request.session['user_id']).exists()))
    if id!=request.session['user_id'] and not(Administrador.objects.filter(pk=request.session['user_id']).exists()):
        context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
        return render(request,"not_for-u.html",context)
    name = Utilizador.objects.get(idutilizador=id).nome
    me=request.session['user_id']
    if request.method=='POST':
        form=ModifyForm(request.POST)
        print(request.POST['name']!="")
        print(request.POST['email']!="")
        print(not Utilizador.objects.filter(email=request.POST['email']).exists() )
        print(not Utilizador.objects.filter(telefone=request.POST['telefone']).exists())
        print(request.POST['telefone']!="")
        print(bool(validateEmail(request.POST['email'])))
        if (request.POST['name']!="")  and (request.POST['email']!="") and (not(Utilizador.objects.filter(email=request.POST['email']).exists()) or Utilizador.objects.get(pk=id).email==request.POST['email']) and (request.POST['telefone']!="") and (validateEmail(request.POST['email'])):
            t=Utilizador.objects.get(pk=id)
            t.nome=request.POST['name']
            t.email=request.POST['email']
            t.telefone=request.POST['telefone']
            if t.validada==5:
                t.validada=0
            t.save()
            print("1")
            noti_views.new_noti(request,t.pk,'Alteração de dados no perfil','Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.')
            messages.success(request, f"Utilizador alterado com sucesso")
            return redirect('profile_list')
        else:
            error=False
            error3=False
            data=request.POST
            telefone=data['telefone']
            funcao=data['funcao']
            email=data['email']
            curso=False
            dep=False
            UO=False
            ano=False
            if 'ano' in data:
                ano=data['ano']
            if 'curso' in data:
                curso=data['curso']
            if 'dep' in data:
                dep=data['dep']
            if 'UO' in data:
                UO=data['UO']
            if request.POST['telefone']=="":    
                error3 = 'Preencha este campo.'
            if Utilizador.objects.filter(email=request.POST['email']).exists() and Utilizador.objects.get(email=request.POST['email']).idutilizador!=id:
                error = "Email ja existe"
            return render(request, 'profile_modify.html', {'email':email,'UO':UO,'telefone':telefone,'funcao':funcao,'curso':curso,'dep':dep,"form": form,'error4':error3,"error1":error,'me':me,'id':id,'nome':name,'ano':ano,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
    else:
        form = ModifyForm()
        email = Utilizador.objects.get(idutilizador=id).email
        telefone = Utilizador.objects.get(idutilizador=id).telefone
    UO=False
    dep=False
    ano=False
    curso=False
    funcao=False
    atual=datetime.now().year
    u=Utilizador.objects.get(pk=id)
    if Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Administardor"
        ano=year(u,atual)
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Docente Univesitario"
        depid = ProfessorUniversitario.objects.get(utilizador_idutilizador=id).departamento_iddepartamento
        dep= Departamento.objects.get(pk=depid.pk).nome
        UO=depid.unidade_organica_iduo.sigla
        ano=year(u,atual)
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
        UO=UnidadeOrganica.objects.get(pk=IDUO.pk).sigla
        ano=year(u,atual)
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Colaborador"
        cursoid=Colaborador.objects.get(utilizador_idutilizador=id).curso_idcurso
        UO=Curso.objects.get(pk=cursoid.pk).unidade_organica_iduo.sigla
        ano=year(u,atual)
    elif Participante.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Participante"
        ano=year(u,atual)
    return render(request, 'profile_modify.html', {"form": form, 'nome': name,'UO':UO, 'email': email, "ano":ano,
                    'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': curso,'dep':dep,"me":me,'id':id,'func':user(request),'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def profile(request,id):
    id=id
    #print(id!=request.session['user_id'] and not(Administrador.objects.filter(pk=request.session['user_id']).exists()))
    if not(Administrador.objects.filter(pk=request.session['user_id']).exists()) and not(Coordenador.objects.filter(pk=request.session['user_id']).exists()):
        context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
        return render(request,"not_for-u.html",context)
    name = Utilizador.objects.get(idutilizador=id).nome
    me=request.session['user_id']
    form = ModifyForm()
    email = Utilizador.objects.get(idutilizador=id).email
    telefone = Utilizador.objects.get(idutilizador=id).telefone
    UO=False
    dep=False
    ano=False
    cursoname=False
    funcao=False
    if Administrador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "administardor"
    elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Docente Univesitario"
        depid = ProfessorUniversitario.objects.get(utilizador_idutilizador=id).departamento_iddepartamento
        dep= Departamento.objects.get(pk=depid.pk).nome
        UO=UnidadeOrganica.objects.get(pk=depid.unidade_organica_iduo.pk).sigla
    elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
        funcao = "Coordenador"
        IDUO = Coordenador.objects.get(pk=id).unidade_organica_iduo
        UO=UnidadeOrganica.objects.get(pk=IDUO.pk).sigla
    elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
        #ano = Utilizador.objects.get(pk=id).dia_aberto_ano.pk 
        funcao = "Colaborador"
        curso=Colaborador.objects.get(utilizador_idutilizador=id).curso_idcurso
        cursoname=curso.nome
        UO=UnidadeOrganica.objects.get(pk=curso.unidade_organica_iduo.pk).sigla
    elif Participante.objects.filter(pk=id).exists():
        funcao="Participante"
    return render(request, 'profile.html', {"form": form, 'nome': name,'UO':UO, 'email': email,"ano":ano,
                    'telefone': telefone, 'funcao': funcao, 'ano': ano, 'curso': cursoname,'dep':dep,"me":me,'id':id,'func':user(request),'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})



def uo():
    uos=UnidadeOrganica.objects.all().annotate(value=Value("",CharField()))
    for uo in uos:
        camp=uo.campus_idcampus
        uo.value=str(camp.pk)+"_"+str(uo.pk)
    return uos

def year(u,atual):
    n=Notificacao.objects.filter(idutilizadorenvia=u.pk)
    if u.dia_aberto_ano!=None:
        u.year=u.dia_aberto_ano.ano
    elif u.dia_aberto_ano==None and n.exists():
        u.year=n.order_by('-criadoem')[0].criadoem.year
        n=Notificacao.objects.filter(utilizadorrecebe=u.pk)
        if n.exists() and n.order_by('-criadoem')[0].criadoem.year<u.year:
            u.year=n.order_by('-criadoem')[0].criadoem.year
    else:
        u.year=atual
    return  u.year

def profile_list(request):
    funcao=user(request)
    user_id=request.session['user_id']
    #print("can_enter:"+str(not(Coordenador.objects.filter(pk=request.session['user_id']).exists()) or not(Administrador.objects.filter(pk=request.session['user_id']).exists())))
    if not(Coordenador.objects.filter(pk=request.session['user_id']).exists()) and not(Administrador.objects.filter(pk=request.session['user_id']).exists()) or not('user_id' in request.session):
        context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
        return render(request,"not_for-u.html",context)
    users=Utilizador.objects.all().annotate(cargo=Value('Participante',CharField()),estado=Value('Pendente',CharField()),UO=Value('-',CharField()), no_enc=Value(0,IntegerField()),year=Value(0,IntegerField()))
    atual=datetime.now().year
    for u in users:
        if Coordenador.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Coordenador"
            u.UO=UnidadeOrganica.objects.get(pk=Coordenador.objects.get(pk=u.idutilizador).unidade_organica_iduo.pk).sigla
            if u.validada==2:
                u.estado="Validado"
            u.year=year(u,atual)
        elif Colaborador.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Colaborador"
            curso_id=Colaborador.objects.get(pk=u.pk).curso_idcurso.pk
            u.UO=UnidadeOrganica.objects.get(pk=Curso.objects.get(pk=curso_id).unidade_organica_iduo.pk).sigla
            if u.validada==1:
                u.estado="Validado"
            u.year=year(u,atual)
        elif ProfessorUniversitario.objects.filter(pk=u.idutilizador).exists():
            u.cargo="Docente Universitario"
            dep=ProfessorUniversitario.objects.get(pk=u.idutilizador).departamento_iddepartamento
            u.UO=UnidadeOrganica.objects.get(pk=dep.unidade_organica_iduo.pk).sigla
            if u.validada==3:
                u.estado="Validado"
            u.year=year(u,atual)
        elif Administrador.objects.filter(pk=u.pk).exists():
            u.cargo="Administrador"
            if u.validada==4:
                u.estado="Validado"
            u.year=year(u,atual)
        elif Participante.objects.filter(pk=u.pk).exists():
            u.estado="Validado"
            u.year=year(u,atual)
        #print(str(u.idutilizador)+" "+str(user_id))
        u.no_enc=u.pk
        u.idutilizador=u.idutilizador
    if Coordenador.objects.filter(pk=user_id).exists():
        me=UnidadeOrganica.objects.get(pk=Coordenador.objects.get(pk=user_id).unidade_organica_iduo.pk).sigla
    elif Administrador.objects.filter(pk=user_id).exists():
        me=Administrador.objects.get(pk=user_id)
        me.sigla=None
    me_id=user_id
    campus=Campus.objects.all()
    uos=uo()
    #print(users)
    return render(request,"list_users.html",{'atual':atual,"users":users,"funcao":funcao,"me":me,"me_id":me_id,"campus":campus,"uos":uos,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'colaboradores':Colaborador.objects.all(),'docentes':ProfessorUniversitario.objects.all()})
#--------------------------------------------recuperaçao de password---------------------------------
def change_password(request, id):
    id_deccryp=decrypt(id)
    if request.method=='POST':
        form=PasswordChangeForm(request.POST)
        passwd=request.POST['password']
        if form.is_valid and password_check(passwd) is True:
            t=Utilizador.objects.get(pk=id_deccryp)
            t.password=hashlib.sha256(passwd.encode('utf-8')).hexdigest()
            t.save()
            messages.success(request, f'Password alterada com sucesso')
            return redirect('blog:blog-home')
        else:
            messages.error(request,password_check(passwd))
            if request.POST['confirm_password']!=passwd:
                error=True
                return render(request,"reset_password.html",{"form":form,"error":error})
    else:
        form=PasswordChangeForm()
    return render(request,"reset_password.html",{"form":form})


def reset(request):
    message=None
    sub = EmailSender()
    if request.method == 'POST':
        sub = EmailSender(request.POST)
        recepient = request.POST['email']
        sub.is_valid()
        if Utilizador.objects.filter(email=recepient).exists():
            subject = 'Recuperação da Palavra-Passe'
            p=Utilizador.objects.get(email=recepient).idutilizador
            id = encrypt(p)
            message = str("Para recuperar a sua palavra-passe re-introduza uma palavra-passe nova, no seguinte link: "+request.build_absolute_uri(id))
            send_mail(subject, message, 'diabertoworking@gmail.com', [recepient])
            messages.success(request, f'Verifique o seu email')
            return render(request, 'reset.html', {'form': sub})
        else:
            message='Email incorreto'
            return render(request, 'reset.html', {'form': sub,'message':message,'p':2})
    return render(request, 'reset.html', {'form': sub,'p':2})
#-------------------------------------------------validacoes---------------------------------------------------------------
def validacoes(request,acao,id):
    if not (Administrador.objects.filter(pk=request.session['user_id']).exists() or Coordenador.objects.filter(pk=request.session['user_id']).exists()):
        redirect("blog:blog-home")
    id=id
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
        noti_views.new_noti(request,id,'Bem-vindo','Seja bem-vindo ao site do dia aberto')
        recepient=user.email
        from_user=Utilizador.objects.get(pk=request.session['user_id']).email
        subject="Validação da conta"
        message=str("A sua conta foi aceite. Faça login no seguinte link: "+request.build_absolute_uri().split("register")[0]+"login/")
        send_mail(subject,message,'diaabertoworking@gmail.com',[recepient])
        messages.success(request,f'Utilizador {user.nome} validado com sucesso.')
    else:
        recepient=user.email
        subject="Validação da conta"
        message=str("A sua conta nao foi aceite. Crie uma nova conta"+request.build_absolute_uri().split("validacoes")[0])
        send_mail(subject,message,'a61098@ualg.pt',[recepient])
        messages.success(request,f'Email enviado com sucesso')
        user.delete()
    return redirect('profile_list')

@csrf_exempt
def getUserType(request):
    if(request.method=='POST'):
        num = request.POST.get("id","")
        query = Utilizador.objects.get(idutilizador=num)
        num = query.validada
        return HttpResponse(json.dumps({'type': num}), content_type="application/json")

    raise Exception("Error")

def update_ano_user_null():
    atual=datetime.now().year
    users=Utilizador.objects.filter(dia_aberto_ano=None)
    if DiaAberto.objects.filter(ano=atual).exists():
        for user in users:
            Utilizador.objects.filter(pk=user.pk).update(dia_aberto_ano=DiaAberto.objects.get(ano=atual))


from django.shortcuts import render, redirect
from Notification import templates
from .models import Notificacao, Departamento, Utilizador, DjangoSession, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, UtilizadorHasNotificacao, UnidadeOrganica
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import signing
from django.contrib import messages
from user import views as user_views
from django.db.models import CharField, Value,IntegerField, DateTimeField
from datetime import datetime
from django.db.models.functions import Cast
from Notification.models import Curso

def createnot(request):
    list=[]
    me_id=request.session['user_id']
    funcao=user_views.user(request)
    contacts=get_my_lists(request,list)
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        emails=request.POST['Destinatario'].split(",")
        if form.is_valid():
            for email in emails:
                email=email.strip()
                form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
                if user_views.validateEmail(email) is True and (Utilizador.objects.filter(email=email).exists()):
                    if Utilizador.objects.filter(email=email).exists():
                        user_email = Utilizador.objects.get(email=email)
                elif email in list:
                    None
                else:
                    form.add_error('Destinatario','email invalido ou não existe')
                    messages.error(request,"Email Invalido")
                    return render(request, 'compor_not.html', {'form': form,'me_id':me_id,'funcao':funcao,'contacts':contacts})
            for email in emails:
                email=email.strip()
                if email in list:
                    send_to_org(email,request)
                else:
                    user_email = Utilizador.objects.get(email=email)
                    d=request.POST['Descricao']
                    a=request.POST['Assunto']
                    destinatario_pk= int(user_email.pk)
                    noti=Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
                    UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=user_email,notificacao=noti,estado=0)
                    if email!=Utilizador.objects.get(pk=request.session['user_id']).email:
                        UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=request.session['user_id']),notificacao=noti,estado=1)
            messages.success(request, 'Notificação enviada com sucesso')
            return redirect('check_not')
        else:
            for email in emails:
                email=email.strip()
                form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
                if user_views.validateEmail(email) is True and (Utilizador.objects.filter(email=email).exists()):
                    if Utilizador.objects.filter(email=email).exists():
                        user_email = Utilizador.objects.get(email=email)
                elif email in list:
                    None
                else:
                    form.add_error('Destinatario','email invalido ou não existe')
                    messages.error(request,"Email Invalido")
    else:
        form = NotificationForm()
    for f in form:
        print(type(f.errors))
    return render(request, 'compor_not.html', {'form': form,'me_id':me_id,'funcao':funcao,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'contacts':contacts})

def send_to_org(email,request):
    email=email.split(".")
    if email[0]=="Docentes":
        users_send=ProfessorUniversitario.objects.all()
        if len(email)==2:
            users_send=[]
            for dep in Departamento.objects.filter(unidade_organica_iduo=UnidadeOrganica.objects.get(sigla=email[1])):
                users_send=ProfessorUniversitario.objects.filter(departamento_iddepartamento=dep)
    if email[0]=="Coordenadores":
        users_send=Coordenador.objects.all()
        if len(email)==2:
            users_send=Coordenador.objects.filter(unidade_organica_iduo=UnidadeOrganica.objects.get(sigla=email[1]))
    if email[0]=="Colaboradores":
        users_send=Colaborador.objects.all()
        if len(email)==2:
            users_send=[]
            for curso in Curso.objects.filter(unidade_organica_iduo=UnidadeOrganica.objects.get(sigla=email[1])):
                users_send=Colaborador.objects.filter(curso_idcurso=curso)
    if email[0]=="Administradores":
        users_send=Administrador.objects.all()
    if email[0]=="Participantes":
        users_send=Participante.objects.all()
    for user in users_send:
        print(user)
        if user.pk != Utilizador.objects.get(pk=request.session['user_id']):
            d=request.POST['Descricao']
            a=request.POST['Assunto']
            destinatario_pk= int(user.pk)
            noti=Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
            UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=user.pk),notificacao=noti,estado=0)
            UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=request.session['user_id']),notificacao=noti,estado=1)

def has_noti(notis,noti):
    for n in notis:
        if noti.notificacao.pk==n.notificacao.pk:
            return True
    return False

def checknot(request):
    me_id=request.session['user_id']
    i=len(noti_not_checked(request))
    notis=[]
    nots=UtilizadorHasNotificacao.objects.all().annotate(emissor=Value("",CharField()))
    deletenot(request)
    for noti in nots:
        if noti.notificacao.utilizadorrecebe==me_id:
            print(notis)
        if noti.notificacao.utilizadorrecebe==me_id and not(has_noti(notis,noti)):
            if Utilizador.objects.filter(pk=noti.notificacao.idutilizadorenvia).exists():
                noti.emissor=Utilizador.objects.get(pk=noti.notificacao.idutilizadorenvia).email
            else:
                noti.emissor='Diaaberto@ualg.pt'
            noti.pk=noti.pk
            notis.append(noti)
    func=user_views.user(request)
    #print(func)
    return render(request,'check.html',{'nots':notis,'me_id':me_id,'funcao':func,'i':i,'not_checked':noti_not_checked(request)})

def deletenot(request):
    if request.method == 'POST':
        print(request.POST.getlist('noti'))
        pressed = request.POST.getlist('noti')
        for press in pressed:
            #print("eliminadas:"+str(signing.loads(press))) 
            UtilizadorHasNotificacao.objects.filter(pk=press).delete()
        messages.success(request, 'Notificação/Notificações eliminada(s)')
         
def enviados(request):
    me_id=request.session['user_id']
    notis=[]
    nots=UtilizadorHasNotificacao.objects.all().annotate(emissor=Value("",CharField()),recept=Value("",CharField()))
    deletenot(request)
    for noti in nots:
        if noti.notificacao.idutilizadorenvia==me_id and noti.utilizador_idutilizador.pk==noti.notificacao.utilizadorrecebe and not(has_noti(notis,noti)):
            noti.recept=Utilizador.objects.get(pk=noti.notificacao.utilizadorrecebe).email
            noti.pk=noti.pk
            notis.append(noti)
    func=user_views.user(request)
    my=True
    i=len(noti_not_checked(request))
    return render(request,'check.html',{'nots':notis,'me_id':me_id,'funcao':func,'my':my,'i':i,'not_checked':noti_not_checked(request)})

def noti(request,id):
    me_id=id
    noti=pk=UtilizadorHasNotificacao.objects.get(pk=me_id).notificacao
    destinatario=noti.utilizadorrecebe
    tipo="Destinatario"
    if request.session['user_id']==noti.utilizadorrecebe:
        if noti.idutilizadorenvia==-1:
            destinatario="Diaaberto@ualg.pt"
        else:
            destinatario=noti.idutilizadorenvia
            destinatario=Utilizador.objects.get(pk=destinatario).email
        tipo="Emissor"
    form = NotificationForm(initial={'Destinatario':destinatario,'Assunto':noti.assunto,'Descricao':noti.descricao})
    print(form)
    UtilizadorHasNotificacao.objects.filter(notificacao=noti).update(estado=1)
    return render(request,"consultar_not.html",{'form':form,'me_id':me_id,'funcao':user_views.user(request),'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'tipo':tipo})

def noti_not_checked(request):
    noti=[]
    if 'user_id' in request.session:
        user_id=request.session['user_id']
        user=Utilizador.objects.get(pk=user_id)
        my_noti=UtilizadorHasNotificacao.objects.all()
        for n in my_noti:
            if n.notificacao.utilizadorrecebe==user.pk and n.estado==0 and n.utilizador_idutilizador==user:
                n.pk=n.pk
                noti.append(n)
    return noti

def get_my_lists(request,list):
    me=Utilizador.objects.get(pk=request.session['user_id'])
    list.append("Administradores")
    if  me.validada==4:
        list.append("Participantes")
        list.append("Coordenadores")
        list.append("Colaboradores")
        list.append("Docentes")
        list.append("Unidades_Organicas")
        uos=UnidadeOrganica.objects.all()
        dus=ProfessorUniversitario.objects.all()
        coords=Coordenador.objects.all()
        colabs=Colaborador.objects.all()
        joins(uos,"Docentes",list)
        joins(uos,"Coordenadores",list)
        joins(uos,"Colaboradores",list)
    if me.validada==2:
        me=Coordenador.objects.get(utilizador_idutilizador=me)
        uos=me.unidade_organica_iduo
        dus=ProfessorUniversitario.objects.all()
        coords=Coordenador.objects.all()
        colabs=Colaborador.objects.all()
        list.append(str('Docentes'+"."+uos.sigla+""))
        list.append(str('Coordenadores'+"."+uos.sigla+""))
        list.append(str('Colaboradores'+"."+uos.sigla+""))
    if me.validada==3:
        me=ProfessorUniversitario.objects.get(utilizador_idutilizador=me)
        uos=me.departamento_iddepartamento.unidade_organica_iduo
        coords=Coordenador.objects.all()
        colabs=Colaborador.objects.all()
        list.append(str('Coordenadores'+"."+uos.sigla+""))
    if me.validada==1:
        me=Colaborador.objects.get(utilizador_idutilizador=me)
        uos=me.curso_idcurso.unidade_organica_iduo
        coords=Coordenador.objects.all()
        dus=ProfessorUniversitario.objects.all()
        list.append(str('Coordenadores'+"."+uos.sigla+""))

    return list

def new_noti(request,destinatario_pk,assunto,texto):
    if not('user_id' in request.session):
        user_id=-1
    else:
        user_id=request.session['user_id']
        if destinatario_pk==request.session['user_id'] or assunto=='Bem-vindo':
            user_id=-1
    noti=Notificacao.objects.create(descricao=texto,utilizadorrecebe=destinatario_pk,idutilizadorenvia=user_id,criadoem=datetime.now(),assunto=assunto)
    UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=destinatario_pk),notificacao=noti,estado=0)
    if Utilizador.objects.filter(pk=user_id).exists():
        UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=user_id),notificacao=noti,estado=0)


def joins(uos,x,list):
    for uo in uos:
        print(str(x+uo.sigla+""))
        if not str(x+uo.sigla+"") in list:
            list.append(str(x+"."+uo.sigla+""))
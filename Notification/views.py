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

list=[]
def createnot(request):
    me_id=request.session['user_id']
    funcao=user_views.user(request)
    contacts=get_my_lists(request)
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        emails=request.POST['Destinatario'].split(",")
        #print(form.is_valid())
        if form.is_valid():
            for email in emails:
                #print("noti:"+str(user_views.validateEmail(email) is True) +" "+str(Utilizador.objects.filter(email=email).exists()))
                form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
                if user_views.validateEmail(email) is True and (Utilizador.objects.filter(email=email).exists() or email in list):
                    if Utilizador.objects.filter(email=email).exists():
                        user_email = Utilizador.objects.get(email=email)
                else:
                    form.add_error('Destinatario','email invalido ou não existe')
                    messages.error(request,"Email Invalido")
                    return render(request, 'compor_not.html', {'form': form,'me_id':signing.dumps(me_id),'funcao':funcao,'contacts':contacts})
                if email in list:
                    send_to_org(email,request)
                else:
                    d=request.POST['Descricao']
                    a=request.POST['Assunto']
                    destinatario_pk= int(user_email.pk)
                    noti=Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
                    UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=user_email,notificacao=noti,estado=0)
            messages.success(request, 'Successfully sent.')
            return redirect('check_not')
    else:
        form = NotificationForm()
    return render(request, 'compor_not.html', {'form': form,'me_id':signing.dumps(me_id),'funcao':funcao,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'contacts':contacts})

def send_to_org(email,request):
    email=email.split("@")[0]
    email=email.split(".")
    if email[0]=="Docentes":
        users_send=ProfessorUniversitario.objects.all()
        if len(email)==2:
            users_send=ProfessorUniversitario.objects.get(departamento_iddepartamento=Departamento.objects.get(unidade_organica_iduo=UnidadeOrganica.objects.get(sigla=email[1])))
    if email[0]=="Coordenadores":
        users_send=Coordenador.objects.all()
        if len(email)==2:
            users_send=Coordenador.objects.get(unidade_organica_iduo=UnidadeOrganica.objects.get(sigla=email[1]))
    if email[0]=="Colaboradores":
        users_send=Colaborador.objects.all()
        if len(email)==2:
            users_send=Colaborador.objects.get(curso_idcurso=Curso.objects.get(unidade_organica_iduo=email[1]))
    if email[0]=="Administradores":
        users_send=Administrador.objects.all()
    if email[0]=="Participantes":
        users_send=Participante.objects.all()
    for user in users_send:
        d=request.POST['Descricao']
        a=request.POST['Assunto']
        destinatario_pk= int(user.pk)
        noti=Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
        UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=user.pk),notificacao=noti,estado=0)
        UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=request.session['user_id']),notificacao=noti,estado=0)

    
def checknot(request):
    me_id=request.session['user_id']
    i=len(noti_not_checked(request))
    notis=[]
    nots=UtilizadorHasNotificacao.objects.all().annotate(emissor=Value("",CharField()))
    deletenot(request)
    for noti in nots:
        if noti.utilizador_idutilizador.pk==me_id:
            noti.emissor=Utilizador.objects.get(pk=noti.notificacao.idutilizadorenvia).email
            noti.pk=signing.dumps(noti.pk)
            notis.append(noti)
    func=user_views.user(request)
    return render(request,'check.html',{'nots':notis,'me_id':me_id,'funcao':func,'i':i,'not_checked':noti_not_checked(request)})

def deletenot(request):

    if request.method == 'POST':
        print(request.POST.getlist('noti'))
        pressed = request.POST.getlist('noti')
        for press in pressed:
            UtilizadorHasNotificacao.objects.filter(pk=signing.loads(press)).delete()
        messages.success(request, 'Successfully deleted.')
            

def enviados(request):
    me_id=request.session['user_id']
    notis=[]
    nots=UtilizadorHasNotificacao.objects.all().annotate(emissor=Value("",CharField()),recept=Value("",CharField()))
    deletenot(request)
    for noti in nots:
        if noti.notificacao.idutilizadorenvia==me_id:
            noti.recept=Utilizador.objects.get(pk=noti.notificacao.utilizadorrecebe).email
            noti.pk=signing.dumps(noti.pk)
            notis.append(noti)
    func=user_views.user(request)
    my=True
    i=len(noti_not_checked(request))
    return render(request,'check.html',{'nots':notis,'me_id':me_id,'funcao':func,'my':my,'i':i,'not_checked':noti_not_checked(request)})

def noti(request,id):
    me_id=signing.loads(id)
    noti=Notificacao.objects.get(pk=me_id)
    form = NotificationForm(initial={'Destinatario':Utilizador.objects.get(pk=noti.utilizadorrecebe).email,'Assunto':noti.assunto,'Descricao':noti.descricao})
    print(form)
    UtilizadorHasNotificacao.objects.filter(notificacao=noti).update(estado=1)
    return render(request,"consultar_not.html",{'form':form,'me_id':signing.dumps(me_id),'funcao':user_views.user(request),'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def noti_not_checked(request):
    noti=[]
    if 'user_id' in request.session:
        user_id=request.session['user_id']
        user=Utilizador.objects.get(pk=user_id)
        my_noti=UtilizadorHasNotificacao.objects.all()
        for n in my_noti:
            if n.notificacao.utilizadorrecebe==user.pk and n.estado==0:
                n.notificacao.pk=signing.dumps(n.notificacao.pk)
                noti.append(n.notificacao)
    return noti

def get_my_lists(request):
    me=Utilizador.objects.get(pk=request.session['user_id'])
    list.append("Administradores@ualg.pt")
    if  me.validada==4:
        list.append("Participantes@ualg.pt")
        list.append("Coordenadores@ualg.pt")
        list.append("Colaboradores@ualg.pt")
        list.append("Docentes@ualg.pt")
        list.append("UOs@ualg.pt")
        uos=UnidadeOrganica.objects.all()
        dus=ProfessorUniversitario.objects.all()
        coords=Coordenador.objects.all()
        colabs=Colaborador.objects.all()
        joins(uos,"Docentes")
        joins(uos,"Coordenadores")
        joins(uos,"Colaboradores")
    if me.validada==2:
        uos=me.unidade_organica_iduo
        dus=ProfessorUniversitario.objects.all()
        coords=Coordenador.objects.all()
        colabs=Colaborador.objects.all()
        joins(uos,"Docentes")
        joins(uos,"Coordenadores")
        joins(uos,"Colaboradores")
    return list

def new_noti(request,destinatario_pk,assunto,texto):
    noti=Notificacao.objects.create(descricao=texto,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=assunto)
    UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=destinatario_pk),notificacao=noti,estado=0)
    UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=Utilizador.objects.get(pk=request.session['user_id']),notificacao=noti,estado=0)


def joins(uos,x):
    for uo in uos:
        print(str(x+uo.sigla+"@ualg.pt"))
        if not str(x+uo.sigla+"@ualg.pt") in list:
            list.append(str(x+"."+uo.sigla+"@ualg.pt"))

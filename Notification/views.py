from django.shortcuts import render, redirect
from Notification import templates
from .models import Notificacao, Utilizador, DjangoSession, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador, UtilizadorHasNotificacao
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import signing
from django.contrib import messages
from user import views as user_views
from django.db.models import CharField, Value,IntegerField
from datetime import datetime
from django.db.models.functions import Cast

def createnot(request):
    me_id=request.session['user_id']
    funcao=user_views.user(request)
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        emails=request.POST['Destinatario'].split(",")
        #print(form.is_valid())
        if form.is_valid():
            for email in emails:
                #print("noti:"+str(user_views.validateEmail(email) is True and not Utilizador.objects.filter(email=email).exists()))
                form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
                if user_views.validateEmail(email) is True and not Utilizador.objects.filter(email=email).exists():
                    user_email = Utilizador.objects.get(email=email)
                else:
                    form.add_error('Destinatario','email invalido ou não existe')
                    messages.error(request,"Email Invalido")
                    return render(request, 'compor_not.html', {'form': form,'me_id':signing.dumps(me_id),'funcao':funcao})
                d=request.POST['Descricao']
                a=request.POST['Assunto']
                destinatario_pk= int(user_email.pk)
                noti=Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
                UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=user_email,notificacao=noti,estado=0)
            messages.success(request, 'Successfully sent.')
            return redirect('check_not')
    else:
        form = NotificationForm()
    return render(request, 'compor_not.html', {'form': form,'me_id':signing.dumps(me_id),'funcao':funcao})

def checknot(request):
    me_id=request.session['user_id']
    i=len(noti_not_checked(request))
    nots=Notificacao.objects.all().annotate(emissor=Value("",CharField()))
    for noti in nots:
        noti.emissor=Utilizador.objects.get(pk=noti.idutilizadorenvia).email
        noti.pk=signing.dumps(noti.pk)
    func=user_views.user(request)
    return render(request,'check.html',{'nots':nots,'me_id':me_id,'funcao':func,'i':i,'not_checked':noti_not_checked(request)})

def deletenot(request):

    pressed = request.POST.getlist('{{forloop.count}}')

    if request.method == 'POST':
        pressed.delete()
        messages.success(request, 'Successfully deleted.')
            
    else:
        return render(request, 'tabela_de_consulta.html', {'pressed': pressed})

def enviados(request):
    me_id=request.session['user_id']
    nots=Notificacao.objects.filter(idutilizadorenvia = me_id).annotate(emissor=Value("",CharField()),recept=Value("",CharField()))
    i=0
    for noti in nots:
        if noti.utilizadorrecebe==me_id and noti.estadol==1:
            i+=1
        noti.recept=Utilizador.objects.get(pk=noti.utilizadorrecebe).email
        noti.pk=signing.dumps(noti.pk)
    func=user_views.user(request)
    my=True
    return render(request,'check.html',{'nots':nots,'me_id':me_id,'funcao':func,'my':my,'i':i})

def noti(request,id):
    me_id=signing.loads(id)
    noti=Notificacao.objects.get(pk=me_id)
    form = NotificationForm(initial={'Destinatario':Utilizador.objects.get(pk=noti.utilizadorrecebe).email,'Assunto':noti.assunto,'Descricao':noti.descricao})
    print(form)
    return render(request,"consultar_not.html",{'form':form,'me_id':signing.dumps(me_id),'funcao':user_views.user(request)})

def noti_not_checked(request):
    user_id=request.session['user_id']
    user=Utilizador.objects.get(pk=user_id)
    my_noti=Notificacao.objects.annotate(estado=Value(1,IntegerField())).get(utilizadorrecebe=user_id)
    
    for noti in my_noti:
        if UtilizadorHasNotificacao.objects.filter(notificacao=noti).exists():
            noti.estado=0
    return my_noti


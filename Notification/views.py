from django.shortcuts import render, redirect
from Notification import templates
from .models import Notificacao, Utilizador, DjangoSession, Participante, ProfessorUniversitario, Administrador, Coordenador, Colaborador
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core import signing
from django.contrib import messages
from user import views as user_views
from django.db.models import CharField, Value
from datetime import datetime
from pytz import timezone

def createnot(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
            user_email = Utilizador.objects.get(email=request.POST['Destinatario'])
            d=request.POST['Descricao']
            a=request.POST['Assunto']
            destinatario_pk= int(user_email.pk)
            Notificacao.objects.create(descricao=d,utilizadorrecebe=destinatario_pk,idutilizadorenvia=request.session['user_id'],criadoem=datetime.now(),assunto=a)
            messages.success(request, 'Successfully sent.')
            return redirect('notification.html')
    else:
        form = NotificationForm()

    return render(request, 'notification.html', {'form': form})

def checknot(request):
    me_id=request.session['user_id']
    nots=Notificacao.objects.all().annotate(emissor=Value("",CharField()))
    for noti in nots:
        noti.emissor=Utilizador.objects.get(pk=noti.idutilizadorenvia).email
        noti.id=signing.dumps(noti.id)
    func=user_views.user(request)
    return render(request,'check.html',{'nots':nots,'me_id':me_id,'funcao':func})

def deletenot(request):

    id_list = request.POST.getlist('forloop.count')
    if request.method == 'POST':
        #id_list = request.POST.getlist('forloop.count')
        for not_id in id_list:
            Notificacao.objects.get(id=not_id).delete()
            return HttpResponse("<h2>Deleted sucessfully</h2>")
    else:
        return render(request, 'tabela_de_consulta.html', {'id_list': id_list})

def enviados(request):
    me_id=request.session['user_id']
    nots=Notificacao.objects.filter(idutilizadorenvia = me_id).annotate(emissor=Value("",CharField()))
    for noti in nots:
        noti.emissor=Utilizador.objects.get(pk=noti.idutilizadorenvia).email
        noti.id=signing.dumps(noti.id)
    func=user_views.user(request)
    return render(request,'check.html',{'nots':nots,'me_id':me_id,'funcao':func})

def noti(request,id):
    return HttpResponse("top")


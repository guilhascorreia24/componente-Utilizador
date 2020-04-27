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


def createnot(request):

    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
            user_email = Utilizador.objects.get(email=request.POST['Destinatario'])
            print(request.POST['Destinatario'])
            print("hello world")
            form.cleaned_data['idutilizadorrecebe'] = int(user_email.pk)
            form.save(request)
            messages.success(request, 'Successfully sent.')
            return redirect('/create/')
    else:
        form = NotificationForm()

    return render(request, 'notification.html', {'form': form})


def checknot(request):

    form = Notificacao.objects.filter(utilizadorrecebe=request.session['user_id'])
    return render(request, 'check.html', {'form': form})


def deletenot(request):

    form = Notificacao.objects.filter(utilizadorrecebe=request.session['user_id'])

    if 'nots' in request.POST:
        if request.POST.get('delete'):
            form = Notificacao.objects.filter().delete()
            return HttpResponse("<h2>Deleted sucessfully</h2>")
    else:
        return render(request, 'delete.html', {'form': form})

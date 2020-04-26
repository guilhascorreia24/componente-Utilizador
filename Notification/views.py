from django.shortcuts import render, redirect
from Notification import templates
from .models import Notificacao, Utilizador, DjangoSession
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core import signing
from django.contrib import messages

def createnot(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idutilizadorenvia'] = request.session['user_id']
            form.save(request)
            return HttpResponse("<h2>Sent sucessfully</h2>")
    else:
        form = UserRegisterForm()

    return render(request, 'notification.html', {'form': form})


def checknot(request):

    form = Notificacao.objects.filter(utilizadorrecebe=request.session['user_id'])
    return render(request, 'check.html', {'form': form})


def deletenot(request):

    form = Notificacao.objects.filter(utilizadorrecebe=request.session['user_id'])

    if 'nots' in request.POST:
        print("hello world")
        form.delete()
        return HttpResponse("<h2>Deleted sucessfully</h2>")
    else:
        return render(request, 'delete.html', {'form': form})

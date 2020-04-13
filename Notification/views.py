from django.shortcuts import render
from Notification import templates
from .models import Notificacao
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def crazyuser(request):

    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    current_user = request.user
    print(current_user.id)

def createnot(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Sent sucessfully</h2>")
    else:
        form = UserRegisterForm()

    return render(request, 'notification.html', {'form': form})


def checknot(request):

    #form = Notificacao.objects.filter(idutilizadorrecebe=request.id())
    form = Notificacao.objects.filter(utilizadorrecebe=2331)
    return render(request,'check.html', {'form': form})


def deletenot(request):

    #form = Notificacao.objects.filter(idutilizadorrecebe=request.id())
    form = Notificacao.objects.filter(utilizadorrecebe=2331)

    if request.method == 'POST':
        if 'checkbox' in request.POST:
            form.delete()
            return HttpResponse("<h2>Deleted sucessfully</h2>")
         
    #else:
    return render(request,'delete.html', {'form': form})

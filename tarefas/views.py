from django.shortcuts import render, redirect, HttpResponse
from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from tarefas import forms
from django.db.models import F
from .models import Disponibilidade, Utilizador,Dia,Horario


# Consultar tarefas
def disponibilidade(request):
    user = request.session['user_id']
    utilizador = Utilizador.objects.get(pk=user)
    dias=Dia.objects.all()
    Horas=Horario.objects.all()
    tipo=['Guiar Participante(s)','Ajudar na Atividade']

    #Colaborador

    if utilizador.validada == 1 :

        disp = modelformset_factory(Disponibilidade,form = forms.Form_Disponibilidade,extra=1)
        if request.method == 'POST':
            form = forms.Form_Disponibilidade(request.POST, prefix="tarefa")

            if form.is_valid():
                form.save(user)
                return HttpResponse("<html>Sucesso</html>")

        else:   
            form = disp(queryset=Disponibilidade.objects.none(), prefix="tarefa")


        return render(request, "Disponibilidade.html", {'form': form})

        
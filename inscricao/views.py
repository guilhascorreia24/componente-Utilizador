from django.shortcuts import render, redirect, HttpResponse
from inscricao import models
from django.contrib.auth import authenticate, login, logout
from blog import userValidation
from inscricao import forms
from django.forms import formset_factory
from django.db.models import F
from django.core import signing

# Main Views.
def test(request):
    #return inscricao.showForm(request)
    form = forms.Form_Escola()
    return render(request,'test2.html',{'form': form})

def test1(request):
    if request.method == 'POST':
        form = forms.CustomForm(request)
        if form.is_valid():
            form.save()
            return HttpResponse("<html>Sucess</html>")
        else:
            return render(request,'test.html',{'form': form})
        
    else:
        form = forms.CustomForm()
        return render(request,'test.html',{'form': form})

def list_sessao():
    #models.Sessao.objects.raw('SELECT titulo,duracao,descricao,unidade_organica_iduo,departamento_iddepartamento,tematica,idsessao,vagas,atividade_idatividade,horario_has_dia_id_dia_hora FROM Sessao, Atividade WHERE Atividade.validada = 1 INNER JOIN Atividade.idatividade=Sessao.atividade_idatividade ORDER BY Atividade.titulo')
    #models.Sessao.objects.filter()
    test = models.Sessao.objects \
    .select_related('atividade_idatividade','atividade_idatividade__departamento_iddepartamento','atividade_idatividade__campus','atividade_idatividade__unidade_organica_iduo__campus_idcampus','atividade_idatividade__unidade_organica_iduo','horario_has_dia_id_dia_hora__horario_hora','atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador','atividade_idatividade__espaco_idespaco')\
    .filter(atividade_idatividade__validada=1)\
    .order_by('atividade_idatividade__titulo','horario_has_dia_id_dia_hora__horario_hora__hora')\
    .values('idsessao','vagas',hora=F('horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('atividade_idatividade__idatividade'),titulo=F('atividade_idatividade__titulo'),duracao=F('atividade_idatividade__duracao'),descricao=F('atividade_idatividade__descricao'),unidade_organica=F('atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('atividade_idatividade__tematica'),docente = F('atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('atividade_idatividade__espaco_idespaco__nome'))
    return test

def inscricao_form(request):
    id=signing.dumps(request.session['user_id'])
    if request.method == 'POST':
        form = forms.CustomForm(request)
        if form.is_valid():
            form.save()
            return HttpResponse("<html>Sucess</html>")
        else:
            sessoes = list_sessao()
            return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes,'id':id})
        
    else:
        #//atividades

        form = forms.CustomForm()
        sessoes = list_sessao()
        return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes,'id':id})
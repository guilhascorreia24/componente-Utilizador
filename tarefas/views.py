from django.shortcuts import render, redirect, HttpResponse
from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from tarefas import forms
from django.db.models import F
from .models import Disponibilidade, Utilizador, Colaborador, Sala, Anfiteatro , Arlivre, Tarefa
from django.views.decorators.csrf import csrf_exempt
from Notification.views import noti_not_checked
from django.contrib import messages



# DISPONIBILIDADE

def consultar_tarefas(request):
    user = request.session['user_id']
    utilizador = Utilizador.objects.get(pk=user)
    colaborador = Colaborador.objects.get(pk=user)

    #Colaborador

    if utilizador.validada == 1 :


        disp = modelformset_factory(Disponibilidade,form = forms.Form_Disponibilidade,extra=0, can_delete=True)
        if request.method == 'POST':
            form = disp(request.POST, prefix="tarefa")

            for disps in form:
                disps.save_user(colaborador)

            print(form.deleted_forms)

            if form.is_valid():
              
                form.save()

                form = disp(queryset=Disponibilidade.objects.filter(colaborador_utilizador_idutilizador = colaborador), prefix="tarefa")
                messages.success(request, f'Disponibilidade alterada!')
                return render(request, "consultar_tarefas.html", {'form': form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
  
        form = disp(queryset=Disponibilidade.objects.filter(colaborador_utilizador_idutilizador = colaborador), prefix="tarefa")
        return render(request, "consultar_tarefas.html", {'form': form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

# Consultar Tarefas

def consultar_tarefas2(request):
    user = request.session['user_id']
    utilizador = Utilizador.objects.get(pk=user)

    #Colaborador

    if utilizador.validada == 1 :
        tarefas = Tarefa.objects \
        .select_related('idtarefa','dia_dia','coordenador_utilizador_idutilizador__utilizador_idutilizador','sessao_idsessao','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora','sessao_idsessao__horario_has_dia_id_dia_hora__dia_dia','sessao_idsessao__atividade_idatividade','buscar','levar', 'levar__campus_idcampus','inscricao_coletiva_inscricao_idinscricao','inscricao_coletiva_inscricao_idinscricao__escola_idescola','colaborador_utilizador_idutilizador').all() \
        .values(id_tarefa=F('idtarefa'),estado=F('concluida'),dia=F('dia_dia__dia'),nome_coordenador=F('coordenador_utilizador_idutilizador__utilizador_idutilizador__nome'),hora=F('hora_inicio'),sessao_hora=F('sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora'),nome_tarefa=F('nome'),atividade=F('sessao_idsessao__atividade_idatividade__titulo'),espaco_antes=F('buscar__nome'),espaco_depois=F('levar__nome'),id_espaco_antes=F('buscar'),id_espaco_depois=F('levar'),
            campus=F('levar__campus_idcampus__nome'),n_alunos=F('sessao_idsessao__nrinscritos'),turma=F('inscricao_coletiva_inscricao_idinscricao__turma'),escola=F('inscricao_coletiva_inscricao_idinscricao__escola_idescola__nome'),atividade_espaco=F('sessao_idsessao__atividade_idatividade__espaco_idespaco__nome'),id_atividade_espaco=F('sessao_idsessao__atividade_idatividade__espaco_idespaco'),
            atividade_campus=F('sessao_idsessao__atividade_idatividade__espaco_idespaco__campus_idcampus__nome'),colab=F('colaborador_utilizador_idutilizador'),sessao_dia=F('sessao_idsessao__horario_has_dia_id_dia_hora__dia_dia'))
        sala=Sala.objects.all()
        anfi=Anfiteatro.objects.all()
        ar=Arlivre.objects.all()
        return render(request, "consultar_tarefas2.html", { 'ar':ar,'sala':sala,'anfi':anfi,'tarefas':tarefas,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request) })

    else:
        return render(request, "not_for-u.html", { 'message' : 'Não é um colaborador','i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request) })

@csrf_exempt
def mudar_estado(request):

    if request.method == 'POST':
        id = request.POST.get("id","") 
        valor = request.POST.get("valor","") 

        Tarefa.objects.filter(pk=id).update(concluida=valor)

    return HttpResponse("")

        
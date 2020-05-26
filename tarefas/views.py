from django.shortcuts import render, redirect, HttpResponse
from django.forms import ModelForm,modelformset_factory,Form,inlineformset_factory,ValidationError
from tarefas import forms
from django.db.models import F
from .models import Disponibilidade, Utilizador
from .models import Tarefa
from django.views.decorators.csrf import csrf_exempt



# DISPONIBILIDADE

def consultar_tarefas(request):
    user = request.session['user_id']
    utilizador = Utilizador.objects.get(pk=user)

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


        return render(request, "consultar_tarefas.html", {'form': form})

# Consultar Tarefas

def consultar_tarefas2(request):
    user = request.session['user_id']
    utilizador = Utilizador.objects.get(pk=user)

    #Colaborador

    if utilizador.validada == 1 :

        tarefas = Tarefa.objects \
        .select_related('idtarefa','dia_dia','coordenador_utilizador_idutilizador__utilizador_idutilizador','sessao_idsessao','sessao_idsessao__atividade_idatividade','buscar','levar', 'levar__campus_idcampus','inscricao_coletiva_inscricao_idinscricao','inscricao_coletiva_inscricao_idinscricao__escola_idescola').all() \
        .values(id_tarefa=F('idtarefa'),estado=F('concluida'),dia=F('dia_dia__dia'),nome_coordenador=F('coordenador_utilizador_idutilizador__utilizador_idutilizador__nome'),hora=F('hora_inicio'),nome_tarefa=F('nome'),atividade=F('sessao_idsessao__atividade_idatividade__titulo'),espaco_antes=F('buscar__nome'),espaco_depois=F('levar__nome'),campus=F('levar__campus_idcampus__nome'),n_alunos=F('sessao_idsessao__nrinscritos'),turma=F('inscricao_coletiva_inscricao_idinscricao__turma'),escola=F('inscricao_coletiva_inscricao_idinscricao__escola_idescola__nome'))

        return render(request, "consultar_tarefas2.html", { 'tarefas':tarefas } )

@csrf_exempt
def mudar_estado(request):

    if request.method == 'POST':
        id = request.POST.get("id","") 
        valor = request.POST.get("valor","") 

        Tarefa.objects.filter(pk=id).update(concluida=valor)

    return HttpResponse("")

        
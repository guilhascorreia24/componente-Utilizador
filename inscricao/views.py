from django.shortcuts import render, redirect, HttpResponse
from inscricao import models
from django.contrib.auth import authenticate, login, logout
from blog import userValidation
from inscricao import forms
from django.forms import formset_factory
from django.db.models import F
from django.core import signing

# Main Views.

def list_sessao():
    test = models.Sessao.objects \
    .select_related('atividade_idatividade','atividade_idatividade__departamento_iddepartamento','atividade_idatividade__campus','atividade_idatividade__unidade_organica_iduo__campus_idcampus','atividade_idatividade__unidade_organica_iduo','horario_has_dia_id_dia_hora__horario_hora','atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador','atividade_idatividade__espaco_idespaco')\
    .filter(atividade_idatividade__validada=1)\
    .order_by('atividade_idatividade__titulo','horario_has_dia_id_dia_hora__horario_hora__hora')\
    .values('idsessao','vagas',hora=F('horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('atividade_idatividade__idatividade'),titulo=F('atividade_idatividade__titulo'),duracao=F('atividade_idatividade__duracao'),descricao=F('atividade_idatividade__descricao'),unidade_organica=F('atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('atividade_idatividade__tematica'),docente = F('atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('atividade_idatividade__espaco_idespaco__nome'))
    return test

def inscricao_form(request):
    user = userValidation.getLoggedUser(request)
    if user._type != userValidation.PARTICIPANTE:
        return HttpResponse("<html>User needs to be a Participante</html>")

    if request.method == 'POST':
        form = forms.CustomForm(request)
        if form.is_valid():
            form.save(user)
            return HttpResponse("<html>Sucess</html>")
        else:
            sessoes = list_sessao()
            return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes,'id':id})
        
    else:
        form = forms.CustomForm()
        sessoes = list_sessao()
        return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes})


def consultar_inscricao(request):
    user = userValidation.getLoggedUser(request)
    if user._type != userValidation.PARTICIPANTE:
        return HttpResponse("<html>User needs to be a Participante</html>")

    query = models.InscricaoColetiva.objects.select_related('inscricao_idinscricao','escola_idescola').filter(participante_utilizador_idutilizador=user.pk)
    coletivas = query.values('turma',escola=F('escola_idescola__nome'),area=F('inscricao_idinscricao__areacientifica'),participantes=F('nparticipantes'))
    
    for inscricao in query:
        coletivas.almocos = models.InscricaoHasPrato.objects.select_related('prato_idprato','prato_idprato__menu_idmenu','prato_idprato__menu_idmenu__campus_idcampus').filter(inscricao_idinscricao=inscricao.inscricao_idinscricao)\
            .values(campus=F('prato_idprato__menu_idmenu__campus_idcampus__nome'),menu=F('prato_idprato__menu_idmenu__menu'),tipo=F('prato_idprato__menu_idmenu__tipo'),descricao=F('prato_idprato__descricao'),nralmocos=F('prato_idprato__nralmocos'))\
            .order_by('prato_idprato__menu_idmenu__campus_idcampus__nome','prato_idprato__menu_idmenu__tipo')
        
        coletivas.transportes = models.TransporteHasInscricao.objects.select_related('paragem','horario_has_dia').filter(inscricao_idinscricao=inscricao.inscricao_idinscricao)\
            .values('partida_paragem','chegada_paragem',passageiros=F('numero_passageiros'),hora=F('partida'))

        coletivas.responsaveis = models.Responsaveis.objects.filter(idinscricao=inscricao.inscricao_idinscricao)\
            .values('nome','telefone','email')

        coletivas.sessoes = models.InscricaoHasSessao.objects \
            .select_related('sessao_idsessao__atividade_idatividade','sessao_idsessao__atividade_idatividade__departamento_iddepartamento','sessao_idsessao__atividade_idatividade__campus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora','sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador','sessao_idsessao__atividade_idatividade__espaco_idespaco')\
            .filter(inscricao_idinscricao=inscricao.inscricao_idinscricao)\
            .order_by('atividade_idatividade__titulo','horario_has_dia_id_dia_hora__horario_hora__hora')\
            .values('nrinscritos',idsessao=F('sessao_idsessao__idsessao'),vagas=F('sessao_idsessao__vagas'),hora=F('sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('sessao_idsessao__atividade_idatividade__idatividade'),titulo=F('sessao_idsessao__atividade_idatividade__titulo'),duracao=F('sessao_idsessao__atividade_idatividade__duracao'),descricao=F('sessao_idsessao__atividade_idatividade__descricao'),unidade_organica=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('sessao_idsessao__atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('sessao_idsessao__atividade_idatividade__tematica'),docente = F('sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('sessao_idsessao__atividade_idatividade__espaco_idespaco__nome'))
        

    return render(request,'consulta_inscricao.html',{'inscricoes':coletivas})
    

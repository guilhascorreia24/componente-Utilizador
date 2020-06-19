from django.shortcuts import render, redirect, HttpResponse
from Notification.views import noti_not_checked,noti_not_checked
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
    .values('idsessao','capacidade',vagas=F('capacidade')-F('nrinscritos'),hora=F('horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('atividade_idatividade__idatividade'),titulo=F('atividade_idatividade__titulo'),duracao=F('atividade_idatividade__duracao'),descricao=F('atividade_idatividade__descricao'),unidade_organica=F('atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('atividade_idatividade__tematica'),docente = F('atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('atividade_idatividade__espaco_idespaco__nome'))
    return test




def inscricao_delete(request,inscricao):
    user = userValidation.getLoggedUser(request)
    if user._type == userValidation.PARTICIPANTE:
        insc = None
        try:
            insc = models.InscricaoColetiva.objects.get(participante_utilizador_idutilizador = user.pk, inscricao_idinscricao=inscricao)
        except:
            try:
                insc = models.InscricaoIndividual.objects.get(participante_utilizador_idutilizador = user.pk, inscricao_idinscricao=inscricao)
            except:
                return HttpResponse("<h1>Inscrição não existe</h1>")
                
        delete_inscricao(insc)

    return consultar_inscricao(request)

def inscricao_alterar(request,inscricao):

    try:
        insc = models.InscricaoColetiva.objects.get(inscricao_idinscricao=inscricao)
    except:
        try:
            insc = models.InscricaoIndividual.objects.get(inscricao_idinscricao=inscricao)
        except:
            return HttpResponse("<h1>Inscrição não existe</h1>")
        
        return inscricao_individual_form(request,inscricao)

    return inscricao_form(request,inscricao)

#Precisa de ser inscricao individual ou coletiva
def delete_inscricao(inscricao):
    models.InscricaoHasPrato.objects.filter(inscricao_idinscricao = inscricao.inscricao_idinscricao).delete()
    #models.Prato.objects.filter(inscricao_idinscricao = inscricao.inscricao_idinscricao).delete()
    models.TransporteHasInscricao.objects.filter(inscricao_idinscricao = inscricao.inscricao_idinscricao).delete()
    models.InscricaoHasSessao.objects.filter(inscricao_idinscricao = inscricao.inscricao_idinscricao).delete()
    models.Responsaveis.objects.filter(idinscricao = inscricao.inscricao_idinscricao).delete()
    models.Inscricao.objects.filter(idinscricao = inscricao.inscricao_idinscricao.pk).delete()
    inscricao.delete()


def inscricao_form(request,inscricao=None):
    user = userValidation.getLoggedUser(request)
    if user._type != userValidation.PARTICIPANTE:
        return HttpResponse("<html>User needs to be a Participante</html>")

    if request.method == 'POST':
        form = forms.CustomForm(request,inscricao=inscricao)
        if form.is_valid():
            form.save(user)
            return redirect('inscricao:consulta')
        else:
            campus = models.Campus.objects.all()
            sessoes = list_sessao()
            return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes, 'campus':campus, 'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
        
    else:
        campus = models.Campus.objects.all()
        form = forms.CustomForm(inscricao=inscricao)
        sessoes = list_sessao()
        return render(request,'inscricao_form.html',{'form': form, 'atividades_sessao' : sessoes,'campus':campus, 'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
    
    
def test(request):
    return render(request,'test.html')


def consultar_inscricao(request):
    user = userValidation.getLoggedUser(request)
    if user._type != userValidation.PARTICIPANTE:
        return HttpResponse("<html>User needs to be a Participante</html>")

    query_coletiva = models.InscricaoColetiva.objects.select_related('inscricao_idinscricao','escola_idescola').filter(participante_utilizador_idutilizador=user.pk)
    coletivas = query_coletiva.values('turma','nparticipantes',local=F('inscricao_idinscricao__local'),idinscricao=F('inscricao_idinscricao__idinscricao'),ano=F('inscricao_idinscricao__ano'),email=F('escola_idescola__email'),telefone=F('escola_idescola__telefone'),escola=F('escola_idescola__nome'),areacientifica=F('inscricao_idinscricao__areacientifica'))
    query_individual = models.InscricaoIndividual.objects.select_related('inscricao_idinscricao').filter(participante_utilizador_idutilizador=user.pk)
    individuais = query_individual.values('nracompanhantes','telefone',local=F('inscricao_idinscricao__local'),idinscricao=F('inscricao_idinscricao__idinscricao'),ano=F('inscricao_idinscricao__ano'),areacientifica=F('inscricao_idinscricao__areacientifica'))
    result_coletivo = []
    result_individual = []
    
    i=0
    for inscricao in coletivas:
        row = dict()
        row['is_coletiva'] = 1
        row['inscricao'] = coletivas[i]

        row['almoco'] = models.InscricaoHasPrato.objects.select_related('prato_idprato','prato_idprato__menu_idmenu','prato_idprato__menu_idmenu__campus_idcampus').filter(inscricao_idinscricao=query_coletiva[i].inscricao_idinscricao)\
            .values(campus=F('prato_idprato__menu_idmenu__campus_idcampus__nome'),menu=F('prato_idprato__menu_idmenu__menu'),tipo=F('prato_idprato__menu_idmenu__tipo'),descricao=F('prato_idprato__descricao'),nralmocos=F('prato_idprato__nralmocos'))\
            .order_by('prato_idprato__menu_idmenu__campus_idcampus__nome','prato_idprato__menu_idmenu__tipo')
        
        row['transportes'] = models.TransporteHasInscricao.objects.select_related('paragem','horario').filter(inscricao_idinscricao=query_coletiva[i].inscricao_idinscricao)\
            .values(partida_paragem=F('horario__origem'),chegada_paragem=F('horario__destino'),passageiros=F('n_passageiros'),hora=F('horario__horario_has_dia_id_dia_hora'))

        row['responsaveis'] = models.Responsaveis.objects.filter(idinscricao=query_coletiva[i].inscricao_idinscricao)\
            .values('nome','telefone','email')

        row['atividade'] = models.InscricaoHasSessao.objects \
            .select_related('sessao_idsessao__atividade_idatividade','sessao_idsessao__atividade_idatividade__departamento_iddepartamento','sessao_idsessao__atividade_idatividade__campus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora','sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador','sessao_idsessao__atividade_idatividade__espaco_idespaco')\
            .filter(inscricao_idinscricao=query_coletiva[i].inscricao_idinscricao)\
            .order_by('sessao_idsessao__atividade_idatividade__titulo','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora__hora')\
            .values('nr_inscritos',idsessao=F('sessao_idsessao__idsessao'),vagas=F('sessao_idsessao__capacidade'),hora=F('sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('sessao_idsessao__atividade_idatividade__idatividade'),titulo=F('sessao_idsessao__atividade_idatividade__titulo'),duracao=F('sessao_idsessao__atividade_idatividade__duracao'),descricao=F('sessao_idsessao__atividade_idatividade__descricao'),unidade_organica=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('sessao_idsessao__atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('sessao_idsessao__atividade_idatividade__tematica'),docente = F('sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('sessao_idsessao__atividade_idatividade__espaco_idespaco__nome'))
        i+=1
        result_coletivo.append(row)
    
    j = 0
    for inscricao in individuais:
        row = dict()
        row['is_coletiva'] = 0
        row['inscricao'] = individuais[j]

        row['almoco'] = models.InscricaoHasPrato.objects.select_related('prato_idprato','prato_idprato__menu_idmenu','prato_idprato__menu_idmenu__campus_idcampus').filter(inscricao_idinscricao=query_individual[j].inscricao_idinscricao)\
            .values(campus=F('prato_idprato__menu_idmenu__campus_idcampus__nome'),menu=F('prato_idprato__menu_idmenu__menu'),tipo=F('prato_idprato__menu_idmenu__tipo'),descricao=F('prato_idprato__descricao'),nralmocos=F('prato_idprato__nralmocos'))\
            .order_by('prato_idprato__menu_idmenu__campus_idcampus__nome','prato_idprato__menu_idmenu__tipo')
        
        row['transportes'] = models.TransporteHasInscricao.objects.select_related('paragem','horario').filter(inscricao_idinscricao=query_individual[j].inscricao_idinscricao)\
            .values(partida_paragem=F('horario__origem'),chegada_paragem=F('horario__destino'),passageiros=F('n_passageiros'),hora=F('horario__horario_has_dia_id_dia_hora'))

        #row['responsaveis'] = models.Responsaveis.objects.filter(idinscricao=query[i].inscricao_idinscricao)\
            #.values('nome','telefone','email')

        row['atividade'] = models.InscricaoHasSessao.objects \
            .select_related('sessao_idsessao__atividade_idatividade','sessao_idsessao__atividade_idatividade__departamento_iddepartamento','sessao_idsessao__atividade_idatividade__campus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus','sessao_idsessao__atividade_idatividade__unidade_organica_iduo','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora','sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador','sessao_idsessao__atividade_idatividade__espaco_idespaco')\
            .filter(inscricao_idinscricao=query_individual[j].inscricao_idinscricao)\
            .order_by('sessao_idsessao__atividade_idatividade__titulo','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora__hora')\
            .values('nr_inscritos',idsessao=F('sessao_idsessao__idsessao'),vagas=F('sessao_idsessao__capacidade'),hora=F('sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora__hora'),idatividade=F('sessao_idsessao__atividade_idatividade__idatividade'),titulo=F('sessao_idsessao__atividade_idatividade__titulo'),duracao=F('sessao_idsessao__atividade_idatividade__duracao'),descricao=F('sessao_idsessao__atividade_idatividade__descricao'),unidade_organica=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__sigla'),campus=F('sessao_idsessao__atividade_idatividade__unidade_organica_iduo__campus_idcampus__nome'),departamento=F('sessao_idsessao__atividade_idatividade__departamento_iddepartamento__nome'),tematica=F('sessao_idsessao__atividade_idatividade__tematica'),docente = F('sessao_idsessao__atividade_idatividade__professor_universitario_utilizador_idutilizador__utilizador_idutilizador__nome'),espaco = F('sessao_idsessao__atividade_idatividade__espaco_idespaco__nome'))
        j+=1
        result_individual.append(row)


    return render(request,'consultar_participante.html',{'inscricoes_coletivas':result_coletivo,'inscricoes_individuais':result_individual,  'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
    


def inscricao_individual_form(request,inscricao=None):
    user = userValidation.getLoggedUser(request)
    if user._type != userValidation.PARTICIPANTE:
        return HttpResponse("<html>User needs to be a Participante</html>")

    if request.method == 'POST':
        form = forms.FormIndividual(request,inscricao=inscricao)
        if form.is_valid():
            form.save(user)
            return redirect('inscricao:consulta')
        else:
            campus = models.Campus.objects.all()
            sessoes = list_sessao()
            return render(request,'inscricao_individual_form.html',{'form': form, 'atividades_sessao' : sessoes, 'campus':campus,  'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
        
    else:
        campus = models.Campus.objects.all()
        form = forms.FormIndividual(inscricao=inscricao)
        sessoes = list_sessao()
        return render(request,'inscricao_individual_form.html',{'form': form, 'atividades_sessao' : sessoes,'campus':campus,  'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})
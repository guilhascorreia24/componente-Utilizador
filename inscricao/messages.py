
from Notification.views import noti_not_checked,noti_not_checked, new_noti
from django.contrib import messages as message_info

from django.core.mail import  send_mail

NEW_INSCRICAO_TITLE = "Nova Inscrição"
CHANGE_INSCRICAO_TITLE = "Inscrição alterada"
DELETE_INSCRICAO_TITLE = "Inscrição apagada"

DELETE_INSCRICAO_CONTENT = "Inscrição de __NUM__ pessoa(s) apagada na atividade __ATV__ na sessão das __HORAS__.\nExistem agora __LUGARES__ lugares disponiveis."
NEW_INSCRICAO_CONTENT = "Nova inscrição de __NUM__ pessoa(s) registada na atividade __ATV__ na sessão das __HORAS__.\nExistem ainda __LUGARES__ lugares disponiveis."
CHANGE_INSCRICAO_CONTENT = "Inscrição alterada na atividade __ATV__ na sessão das __HORAS__.\nExistem ainda __LUGARES__ lugares disponiveis."

def send_notification(request,form):
    #New
    #return None
    #print(form.sessao.extra_forms())
    for sessao_form in form.sessao.extra_forms:
        sessao = sessao_form.cleaned_data['sessao_idsessao']
        message = NEW_INSCRICAO_CONTENT.replace("__ATV__",sessao.atividade_idatividade.titulo)
        message = message.replace("__NUM__",str(sessao_form.cleaned_data['nr_inscritos']))
        message = message.replace("__HORAS__",sessao.horario_has_dia_id_dia_hora.horario_hora.__str__())
        message = message.replace("__LUGARES__",str(sessao.capacidade - sessao.nrinscritos))
        new_noti(request,sessao.atividade_idatividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.pk,NEW_INSCRICAO_TITLE.replace('__ATV__',sessao.atividade_idatividade.titulo),message)

    #Deleted
    for sessao_form in form.sessao.deleted_forms:
        sessao = sessao_form.cleaned_data['sessao_idsessao']
        message = DELETE_INSCRICAO_CONTENT.replace("__ATV__",sessao.atividade_idatividade.titulo)
        message = message.replace("__NUM__",str(sessao_form.cleaned_data['nr_inscritos']))
        message = message.replace("__HORAS__",sessao.horario_has_dia_id_dia_hora.horario_hora.__str__())
        message = message.replace("__LUGARES__",str(sessao.capacidade - sessao.nrinscritos))
        new_noti(request,sessao.atividade_idatividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.pk,DELETE_INSCRICAO_TITLE.replace('__ATV__',sessao.atividade_idatividade.titulo),message)

    #Changed
    for sessao_form in form.sessao.initial_forms:
        if sessao_form in form.sessao.deleted_forms:
            return
        sessao = sessao_form.cleaned_data['sessao_idsessao']
        message = CHANGE_INSCRICAO_CONTENT.replace("__ATV__",sessao.atividade_idatividade.titulo)
        message = message.replace("__HORAS__",sessao.horario_has_dia_id_dia_hora.horario_hora.__str__())
        message = message.replace("__LUGARES__",str(sessao.capacidade - sessao.nrinscritos))
        new_noti(request,sessao.atividade_idatividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.pk,CHANGE_INSCRICAO_TITLE.replace('__ATV__',sessao.atividade_idatividade.titulo),message)


from Notification.views import noti_not_checked,noti_not_checked, new_noti

NEW_INSCRICAO_TITLE = "Nova Inscrição na atividade __ATV__"
NEW_INSCRICAO_CONTENT = "Nova inscrição de __NUM__ pessoa(s) registada na atividade __ATV__ na sessão das __HORAS__.\nExistem ainda __LUGARES__ lugares disponiveis."


def send_new_inscricao_individual(request,form):
    for sessao_form in form.sessao:
        sessao = sessao_form.cleaned_data['sessao_idsessao']
        message = NEW_INSCRICAO_CONTENT.replace("__ATV__",sessao.atividade_idatividade.titulo)
        message = message.replace("__NUM__",str(sessao_form.cleaned_data['nr_inscritos']))
        message = message.replace("__HORAS__",sessao.horario_has_dia_id_dia_hora.horario_hora.__str__())
        message = message.replace("__LUGARES__",str(sessao.capacidade - sessao.nrinscritos))
    return new_noti(request,sessao.atividade_idatividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.pk,NEW_INSCRICAO_TITLE.replace('__ATV__',sessao.atividade_idatividade.titulo),message)


def send_new_inscricao_coletiva(request,form):
    for sessao_form in form.sessao:
        sessao = sessao_form.cleaned_data['sessao_idsessao']
        message = NEW_INSCRICAO_CONTENT.replace("__ATV__",sessao.atividade_idatividade.titulo)
        message = message.replace("__NUM__",str(sessao_form.cleaned_data['nr_inscritos']))
        message = message.replace("__HORAS__",sessao.horario_has_dia_id_dia_hora.horario_hora.__str__())
        message = message.replace("__LUGARES__",str(sessao.capacidade - sessao.nrinscritos))
    return new_noti(request,sessao.atividade_idatividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.pk,NEW_INSCRICAO_TITLE.replace('__ATV__',sessao.atividade_idatividade.titulo),message)


def send_change_inscricao_individual(request,form):
    return None



def send_change_inscricao_coletiva(request,form):
    return None



def send_delete_inscricao_individual(request,form):
    return None

def send_delete_inscricao_coletiva(request,form):
    return None
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, get_list_or_404
from les import settings
from .forms import *
from blog.models import Atividade, Utilizador, Administrador, Coordenador, ProfessorUniversitario, Espaco, Departamento, \
    UnidadeOrganica, Sessao, Horario, Campus, Dia, HorarioHasDia, Sala, Anfiteatro, Arlivre, Menu, CoordenadorHasDepartamento
from Notification.views import noti_not_checked
from Notification.views import vagas
from Notification import views as noti_views


# Create your views here.

def home_view(request):
    if 'id' not in request.session:
        logged = False
        context = {
            "log": logged,
        }
    else:
        logged = True
        context = {
            "log": logged,
            "id": request.session["user_id"],
            "account": return_account_type(request.session["user_id"]),
            'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
        }
    return render(request, "atividades/inicio.html", context)


# --------------------------------Atividades:
def all_valid(request):
    errors = ["","","","","","",""]
    if not request.POST.get('titulo'):
        errors[0]="Campo vazio"
    if not request.POST.get('descricao'):
        errors[1]="Campo vazio"
    if not request.POST.get('publico_alvo'):
        errors[2]="Campo vazio"
    if not request.POST.get('tema'):
        errors[3]="Campo vazio"
    if not request.POST.get('duracao'):
        errors[4]="Campo vazio"
    if not request.POST.get('nrcolaboradores'):
        errors[5]="Campo vazio"
    if not request.POST.get('capacidade'):
        errors[6]="Campo vazio"

    return errors

def number_of(erros):
    result = 0
    for x in erros:
        if x:
            result+=1
    return result


def atividade_create_view(request):
    erros = []
    professor = get_object_or_404(ProfessorUniversitario, utilizador_idutilizador=request.session["user_id"])
    if request.method == "POST":
        erros = all_valid(request)
        if number_of(erros) == 0:
            new = Atividade(titulo=request.POST.get('titulo'), capacidade=request.POST.get('capacidade'),
                            publico_alvo=request.POST.get('publico_alvo'),
                            duracao=request.POST.get('duracao'),
                            descricao=request.POST.get('descricao'),
                            validada=0,
                            professor_universitario_utilizador_idutilizador=professor,
                            unidade_organica_iduo=get_object_or_404(UnidadeOrganica, iduo=request.POST.get('unidade_organica')),
                            departamento_iddepartamento=get_object_or_404(Departamento, iddepartamento=request.POST.get('iddepartamento')),
                            espaco_idespaco=None, nrcolaborador=request.POST.get('nrcolaboradores'), tematica=request.POST.get('tema'))
            new.save()
            idActivity = Atividade.objects.latest('idatividade').idatividade
            return redirect("../atividades/editar_local/"+str(idActivity))
    context = {
        "erros":erros,
        "id": request.session["user_id"],
        "espaco": Espaco.objects.all(),
        "professor": professor,
        "campus": Campus.objects.all(),
        "departamentos": Departamento.objects.all(),
        "unidade_organica": UnidadeOrganica.objects.all(),
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_atividade.html", context)


def editar_atividade_view(request, idActivity):
    erros = []
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    espaco = Espaco.objects.all()
    unidade_organica = UnidadeOrganica.objects.all()
    departamento = Departamento.objects.all()
    professor = get_object_or_404(ProfessorUniversitario, utilizador_idutilizador=request.session["user_id"])
    campus = Campus.objects.all()
    sessao = []
    if list(Sessao.objects.filter(atividade_idatividade=idActivity)):
        for sess in get_list_or_404(Sessao, atividade_idatividade=idActivity):
            sessao.append(sess.horario_has_dia_id_dia_hora)
    if request.method == "POST":
        notification =""
        erros = all_valid(request)
        if number_of(erros) == 0:
            if atividade.titulo != request.POST.get('titulo'):
                notification += "Novo titulo: " + request.POST.get('titulo') +"\n"
            atividade.titulo = request.POST.get('titulo')
            if atividade.capacidade != request.POST.get('capacidade'):
                notification += "Novo numero de vagas: " + request.POST.get('capacidade') +"\n"
            atividade.capacidade = request.POST.get('capacidade')
            if atividade.duracao != request.POST.get('duracao'):
                notification += "Nova duração: " + request.POST.get('duracao') +"\n"
            atividade.duracao = request.POST.get('duracao')
            atividade.validada = 2
            atividade.iddepartamento = request.POST.get('iddepartamento')
            atividade.publico_alvo = request.POST.get('publico_alvo')
            if atividade.descricao != request.POST.get('descricao'):
                notification += "Nova descrição: " + request.POST.get('descricao') +"\n"
            atividade.descricao = request.POST.get('descricao')
            if atividade.tematica != request.POST.get('tema'):
                notification += "Novo tema: " + request.POST.get('tema') +"\n"
            atividade.tematica = request.POST.get('tema')
            atividade.nrcolaborador = request.POST.get('nrcolaboradores')
            atividade.save()
            # Notificação de alterar atividade->coord,colab,part
            vagas(request, atividade.idatividade, "Mudança na atividade " + atividade.titulo, notification)
            return redirect("../../editar_local/"+str(idActivity))
    context = {
        "erros": erros,
        "id": request.session["user_id"],
        "activity": atividade,
        "espaco": espaco,
        "professor": professor,
        "campus": campus,
        "departamentos": departamento,
        "unidade_organica": unidade_organica,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_atividade.html", context)


def all_activities_view(request):
    atividades = Atividade.objects.all().filter(validada=1)
    context = {
        "campus": Campus.objects.all(),
        "uo": UnidadeOrganica.objects.all(),
        "departamentos": Departamento.objects.all(),
        "list": atividades,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/consultar_todas_atividades.html", context)


def coordinator_activities_view(request):
    unidade_organica = get_object_or_404(Coordenador,
                                         utilizador_idutilizador=request.session["user_id"]).unidade_organica_iduo.iduo
    atividades = Atividade.objects.all().filter(unidade_organica_iduo=unidade_organica)
    context = {
        "departamentos": Departamento.objects.filter(unidade_organica_iduo=unidade_organica),
        "list": atividades,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/consultar_atividades_coordenador.html", context)


def validar_atividade_view(request,idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    atividade.validada = 1
    atividade.save()
    return redirect("atividades:consultar_atividades_coodernador")


def deletar_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    atividade.delete()
    return redirect("atividades:consultar_minhas_atividades")


# --------------------------------Sessão:

def delete_session(request, idSession):
    sessao = get_object_or_404(Sessao, idsessao=idSession)
    sessao.delete()
    return redirect("../../editar_sessao/"+str(sessao.atividade_idatividade.idatividade))


def my_activities_view(request):
    querysetAtividade = Atividade.objects.all().filter(
        professor_universitario_utilizador_idutilizador=request.session["user_id"])
    context = {
        "list": querysetAtividade,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/consultar_atividades_professor.html", context)


def activity_session_view(request, idActivity):
    querysetSession = Sessao.objects.all().filter(atividade_idatividade=idActivity)
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    if request.method == "POST":
        id_prof = atividade.professor_universitario_utilizador_idutilizador.utilizador_idutilizador.idutilizador
        noti_views.new_noti(request, id_prof, "Motivo de rejeição", request.POST.get("motivo"))
        atividade.validada = -1
        atividade.save()
        return redirect("atividades:consultar_atividades_coodernador")
    context = {
        "list": querysetSession,
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/sessao_info.html", context)


def create_edit_session_view(request, idActivity):
    dia = Dia.objects.all()
    hora = Horario.objects.all()
    message = ""
    if request.method == "POST" and request.POST.get("dia") and request.POST.get("hora"):
        horario = get_object_or_404(HorarioHasDia, dia_dia=request.POST.get("dia"), horario_hora=request.POST.get("hora"))
        if not Sessao.objects.all().filter(atividade_idatividade=idActivity, horario_has_dia_id_dia_hora=horario):
            atividade = get_object_or_404(Atividade, idatividade=idActivity)
            newSession = Sessao(nrinscritos=0, capacidade=atividade.capacidade,
                                atividade_idatividade=get_object_or_404(Atividade, idatividade=idActivity),
                                horario_has_dia_id_dia_hora=horario)
            newSession.save()
            atividade.validada = 2
            atividade.save()
        else:
            message = "Já existe sessão no horário escolhido"
    sessao = Sessao.objects.all().filter(atividade_idatividade=idActivity).order_by('horario_has_dia_id_dia_hora')
    context = {
        "list": sessao,
        "horario": hora,
        "dia": dia,
        "activity": get_object_or_404(Atividade, idatividade=idActivity),
        "messageError": message,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_editar_sessao.html", context)


def create_edit_session_formulario_view(request, idActivity):
    dia = Dia.objects.all()
    hora = Horario.objects.all()
    message = ""
    if request.method == "POST" and request.POST.get("dia") and request.POST.get("hora"):
        horario = get_object_or_404(HorarioHasDia, dia_dia=request.POST.get("dia"), horario_hora=request.POST.get("hora"))
        if not Sessao.objects.all().filter(atividade_idatividade=idActivity, horario_has_dia_id_dia_hora=horario):
            atividade = get_object_or_404(Atividade, idatividade=idActivity)
            newSession = Sessao(nrinscritos=0, capacidade=atividade.capacidade,
                                atividade_idatividade=get_object_or_404(Atividade, idatividade=idActivity),
                                horario_has_dia_id_dia_hora=horario)
            newSession.save()
            atividade.validada = 2
            atividade.save()
        else:
            message = "Já existe sessão no horário escolhido"
    sessao = Sessao.objects.all().filter(atividade_idatividade=idActivity).order_by('horario_has_dia_id_dia_hora')
    context = {
        "list": sessao,
        "horario": hora,
        "dia": dia,
        "activity": get_object_or_404(Atividade, idatividade=idActivity),
        "messageError": message,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_editar_sessao_formulario.html", context)

# --------------------------------Espaço:

def criar_sala_view(request):
    fields = 0
    lista = []
    for i in Arlivre.objects.all():
        lista.append(i.espaco_idespaco)
    for i in Anfiteatro.objects.all():
        lista.append(i.espaco_idespaco)
    for i in Sala.objects.all():
        lista.append(i.espaco_idespaco)
    campus = Campus.objects.all()
    espaco = Espaco.objects.all()
    form = SalaForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            idEspaco = Espaco.objects.latest('idespaco')
            if request.POST.get("descrition"):
                new = Arlivre(descricao=request.POST.get('descrition'), espaco_idespaco=idEspaco)
                new.save()

            elif request.POST.get("andarAnfiteatro"):
                new = Anfiteatro(edificio=request.POST.get('edificioAnfiteatro'), andar=request.POST.get('andarAnfiteatro'),
                                 espaco_idespaco=idEspaco)
                new.save()
            elif request.POST.get("andarSala"):
                new = Sala(edificio=request.POST.get('edificioSala'), andar=request.POST.get('andarSala'),
                                 espaco_idespaco=idEspaco)
                new.save()
        elif request.POST.get('tipoSala'):
            fields = request.POST.get('tipoSala')
    context = {
        "fields":fields,
        "list": lista,
        "espaco": espaco,
        "form": form,
        "campus": campus,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_sala.html", context)


def deletar_espaco_view(request, idEspaco):
    local = get_object_or_404(Espaco, idespaco=idEspaco)
    local.delete()
    return redirect("atividades:criar_sala")


def editar_local_view(request, idActivity):
    account = return_account_type(request.session["user_id"])
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    espaco = []
    allbuildings = []
    selectedBuilding = None
    fields = 0
    if request.method == "POST":
        if request.POST.get('espaco'):
            if atividade.espaco_idespaco != request.POST.get('espaco'):
                notification = "Novo local: "+get_object_or_404(Espaco, idespaco=request.POST.get('espaco')).nome
                # Notificação de vagas-> part
                vagas(request, atividade.idatividade, "Mudança na local da atividade " + atividade.titulo, notification)
            atividade.espaco_idespaco = get_object_or_404(Espaco, idespaco=request.POST.get('espaco'))
            atividade.save()
            if account == 'coordinator':
                return redirect("atividades:consultar_atividades_coodernador")
            elif account == 'professor':
                return redirect("../../editar_sesao/" + str(idActivity))
        elif request.POST.get('semSala'):
            atividade.espaco_idespaco = None
            atividade.save()
            uo = get_object_or_404(ProfessorUniversitario, utilizador_idutilizador=request.session["user_id"]).departamento_iddepartamento.unidade_organica_iduo
            for x in get_list_or_404(Coordenador, unidade_organica_iduo=uo):
                noti_views.new_noti(request, x.utilizador_idutilizador.idutilizador, "Especificações de sala e material", request.POST.get("infoSala"))
            return redirect("../../editar_sesao/" + str(idActivity))
        elif request.POST.get('tipoSala') == '1':
            fields = 1
            for edificio in get_list_or_404(Espaco, campus_idcampus=atividade.unidade_organica_iduo.campus_idcampus):
                if edificio.idespaco in Sala.objects.all().values_list('espaco_idespaco', flat=True) and get_object_or_404(Sala, espaco_idespaco=edificio.idespaco).edificio not in allbuildings:
                    allbuildings.append(get_object_or_404(Sala, espaco_idespaco=edificio.idespaco).edificio)
            if request.POST.get('edificio'):
                selectedBuilding = request.POST.get('edificio')
                for edificio in get_list_or_404(Sala, edificio=selectedBuilding):
                    espaco.append(get_object_or_404(Espaco, idespaco=edificio.espaco_idespaco.idespaco))
        elif request.POST.get('tipoSala') == '2':
            fields = 2
            for edificio in get_list_or_404(Espaco, campus_idcampus=atividade.unidade_organica_iduo.campus_idcampus):
                if edificio.idespaco in Anfiteatro.objects.all().values_list('espaco_idespaco', flat=True) and get_object_or_404(Anfiteatro, espaco_idespaco=edificio.idespaco).edificio not in allbuildings:
                    allbuildings.append(get_object_or_404(Anfiteatro, espaco_idespaco=edificio.idespaco).edificio)
            if request.POST.get('edificio'):
                selectedBuilding = request.POST.get('edificio')
                for edificio in get_list_or_404(Anfiteatro, edificio=selectedBuilding):
                    espaco.append(get_object_or_404(Espaco, idespaco=edificio.espaco_idespaco.idespaco))
        elif request.POST.get('tipoSala') == '3':
            fields = 3
            selectedBuilding = None
            if Arlivre.objects.exists():
                for local in get_list_or_404(Arlivre):
                    espaco.append(get_object_or_404(Espaco, idespaco=local.espaco_idespaco.idespaco))
        elif atividade.espaco_idespaco:
            if account == 'coordinator':
                return redirect("atividades:consultar_atividades_coodernador")
            elif account == 'professor':
                return redirect("../../editar_sesao/" + str(idActivity))
    context = {
        "activity": atividade,
        "espacos": espaco,
        "account": account,
        "fields": fields,
        "edificios": allbuildings,
        "selectedBuilding": selectedBuilding,
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/editar_local.html", context)


# --------------------------------Outros:

def return_account_type(userId):
    if ProfessorUniversitario.objects.filter(utilizador_idutilizador=userId).exists():
        account = "professor"
    elif Coordenador.objects.filter(utilizador_idutilizador=userId).exists():
        account = "coordinator"
    elif Administrador.objects.filter(utilizador_idutilizador=userId).exists():
        account = "adm"
    else:
        account = "other"
    return account


# --------------------------------Campus:

def criar_campus_view(request):
    campus = Campus.objects.all()
    if request.method == 'POST' and not(Campus.objects.filter(nome=request.POST['nome']).exists()):
        new = Campus(nome=request.POST.get('nome'))
        new.save()
    context = {
        "campus": campus,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_campus.html", context)


def apagar_campus_view(request, idCampus):
    campus = get_object_or_404(Campus, idcampus=idCampus)
    print(str(UnidadeOrganica.objects.filter(campus_idcampus=idCampus).exists() and Menu.objects.filter(campus_idcampus=idCampus).exists() and Espaco.objects.filter(campus_idcampus=idCampus).exists()))
    if not(UnidadeOrganica.objects.filter(campus_idcampus=idCampus).exists() and Menu.objects.filter(campus_idcampus=idCampus).exists() and Espaco.objects.filter(campus_idcampus=idCampus).exists()):
        campus.delete()
    return redirect("atividades:criar_campus")


# --------------------------------Unidade Orgãnica:

def criar_uo_view(request):
    uo = UnidadeOrganica.objects.all()
    form = UoForm(request.POST)
    if request.method == 'POST' and not(UnidadeOrganica.objects.filter(sigla=request.POST['sigla'],campus_idcampus=Campus.objects.get(pk=request.POST['campus_idcampus']))):
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        "uo": uo,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_uo.html", context)


def apagar_uo_view(request, idUo):
    uo = get_object_or_404(UnidadeOrganica, iduo=idUo)
    if not(Atividade.objects.filter(unidade_organica_iduo=idUo).exists() and ColaboradorHasUnidadeOrganica.objects.filter(unidade_organica_iduo=idUo).exists() and Coordenador.objects.filter(unidade_organica_iduo=idUo).exists() and Curso.objects.filter(unidade_organica_iduo=idUo).exists() and Departamento.objects.filter(unidade_organica_iduo=idUo).exists()):
        uo.delete()
    return redirect("atividades:criar_uo")


# --------------------------------Departamento:

def criar_departamento_view(request):
    departamento = Departamento.objects.all()
    form = DepartamentoForm(request.POST)
    if request.method == 'POST' and not(Departamento.objects.filter(nome=request.POST['nome'],unidade_organica_iduo=UnidadeOrganica.objects.get(pk=request.POST['unidade_organica_iduo']))):
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        "departamento": departamento,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_departamento.html", context)


def apagar_departamento_view(request, idDepartamento):
    departamento = get_object_or_404(Departamento, iddepartamento=idDepartamento)
    if not(CoordenadorHasDepartamento.objects.filter(departamento_iddepartamento=idDepartamento).exists() and Atividade.objects.filter(departamento_iddepartamento=idDepartamento).exists() and ProfessorUniversitario.objects.filter(departamento_iddepartamento=idDepartamento).exists()) :
        departamento.delete()
    return redirect("atividades:criar_departamento")

# --------------------------------Paragens:

def criar_paragem_view(request):
    paragem = Paragem.objects.all()
    if request.method == 'POST' and not(Paragem.objects.filter(paragem=request.POST['paragem']).exists()):
        new = Paragem(paragem=request.POST.get('paragem'))
        new.save()
    context = {
        "paragem": paragem,
        "account": return_account_type(request.session["user_id"]),
        'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)
    }
    return render(request, "atividades/criar_paragem.html", context)


def apagar_paragem_view(request, paragem):
    paragem = get_object_or_404(Paragem, paragem=paragem)
    if not(Paragem.objects.filter(paragem=paragem).exists() and TransporteHasHorario.objects.filter(origem=Paragem.objects.get(pk=paragem)).exists() and TransporteHasHorario.objects.filter(destino=Paragem.objects.get(pk=paragem)).exists()):
        paragem.delete()
    return redirect("atividades:criar_paragem")




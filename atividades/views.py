from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, get_list_or_404
from tryDjango import settings
from .forms import *
from blog.models import Atividade, Utilizador, Administrador, Coordenador, ProfessorUniversitario, Espaco, Departamento, \
    UnidadeOrganica, Sessao, Horario, Campus, Dia, HorarioHasDia, Sala, Anfiteatro, Arlivre


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
        }
    return render(request, "atividades/inicio.html", context)


# --------------------------------Atividades:

def atividade_create_view(request):
    professor = get_object_or_404(ProfessorUniversitario, utilizador_idutilizador=request.session["user_id"])
    if request.method == "POST":
        new = Atividade(titulo=request.POST.get('titulo'), capacidade=request.POST.get('capacidade'),
                        publico_alvo=request.POST.get('publico_alvo'),
                        duracao=request.POST.get('duracao'),
                        descricao=request.POST.get('descricao'),
                        validada=0,
                        professor_universitario_utilizador_idutilizador=professor,
                        unidade_organica_iduo=get_object_or_404(UnidadeOrganica, iduo=request.POST.get('unidade_organica')),
                        departamento_iddepartamento=get_object_or_404(Departamento, iddepartamento=request.POST.get('iddepartamento')),
                        espaco_idespaco=None, ncolboradores=request.POST.get('ncolaboradores'), tematica=request.POST.get('tema'))
        new.save()
        idActivity = Atividade.objects.latest('idatividade').idatividade
        return redirect("../atividades/editar_local/"+str(idActivity))
    context = {
        "id": request.session["user_id"],
        "espaco": Espaco.objects.all(),
        "professor": professor,
        "campus": Campus.objects.all(),
        "departamentos": Departamento.objects.all(),
        "unidade_organica": UnidadeOrganica.objects.all(),
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_atividade.html", context)


def editar_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    espaco = Espaco.objects.all()
    unidade_organica = UnidadeOrganica.objects.all()
    departamento = Departamento.objects.all()
    professor = get_object_or_404(ProfessorUniversitario, utilizador_idutilizador=request.session["user_id"])
    campus = Campus.objects.all()
    sessao = []
    for sess in get_list_or_404(Sessao, atividade_idatividade=idActivity):
        sessao.append(sess.horario_has_dia_id_dia_hora)
    if request.method == "POST":
        atividade.titulo = request.POST.get('titulo')
        atividade.capacidade = request.POST.get('capacidade')
        atividade.duracao = request.POST.get('duracao')
        atividade.validada = 2
        atividade.iddepartamento = request.POST.get('iddepartamento')
        atividade.publico_alvo = request.POST.get('publico_alvo')
        atividade.descricao = request.POST.get('descricao')
        atividade.tematica = request.POST.get('tema')
        atividade.ncolboradores = request.POST.get('ncolaboradores')
        atividade.save()
        return redirect("../../editar_local/"+str(idActivity))
    context = {
        "id": request.session["user_id"],
        "activity": atividade,
        "espaco": espaco,
        "professor": professor,
        "campus": campus,
        "departamentos": departamento,
        "unidade_organica": unidade_organica,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_atividade.html", context)


def all_activities_view(request):
    atividades = Atividade.objects.all().filter(validada=1)
    campus_filter = ""
    uo_filter = ""
    departamento_filter = ""
    tema_filter = ""
    titulo_filter = ""
    if request.method == "POST":
        if request.POST.get("unidade_organica"):
            atividades = atividades.filter(unidade_organica_iduo=request.POST.get("unidade_organica"))
            uo_filter = get_object_or_404(UnidadeOrganica, iduo=request.POST.get("unidade_organica")).iduo
        if request.POST.get("departamento"):
            atividades = atividades.filter(departamento_iddepartamento=request.POST.get("departamento"))
            departamento_filter = get_object_or_404(Departamento, iddepartamento=request.POST.get("departamento")).iddepartamento
        if request.POST.get("temaAtividade"):
            atividades = atividades.filter(tematica__icontains=request.POST.get("temaAtividade"))
            tema_filter = request.POST.get("temaAtividade")
        if request.POST.get("nomeAtividade"):
            atividades = atividades.filter(titulo__icontains=request.POST.get("nomeAtividade"))
            titulo_filter = request.POST.get("nomeAtividade")
        if request.POST.get("campus"):
            campus_atividade = []
            for atv in atividades:
                if atv.unidade_organica_iduo.campus_idcampus == get_object_or_404(Campus, idcampus=request.POST.get("campus")):
                    campus_atividade.append(atv)
            atividades = campus_atividade
            campus_filter = get_object_or_404(Campus, idcampus=request.POST.get("campus")).idcampus
    context = {
        "campus_filter": campus_filter,
        "uo_filter": uo_filter,
        "departamento_filter": departamento_filter,
        "tema_filter": tema_filter,
        "titulo_filter": titulo_filter,
        "campus": Campus.objects.all(),
        "uo": UnidadeOrganica.objects.all(),
        "departamentos": Departamento.objects.all(),
        "list": atividades,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/consultar_todas_atividades.html", context)


def info_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    context = {
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/info_atividade.html", context)


def coordinator_activities_view(request):
    departamento_filter = ""
    tema_filter = ""
    titulo_filter = ""
    estado_filter = ""
    unidade_organica = get_object_or_404(Coordenador,
                                         utilizador_idutilizador=request.session["user_id"]).unidade_organica_iduo.iduo
    atividades = Atividade.objects.all().filter(unidade_organica_iduo=unidade_organica)
    if request.method == "POST":
        if request.POST.get("departamento"):
            atividades = atividades.filter(departamento_iddepartamento=request.POST.get("departamento"))
            departamento_filter = get_object_or_404(Departamento,
                                                    iddepartamento=request.POST.get("departamento")).iddepartamento
        if request.POST.get("estado"):
            validada = int(request.POST.get("estado"))
            if validada == 0:
                options = [0, 2]
                print(atividades.filter(validada__in=options))
                atividades = atividades.filter(validada__in=options)
                print(atividades)
            else:
                atividades = atividades.filter(validada=validada)
            estado_filter = request.POST.get("estado")
        if request.POST.get("temaAtividade"):
            atividades = atividades.filter(tematica__icontains=request.POST.get("temaAtividade"))
            tema_filter = request.POST.get("temaAtividade")
        if request.POST.get("nomeAtividade"):
            atividades = atividades.filter(titulo__icontains=request.POST.get("nomeAtividade"))
            titulo_filter = request.POST.get("nomeAtividade")
    context = {
        "departamento_filter": departamento_filter,
        "tema_filter": tema_filter,
        "titulo_filter": titulo_filter,
        "estado_filter": estado_filter,
        "departamentos": Departamento.objects.all(),
        "list": atividades,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/consultar_atividades_coordenador.html", context)


def validar_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    if request.method == "POST":
        atividade.validada = 1
        atividade.save()
        return redirect("atividades:consultar_atividades_coodernador")
    context = {
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/aceitar_atividade.html", context)


def recusar_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    if request.method == "POST":
        atividade.validada = -1
        atividade.save()
        return redirect("atividades:consultar_atividades_coodernador")
    context = {
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/recusar_atividade.html", context)


def deletar_atividade_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    if request.method == "POST":
        atividade.delete()
        return redirect("atividades:consultar_minhas_atividades")
    context = {
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_atividade.html", context)


# --------------------------------Sessão:

def delete_session(request, idSession):
    sessao = get_object_or_404(Sessao, idsessao=idSession)
    if request.method == "POST":
        sessao.delete()
        return redirect("../../editar_sessao/"+str(sessao.atividade_idatividade.idatividade))
    context = {
        "session": sessao,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_sessao.html", context)


def my_activities_view(request):
    querysetAtividade = Atividade.objects.all().filter(
        professor_universitario_utilizador_idutilizador=request.session["user_id"])
    context = {
        "list": querysetAtividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/consultar_atividades_professor.html", context)


def activity_session_view(request, idActivity):
    querysetSession = Sessao.objects.all().filter(atividade_idatividade=idActivity)
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    context = {
        "list": querysetSession,
        "activity": atividade,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/sessao_info.html", context)


def create_edit_session_view(request, idActivity):
    dia = Dia.objects.all()
    hora = Horario.objects.all()
    message = ""
    if request.method == "POST" and request.POST.get("hora") and request.POST.get("hora"):
        horario = get_object_or_404(HorarioHasDia, dia_dia=request.POST.get("dia"), horario_hora=request.POST.get("hora"))
        if not Sessao.objects.all().filter(atividade_idatividade=idActivity, horario_has_dia_id_dia_hora=horario):
            atividade = get_object_or_404(Atividade, idatividade=idActivity)
            newSession = Sessao(nrinscritos=0, vagas=atividade.capacidade,
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
    }
    return render(request, "atividades/criar_editar_sessao.html", context)


# --------------------------------Espaço:

def criar_sala_view(request):
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
    context = {
        "list": lista,
        "espaco": espaco,
        "form": form,
        "campus": campus,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_sala.html", context)


def deletar_espaco_view(request, idEspaco):
    local = get_object_or_404(Espaco, idespaco=idEspaco)
    if request.method == "POST":
        local.delete()
        return redirect("atividades:criar_sala")
    context = {
        "local": local,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_local.html", context)


def especificar_espaco(request, idEspaco):
    fields = 0
    local = get_object_or_404(Espaco, idespaco=idEspaco)
    if request.method == "POST":
        fields = request.POST.get('tipoSala')
        if fields == "1" and request.POST.get('edificio') and request.POST.get('andar'):
            new = Sala(edificio=request.POST.get('edificio'), andar=request.POST.get('andar'), espaco_idespaco=local)
            new.save()
            return redirect("atividades:criar_sala")
        elif fields == "2" and request.POST.get('edificio') and request.POST.get('andar'):
            new = Anfiteatro(edificio=request.POST.get('edificio'), andar=request.POST.get('andar'), espaco_idespaco=local)
            new.save()
            return redirect("atividades:criar_sala")
        elif fields == "3" and request.POST.get('descricao'):
            new = Arlivre(descricao=request.POST.get('descricao'), espaco_idespaco=local)
            new.save()
            return redirect("atividades:criar_sala")
    context = {
        "fields": fields,
        "local": local,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/especificar_espaco.html", context)


def editar_local_view(request, idActivity):
    atividade = get_object_or_404(Atividade, idatividade=idActivity)
    espaco = []
    allbuildings = []
    selectedBuilding = None
    fields = 0
    if request.method == "POST":
        if request.POST.get('espaco'):
            atividade.espaco_idespaco = get_object_or_404(Espaco, idespaco=request.POST.get('espaco'))
            atividade.save()
            if account == 'coordinator':
                return redirect("atividades:consultar_atividades_coodernador")
            elif account == 'professor':
                return redirect("../../editar_sessao/" + str(idActivity))
        elif request.POST.get('semSala') and account == 'coordinator':
            return redirect("atividades:consultar_atividades_coodernador")
        elif request.POST.get('semSala') and account == 'professor':
            return redirect("../../editar_sessao/" + str(idActivity))
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
    context = {
        "activity": atividade,
        "espacos": espaco,
        "account": return_account_type(request.session["user_id"]),
        "fields": fields,
        "edificios": allbuildings,
        "selectedBuilding": selectedBuilding,
    }
    return render(request, "atividades/editar_local.html", context)


# --------------------------------Outros:

def show_image(request, image):
    mapa = get_object_or_404(Espaco, idespaco=image).img
    context = {
        "image": mapa
    }
    return render(request, "atividades/show_image.html", context)


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
    if request.method == 'POST':
        new = Campus(nome=request.POST.get('nome'))
        new.save()
    context = {
        "campus": campus,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_campus.html", context)


def apagar_campus_view(request, idCampus):
    campus = get_object_or_404(Campus, idcampus=idCampus)
    if request.method == "POST":
        campus.delete()
        return redirect("atividades:criar_campus")
    context = {
        "campus": campus,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_campus.html", context)


# --------------------------------Unidade Orgãnica:

def criar_uo_view(request):
    uo = UnidadeOrganica.objects.all()
    form = UoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        "uo": uo,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_uo.html", context)


def apagar_uo_view(request, idUo):
    uo = get_object_or_404(UnidadeOrganica, iduo=idUo)
    if request.method == "POST":
        uo.delete()
        return redirect("atividades:criar_uo")
    context = {
        "uo": uo,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_uo.html", context)


# --------------------------------Departamento:

def criar_departamento_view(request):
    departamento = Departamento.objects.all()
    form = DepartamentoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    context = {
        "form": form,
        "departamento": departamento,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/criar_departamento.html", context)


def apagar_departamento_view(request, idDepartamento):
    departamento = get_object_or_404(Departamento, iddepartamento=idDepartamento)
    if request.method == "POST":
        departamento.delete()
        return redirect("atividades:criar_departamento")
    context = {
        "departamento": departamento,
        "account": return_account_type(request.session["user_id"]),
    }
    return render(request, "atividades/apagar_departamento.html", context)

# --------------------------------Extras:


def login_view(request):
    if request.method == "POST":
        request.session["user_id"] = get_object_or_404(Utilizador, username=request.POST.get('username')).idutilizador
        return redirect("atividades:home_page")
    return render(request, "atividades/login.html")


def logout_view(request):
    del request.session["user_id"]
    return redirect("atividades:login")




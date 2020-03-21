from .models import Utilizador,Participante,Colaborador,Administrador,ProfessorUniversitario,Coordenador
ADMINISTRADOR = 1
COORDENADOR = 2
PARTICIPANTE = 3
PROFESSOR_UNIVERSITARIO = 4
COLABORADOR = 5

NONE = 0

#Retorna um uitilizador com os mesmos campos da base de dados e com um atributo adicional (type) que será 
#um dos campos acima, caso o user não exista retorna 0

def getCurrentUser(_id):
    if _id == 0:
        return 0

    user = Utilizador.objects.filter(idutilizador = _id).first()

    if user == None:
        return 0

    part = Participante.objects.select_related().filter(utilizador_idutilizador = _id).first()
    if part != None:
        part.type = PARTICIPANTE 
        return part
    
    coord = Coordenador.objects.select_related().filter(utilizador_idutilizador = _id).first()
    if coord != None:
        coord.type = COORDENADOR 
        return coord

    prof = ProfessorUniversitario.objects.select_related().filter(utilizador_idutilizador = _id).first()
    if prof != None:
        prof.type = PROFESSOR_UNIVERSITARIO 
        return prof

    admin = Administrador.objects.select_related().filter(utilizador_idutilizador = _id).first()
    if admin != None:
        admin.type = ADMINISTRADOR 
        return admin
    
    colab = Colaborador.objects.select_related().filter(utilizador_idutilizador = _id).first()
    if colab != None:
        colab.type = COLABORADOR
        return colab

    user.type = NONE
    return user
    

def getLoggedUser(request):
    if request.session.is_empty():
        return 0
    return getCurrentUser(request.session['user_id'])
    
    


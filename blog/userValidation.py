from .models import Utilizador,Participante,Colaborador,Administrador,ProfessorUniversitario,Coordenador
ADMINISTRADOR = 4
COORDENADOR = 2
PARTICIPANTE = 0
PROFESSOR_UNIVERSITARIO = 3
COLABORADOR = 1

NONE = -1
class Container(object):
    pass 

#Retorna um utilizador com os mesmos campos da base de dados e com um atributo adicional (type) que será 
#um dos campos acima

def getCurrentUser(_id):
    user = Utilizador.objects.get(idutilizador = _id)

    if user == None:
        value = Container
        value._type = NONE
        return value

    if user.validada == 0:
        part = Participante.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        part.user = user
        part._type = PARTICIPANTE
        return part
    
    if user.validada == 1:
        colab = Colaborador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        colab.user = user
        colab._type = COLABORADOR
        return colab
    
    if user.validada == 2:
        coord = Coordenador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        coord._type = COORDENADOR
        coord.user = user
        return coord

    if user.validada == 3:
        prof._type=PROFESSOR_UNIVERSITARIO
        prof = ProfessorUniversitario.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        prof.user = user
        return prof

    if user.validada == 4:
        admin = Administrador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        admin.user = user
        admin._type = ADMINISTRADOR 
        return admin
    

    user._type = NONE
    return user
    

def getLoggedUser(request):
    if 'user_id' not in request.session:
        value = Container()
        value._type = NONE
        return value
    return getCurrentUser(request.session['user_id'])
    
    


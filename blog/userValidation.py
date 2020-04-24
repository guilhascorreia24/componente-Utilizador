from .models import Utilizador,Participante,Colaborador,Administrador,ProfessorUniversitario,Coordenador
ADMINISTRADOR = 1
COORDENADOR = 2
PARTICIPANTE = 3
PROFESSOR_UNIVERSITARIO = 4
COLABORADOR = 5

NONE = 0
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
        part._type = PARTICIPANTE
        return part
    
    if user.validada == 1:
        colab = Colaborador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        colab._type = COLABORADOR
        return colab
    
    if user.validada == 2:
        coord = Coordenador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        coord._type = COORDENADOR 
        return coord

    if user.validada == 3:
        prof._type=PROFESSOR_UNIVERSITARIO
        prof = ProfessorUniversitario.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        return prof

    if user.validada == 4:
        admin = Administrador.objects.select_related('utilizador_idutilizador').get(utilizador_idutilizador = user)
        admin._type = ADMINISTRADOR 
        return admin
    

    user._type = NONE
    return user
    

def getLoggedUser(request):
    if request.session.is_empty():
        value = Container()
        value._type = NONE
        return value
    return getCurrentUser(request.session['user_id'])
    
    


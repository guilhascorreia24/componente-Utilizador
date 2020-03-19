from .models import Utilizador,Participante,Colaborador,Administrador,ProfessorUniversitario,Coordenador
ADMINISTRADOR = 1
COORDENADOR = 2
PARTICIPANTE = 3
PROFESSOR_UNIVERSITARIO = 4

NONE = 0

#Retorna um uitilizador com os mesmos campos da base de dados e com um atributo adicional (type) que será 
#um dos campos acima, caso o user não exista retorna 0

def getCurrentUser(_id):
    if _id == None:
        return 0

    user = Utilizador.objects.get(idutilizador = _id)

    if user == 0:
        return 0

    part = Participante.objects.get(utilizador_idutilizador = _id)
    if part != 0:
        part.type = PARTICIPANTE 
        return user
    
    coord = Coordenador.objects.get(utilizador_idutilizador = _id)
    if coord != 0:
        coord.type = COORDENADOR 
        return user

    prof = ProfessorUniversitario.objects.get(utilizador_idutilizador = _id)
    if prof != 0:
        user.type = PROFESSOR_UNIVERSITARIO 
        return user

    admin = Administrador.objects.get(utilizador_idutilizador = _id)
    if admin != 0:
        user.type = ADMINISTRADOR 
        return user

    user.type = NONE
    return user
    
    


import .models

ADMINISTRADOR = 1
COORDENADOR = 2
PARTICIPANTE = 3
PROFESSOR_UNIVERSITARIO = 4

NONE = 0

#Retorna um uitilizador com os mesmos campos da base de dados e com um atributo adicional (type) que será 
#um dos campos acima, caso o user não exista retorna 0

def getCurrentUser(request):
    _id = request.session['user-id']
    user = models.Utilizador.objects.get(idutilizador = _id)

    if user == 0
        return 0

    part = models.Participante.objects.get(idutilizador = _id)
    if part != 0:
        part.type = PARTICIPANTE 
        return user
    
    coord = models.Coordenador.objects.get(idutilizador = _id)
    if coord != 0:
        coord.type = COORDENADOR 
        return user

    prof = models.ProfessorUniversitario.objects.get(idutilizador = _id)
    if prof != 0:
        user.type = PROFESSOR_UNIVERSITARIO 
        return user

    admin = models.Administrador.objects.get(idutilizador = _id)
    if admin != 0:
        user.type = ADMINISTRADOR 
        return user

    user.type = NONE
    return user
    
    


from django.shortcuts import render, redirect
from atividades import models
from django.contrib.auth import authenticate, login, logout
from blog import userValidation

# Main Views.
def atividades_show(request):

    print(request.session['user_id'])
    user = userValidation.getCurrentUser(request.session['user_id'])

    #Error user non existent
    if user == 0:
        return 0

    #Error user has no type
    if user.type == userValidation.NONE:
        return 0

    if user.type == userValidation.PARTICIPANTE:
        return atividade_participante_show(request)

    if user.type == userValidation.PROFESSOR_UNIVERSITARIO:
        return atividade_professor_show(request)

    if user.type == userValidation.COORDENADOR:
        return atividade_coordenador_show(request)
    
    if user.type == userValidation.ADMINISTRADOR:
        return atividade_administrador_show(request)

    raise Exception('Uknown error showing template')

def atividades_register(request):
    return 0

def atividades_create(request):
    return 0

def atividades_validate(request):
    return 0




def atividade_participante_show(request):
    return render(request = request,template_name = "atividades_participante_show.html")

def atividade_coordenador_show(request):
    return render(request = request,template_name = "atividades_coordenador_show.html")

def atividade_professor_show(request):
    return render(request = request,template_name = "atividades_professor_show.html")

def atividade_administrador_show(request):
    return render(request = request,template_name = "atividades_administrador_show.html")




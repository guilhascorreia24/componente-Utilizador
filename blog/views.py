
from django.shortcuts import render
from .models import Participante, Administrador, Coordenador, Colaborador, ProfessorUniversitario


def home(request):
    if 'cookie_id' in request.COOKIES:
        print("cookie:"+request.COOKIES['cookie_id'])
        request.session['user_id']=request.COOKIES['cookie_id']
    if 'user_id' in request.session:
        print("session:"+str(request.session['user_id']))
        id=request.session['user_id']
        if Participante.objects.filter(utilizador_idutilizador=id).exists():
            funcao="part"
        elif Coordenador.objects.filter(utilizador_idutilizador=id).exists():
            funcao="coord"
        elif Administrador.objects.filter(utilizador_idutilizador=id).exists():
            funcao="admin"
        elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id).exists():
            funcao="dc"
        elif Colaborador.objects.filter(utilizador_idutilizador=id).exists():
            funcao="colab"
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.

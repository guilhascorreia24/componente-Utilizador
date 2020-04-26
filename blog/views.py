
from django.shortcuts import render
from .models import Administrador, Coordenador, Colaborador, Participante, ProfessorUniversitario
from django.core import signing
def home(request):
    if 'cookie_id' in request.COOKIES:
        request.session['user_id']=signing.loads(request.COOKIES['cookie_id'])
    if 'user_id' in request.session:
        id1=request.session['user_id']
        if Participante.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "part"
        elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "dc"
        elif Administrador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "admin"
        elif Coordenador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "coord"
        elif Colaborador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "colab"
        id=signing.dumps(id1)
        return render(request, 'homepage.html', context={'id':id,'funcao':funcao})
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.

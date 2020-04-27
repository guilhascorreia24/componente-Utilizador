
from django.shortcuts import render
from .models import Administrador, Coordenador, Colaborador, Participante, ProfessorUniversitario
from django.core import signing
from cryptography.fernet import Fernet
import base64
import logging
import traceback
from django.conf import settings
def home(request):
    if 'cookie_id' in request.COOKIES:
        cookie=request.COOKIES['cookie_id']
        request.session['user_id']=decrypt(cookie)
    if 'user_id' in request.session:
        id1=request.session['user_id']
       # print( Administrador.objects.filter(utilizador_idutilizador=id1).exists())
        if Participante.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "part"
            return render(request, 'navbar-part.html', context={})
        elif ProfessorUniversitario.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "dc"
        elif Administrador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "admin"
        elif Coordenador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "coord"
        elif Colaborador.objects.filter(utilizador_idutilizador=id1).exists():
            funcao = "colab"
        id=encrypt(id1)
        print(id)
        return render(request, 'homepage.html', context={'id':id,'funcao':funcao})
    else:
        id=None
    return render(request, 'homepage.html', context={'id':id})
# Create your views here.

def encrypt(txt):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None
def decrypt(txt):
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
        return decoded_text

from django.shortcuts import render, redirect
from atividades import models
from django.contrib.auth import authenticate, login, logout
from blog import userValidation
from atividades import forms
from django.forms import formset_factory
from atividades import inscricao

# Main Views.
def test(request):
    return inscricao.showForm(request)
    
def atividades_show(request):
    user = userValidation.getLoggedUser(request)

    #Error user non existent
    if user == 0:
        error = "Erro, não tem sessão iniciada"
        return render(request, 'error.html',{'message':error})

    #Error user has no type
    if user.type == userValidation.NONE:
        error = "Erro, utilizador não pertence a nenhum grupo de utilizadores"
        return render(request, 'error.html',{'message':error})

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
    return atividade_participante_show(request)

def atividades_create(request):
    user = userValidation.getLoggedUser(request)

    if user == 0:
        error = "Erro, não tem sessão iniciada"
        return render(request, 'error.html',{'message':error})
    
    if userValidation.PROFESSOR_UNIVERSITARIO != user.type:
        error = "Erro, não tem permissao para aceder a esta pagina"
        return render(request, 'error.html',{'message':error})

    if request.method == 'POST':
        ativ_form = forms.Form_Create_Atividades(request.POST)
        ativ_form_edit = ativ_form.save(commit = False)
        ativ_form_edit.departamento_iddepartamento = models.Departamento.objects.get(iddepartamento = user.departamento_iddepartamento.iddepartamento)
        ativ_form_edit.unidade_organica_iduo = models.UnidadeOrganica.objects.get(iduo = user.departamento_iddepartamento.unidade_organica_iduo.iduo)
        ativ_form_edit.professor_universitario_utilizador_idutilizador = models.ProfessorUniversitario.objects.get(utilizador_idutilizador = user.utilizador_idutilizador.idutilizador)
        ativ_form_edit.save()

        formset_sessions = formset_factory(forms.Form_Create_Sessao)
        for form in formset_sessions:
            form.nrinscritos = 0
            form.vagas = 0
            form.atividade_idatividade = ativ_form.idatividade
            form.save()

        render(request,"success.html")


    else:
        form_Atividades = forms.Form_Create_Atividades()
        formset_sessions = formset_factory(forms.Form_Create_Sessao)
        
    
    return render(request,"atividades_create.html",{"form_atividade":form_Atividades,"form_sessao":formset_sessions})

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



def test1(request):
    return inscricao.show(request)
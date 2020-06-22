from django.shortcuts import render,redirect
from user import views
from Notification.views import noti_not_checked
from blog.models import Curso
from .forms import cursoForm

# Create your views here.
def curso_form(request):
    cursos=Curso.objects.all()
    func=views.user(request)
    if request.method=='POST' and not(Curso.objects.filter(nome=request.POST['nome']).exists() and Unidade.objects.filter(unidade_organica_iduo=request.POST['unidade_organica_iduo'])):
        form=cursoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
         form=cursoForm()
    context={'form':form,'cursos':cursos,'id':request.session['user_id'],'funcao':func,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
    return render(request,'cursos.html',context)

def delete_curso(request,idcurso):
    print("curso"+idcurso)
    if Curso.objects.filter(pk=idcurso).exists() and request.session['type']==4:
        Curso.objects.filter(pk=idcurso).delete()
    return redirect("formularios:cursos")
        

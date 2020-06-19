from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import TarefaFilter
from Notification.views import noti_not_checked

def homepage(request):
    return render(request=request,
    			  template_name="main/inicio.html",
    			  )

def criar_tarefa(request):
    return render(request=request,
    			  template_name="main/criarTarefa.html",
    			  )

def mais_info(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	context={'tarefa':tarefa,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request=request,
				template_name="main/info_atividade.html",
				context=context)

def criar_tarefa_atividade(request):
	user = Utilizador.objects.get(idutilizador = 4)
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user)
	new_form = Tarefa(concluida = 1, coordenador_utilizador_idutilizador = coord_user)
	form = TarefasFormAtividade(request.POST, instance = new_form)
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			new_tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST['idsession'])
			if request.POST['colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
			new_tarefa.save()
			return redirect("homepage")
	
	return render(request=request,
				  template_name="main/criarTarefaAtividade.html",
				  context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_grupo(request):
	sessao = request.POST.get('sessao')
	inscricao = Inscricao.objects.filter(idinscricao__in = InscricaoHasSessao.objects.filter(sessao_idsessao=sessao))
	grupos = InscricaoColetiva.objects.filter(inscricao_idinscricao__in = inscricao)
	return render(request=request,
				  template_name="main/grupo_dropdown.html",
				  context={'grupos':grupos,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_espaco(request):
	atividade = request.POST.get('campus')
	espaco = Atividade.objects.filter(idatividade = atividade) 
	return render(request=request,
				  template_name="main/sala_dropdown.html",
				  context={'espaco':espaco,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def criar_tarefa_grupo(request):
	user = Utilizador.objects.get(idutilizador = 4)
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user)
	new_form = Tarefa(concluida = 1, coordenador_utilizador_idutilizador = coord_user)
	form = TarefasFormGroup(request.POST, instance = new_form)
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			new_tarefa.hora_inicio = request.POST['hora_inicio']
			new_tarefa.dia_dia = Dia.objects.get(dia=request.POST['dia_dia'])
			if request.POST['colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
			ativid = Atividade.objects.get(idatividade = request.POST['atividade_idatividade'])
			new_tarefa.buscar = Espaco.objects.get(idespaco = ativid.espaco_idespaco.idespaco)
			new_tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
			grupo = Inscricao.objects.get(idinscricao = request.POST['grupos'])
			new_tarefa.inscricao_coletiva_inscricao_idinscricao = InscricaoColetiva.objects.get(inscricao_idinscricao = grupo)
			new_tarefa.save()
			return redirect("homepage")
	
	return render(request=request,
				  template_name="main/criarTarefaAcompanhar.html",
				  context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_cities(request):
	atividade = request.POST.get('atividade_idatividade')
	sessao = Sessao.objects.filter(atividade_idatividade = atividade) 
	return render(request=request,
				  template_name="main/sessao_dropdown.html",
				  context={'sessao':sessao,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def consultar_tarefa(request):
	tarefas = Tarefa.objects.all()
	sessao = Sessao.objects.all()

	myFilter = TarefaFilter(request.GET, queryset=tarefas)
	tarefas = myFilter.qs

	context={'tarefas': tarefas,
			'sessao': sessao,
			'myFilter': myFilter,
			'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request=request,
				  template_name="main/consultarTarefa.html",
 				  context=context)

def editar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	if tarefa.sessao_idsessao == None:
		template="main/criarTarefaAcompanhar.html"
		form = TarefasFormGroup(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormGroup(request.POST, instance = tarefa)
			if form.is_valid():
				form.save()
				return redirect("homepage")
	else:
		template="main/criarTarefaAtividade.html"
		form = TarefasFormAtividade(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormAtividade(request.POST, instance = tarefa)
			if form.is_valid():
				form.save()
				return redirect("homepage")
	return render(request = request,
				 template_name=template,
				 context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def eliminar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	if request.method == "POST":
		tarefa.delete()
		return redirect("consultar_tarefa")
	context ={'tarefa': tarefa,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request = request,
				 template_name="main/eliminarTarefa.html",
				 context=context)
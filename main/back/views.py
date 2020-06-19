from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import TarefaFilter

# Create your views here.
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
	sala = ''
	if tarefa.buscar != None:
		sala = Sala.objects.get(espaco_idespaco = tarefa.buscar.idespaco)
	else:
		sala = Sala.objects.get(espaco_idespaco = tarefa.sessao_idsessao.atividade_idatividade.espaco_idespaco.idespaco)
	context={'tarefa':tarefa, 'sala':sala}
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
				  context={'form':form})

def load_espaco(request):
	campus = request.POST.get('campus')
	espaco = Espaco.objects.filter(campus_idcampus = campus) 
	return render(request=request,
				  template_name="main/sala_dropdown.html",
				  context={'espaco':espaco})

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
			new_tarefa.buscar = Espaco.objects.get(idespaco = request.POST['buscar'])
			new_tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
			new_tarefa.save()
			return redirect("homepage")
	
	return render(request=request,
				  template_name="main/criarTarefaAcompanhar.html",
				  context={'form':form})

def load_cities(request):
	atividade = request.POST.get('atividade_idatividade')
	sessao = Sessao.objects.filter(atividade_idatividade = atividade) 
	return render(request=request,
				  template_name="main/sessao_dropdown.html",
				  context={'sessao':sessao})

def consultar_tarefa(request):
	tarefas = Tarefa.objects.all()
	sessao = Sessao.objects.all()

	myFilter = TarefaFilter(request.GET, queryset=tarefas)
	tarefas = myFilter.qs

	context={'tarefas': tarefas,
			'sessao': sessao,
			'myFilter': myFilter}
	return render(request=request,
				  template_name="main/consultarTarefa.html",
				  context=context)

def editar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	form = TarefasForm(instance = tarefa)
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			if request.POST['colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
			if request.POST['atividade_idatividade'] != '':
				new_tarefa.atividade_idatividade = Atividade.objects.get(idatividade = request.POST['atividade_idatividade']) #Atribuimos uma atividade a tarefa
			else:
				new_tarefa.hora_inicio = request.POST['hora_inicio']
				new_tarefa.dia_dia = Dia.objects.get(dia=request.POST['dia_dia'])
			new_tarefa.save()
			return redirect("homepage")
	context = {'form':form}
	return render(request = request,
				 template_name="main/editarTarefa.html",
				 context=context)

def eliminar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	if request.method == "POST":
		tarefa.delete()
		return redirect("consultar_tarefa")
	context ={'tarefa': tarefa}
	return render(request = request,
				 template_name="main/eliminarTarefa.html",
				 context=context)
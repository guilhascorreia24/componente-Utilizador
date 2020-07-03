from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from Notification.views import noti_not_checked
import datetime, time
from django.db.models import F
from Notification import views as noti_views

def criar_tarefa(request):
    return render(request=request,
    			  template_name="main/criarTarefa.html",
    			  context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def criar_tarefa_atividade(request):
	user_coord = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user_coord)
	atividade = Atividade.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	form = TarefasFormAtividade(request.POST)
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			new_tarefa.concluida = 0
			new_tarefa.coordenador_utilizador_idutilizador = coord_user
			new_tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST['idsession'])
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['id_colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
				new_tarefa.save()
				noti_views.new_noti(request,colaborador_user.pk,'Tarefa ' + '"' + new_tarefa.nome + '"','Foi atribuido uma Nova Tarefa ' + '"' + new_tarefa.nome + '"')
			else:
				new_tarefa.save()
			messages.success(request, f'Tarefa Criada com Sucesso!')
			return redirect("tarefa_coordenador:consultar_tarefa")

	return render(request=request,
				  template_name="main/criarTarefaAtividade.html",
				  context={'atividade':atividade,'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_grupo(request):
	ses = request.POST.get('sessao')
	hassessao =  InscricaoHasSessao.objects.filter(sessao_idsessao=ses )
	inscricao = Inscricao.objects.filter(idinscricao__in = hassessao)
	grupos = InscricaoColetiva.objects.filter(inscricao_idinscricao__in = inscricao)
	return render(request=request,
				  template_name="main/grupo_dropdown.html",
				  context={'grupos':grupos,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_colab_guiar(request):
	user_coord = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user_coord)
	sessao = Sessao.objects.get(idsessao = request.POST.get('sessao'))
	horario = HorarioHasDia.objects.get(id_dia_hora = sessao.horario_has_dia_id_dia_hora.pk)
	dia = Dia.objects.get(dia = horario.dia_dia.pk)
	curso =  Curso.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	c = Colaborador.objects.filter(curso_idcurso__in = curso)
	colab = Disponibilidade.objects.filter(colaborador_utilizador_idutilizador__in = c, dia_dia = dia).exclude(tipo_de_tarefa="Ajudar Docente")
	return render(request=request,
				  template_name="main/colab_dropdown.html",
				  context={'colab':colab,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_colab_ajudar(request):
	user_coord = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user_coord)
	sessao = Sessao.objects.get(idsessao = request.POST.get('sessao'))
	horario = HorarioHasDia.objects.get(id_dia_hora = sessao.horario_has_dia_id_dia_hora.pk)
	dia = Dia.objects.get(dia = horario.dia_dia.pk)
	curso =  Curso.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	c = Colaborador.objects.filter(curso_idcurso__in = curso)
	colab = Disponibilidade.objects.filter(colaborador_utilizador_idutilizador__in = c, dia_dia = dia).exclude(tipo_de_tarefa="Guiar Grupo")
	return render(request=request,
				  template_name="main/colab_dropdown.html",
				  context={'colab':colab,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})


def load_espaco(request):
	atividade = request.POST.get('campus')
	espaco = Atividade.objects.filter(idatividade = atividade)
	sala = Sala.objects.all()
	anfi = Anfiteatro.objects.all()
	ar = Arlivre.objects.all()
	
	return render(request=request,
				  template_name="main/sala_dropdown.html",
				  context={'espaco':espaco,'ar':ar,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'anfi':anfi,'sala':sala,})

def criar_tarefa_grupo(request):
	user2 = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user2)
	new_form = Tarefa(concluida = 0, coordenador_utilizador_idutilizador = coord_user)
	print(coord_user.unidade_organica_iduo)
	atividade = Atividade.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	form = TarefasFormGroup(request.POST, instance = new_form)
	# dispos = disponibilidades("Guiar Grupo")
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['id_colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
			ativid = Atividade.objects.get(idatividade = request.POST['atividade_idatividade'])
			new_tarefa.buscar = Espaco.objects.get(idespaco = ativid.espaco_idespaco.idespaco)
			new_tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
			grupo = Inscricao.objects.get(idinscricao = request.POST['grupos'])
			new_tarefa.inscricao_coletiva_inscricao_idinscricao = InscricaoColetiva.objects.get(inscricao_idinscricao = grupo)
			new_tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST['idsession'])
			inicio = Sessao.objects.get(idsessao=request.POST['idsession']).horario_has_dia_id_dia_hora.horario_hora.hora
			duracao = ativid.duracao*60
			inicio_s = inicio.hour * 3600 + inicio.minute * 60 + inicio.second
			total = inicio_s + duracao
			new_tarefa.hora_inicio = time.strftime('%H:%M:%S', time.gmtime(total))
			new_tarefa.dia_dia = Dia.objects.get(dia= Sessao.objects.get(idsessao=request.POST['idsession']).horario_has_dia_id_dia_hora.dia_dia.dia)
			new_tarefa.save()
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				noti_views.new_noti(request,colaborador_user.pk,'Tarefa ' + '"' + new_tarefa.nome + '"','Foi atribuido uma Nova Tarefa '+ '"' + new_tarefa.nome + '"')
			messages.success(request, f'Tarefa Criada com Sucesso!')
			return redirect("tarefa_coordenador:consultar_tarefa")
	
	return render(request=request,
				  template_name="main/criarTarefaAcompanhar.html",
				  context={'atividade':atividade,'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def load_cities(request):
	atividade = request.POST.get('atividade_idatividade')
	sessao = Sessao.objects.filter(atividade_idatividade = atividade) 
	return render(request=request,
				  template_name="main/sessao_dropdown.html",
				  context={'sessao':sessao,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def consultar_tarefa(request):
	user2 = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user2)
	tarefas = Tarefa.objects.filter(coordenador_utilizador_idutilizador = coord_user)
	sessao = Sessao.objects.all()
	user_coord = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user_coord)
	curso =  Curso.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	colab = Colaborador.objects.filter(curso_idcurso__in = curso)
	atividade = Atividade.objects.filter(unidade_organica_iduo = coord_user.unidade_organica_iduo)
	sala = Sala.objects.all()
	anfi = Anfiteatro.objects.all()
	ar = Arlivre.objects.all()

	context={'atividade':atividade,
			'tarefas': tarefas,
			'sessao': sessao,
			'colab': colab,
			'anfi':anfi,
			'sala':sala,
			'ar':ar,
			'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request=request,
				  template_name="main/consultarTarefa.html",
 				  context=context)

def consultar_tarefa_admin(request):
	tarefas = Tarefa.objects.all()
	unidade = UnidadeOrganica.objects.all()
	sessao = Sessao.objects.all()
	colab = Colaborador.objects.all()
	atividade = Atividade.objects.all()
	sala = Sala.objects.all()
	anfi = Anfiteatro.objects.all()
	ar = Arlivre.objects.all()

	context={'atividade':atividade,
			'unidade':unidade,
			'tarefas': tarefas,
			'sessao': sessao,
			'colab': colab,
			'anfi':anfi,
			'sala':sala,
			'ar':ar,
			'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request=request,
				  template_name="main/consultarTarefaAdmin.html",
 				  context=context)				   

def editar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	colab = tarefa.colaborador_utilizador_idutilizador
	sala = Sala.objects.all()
	anfi = Anfiteatro.objects.all()
	ar = Arlivre.objects.all()
	ati = Atividade.objects.filter(unidade_organica_iduo = tarefa.coordenador_utilizador_idutilizador.unidade_organica_iduo).exclude(idatividade = tarefa.sessao_idsessao.atividade_idatividade.idatividade)
	ati_levar = Atividade.objects.filter(unidade_organica_iduo = tarefa.coordenador_utilizador_idutilizador.unidade_organica_iduo)
	if tarefa.inscricao_coletiva_inscricao_idinscricao != None:
		# dispos=disponibilidades('Guiar Grupo')
		dispos = Disponibilidade.objects.exclude(tipo_de_tarefa='Ajudar Docente')
		template="main/editarTarefaAcompanhar.html"
		form = TarefasFormGroup(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormGroup(request.POST, instance = tarefa)
			if form.is_valid():
				tarefa.nome= request.POST["nome"]
				tarefa.concluida = 0
				ativid = Atividade.objects.get(idatividade = request.POST['atividade_idatividade'])
				tarefa.buscar = Espaco.objects.get(idespaco = ativid.espaco_idespaco.idespaco)
				tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
				grupo = Inscricao.objects.get(idinscricao = request.POST['grupos'])
				tarefa.inscricao_coletiva_inscricao_idinscricao = InscricaoColetiva.objects.get(inscricao_idinscricao = grupo)
				inicio = Sessao.objects.get(idsessao=request.POST['idsession']).horario_has_dia_id_dia_hora.horario_hora.hora
				duracao = ativid.duracao*60
				inicio_s = inicio.hour * 3600 + inicio.minute * 60 + inicio.second
				total = inicio_s + duracao
				tarefa.hora_inicio = time.strftime('%H:%M:%S', time.gmtime(total))
				tarefa.dia_dia = Dia.objects.get(dia= Sessao.objects.get(idsessao=request.POST['idsession']).horario_has_dia_id_dia_hora.dia_dia.dia)
				if request.POST['id_colaborador_utilizador_idutilizador'] != '':
					c = Colaborador.objects.get(utilizador_idutilizador = Utilizador.objects.get(idutilizador= request.POST["id_colaborador_utilizador_idutilizador"]))
					tarefa.colaborador_utilizador_idutilizador = c
					noti_views.new_noti(request,c.pk,'Tarefa Editada ' + '"' + tarefa.nome + '"','Foi editado a Tarefa ' + '"' + tarefa.nome + '"')
				else:
					tarefa.colaborador_utilizador_idutilizador = None
				tarefa.save()
				messages.success(request, f'Tarefa Editada com Sucesso!')
				return redirect("tarefa_coordenador:consultar_tarefa")
	else:
		dispos = Disponibilidade.objects.exclude(tipo_de_tarefa='Guiar Grupo')
		# dispos=disponibilidades('Ajudar Docente')
		template="main/editarTarefaAtividade.html"
		form = TarefasFormAtividade(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormAtividade(request.POST, instance = tarefa)
			if form.is_valid():
				tarefa = form.save(commit = False)
				tarefa.concluida = 0
				tarefa.nome= request.POST["nome"]
				tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST["idsession"])
				if request.POST['id_colaborador_utilizador_idutilizador'] != '':
					c = Colaborador.objects.get(utilizador_idutilizador = Utilizador.objects.get(idutilizador= request.POST["id_colaborador_utilizador_idutilizador"]))
					tarefa.colaborador_utilizador_idutilizador = c
					noti_views.new_noti(request,c.pk,'Tarefa Editada ' + '"' + tarefa.nome + '"','Foi editado a Tarefa ' + '"' + tarefa.nome + '"')
				else:
					tarefa.colaborador_utilizador_idutilizador = None
				tarefa.save()
				messages.success(request, f'Tarefa Editada com Sucesso!')
				return redirect("tarefa_coordenador:consultar_tarefa")
	return render(request = request,
				 template_name=template,
				 context={'sala':sala,'ar':ar,'anfi':anfi,'ati':ati,'ati_levar':ati_levar,'tarefa': tarefa,'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request), 'dispo':dispos})

def eliminar_tarefa(request, pk):
	if request.session["type"] == 4:
		if Tarefa.objects.filter(idtarefa = pk):
			tarefa = Tarefa.objects.get(idtarefa = pk)
			tarefa.delete()
			messages.success(request, f'Tarefa Eliminada com Sucesso!')
		else:
			messages.success(request, f'Não foi possível eliminar Tarefa!')
		return redirect("tarefa_coordenador:consultar_tarefa_admin")
	else:	
		if Tarefa.objects.filter(idtarefa = pk):
			tarefa = Tarefa.objects.get(idtarefa = pk)
			tarefa.delete()
			messages.success(request, f'Tarefa Eliminada com Sucesso!')
		else:
			messages.success(request, f'Não foi possível eliminar Tarefa!')
		return redirect("tarefa_coordenador:consultar_tarefa")
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import TarefaFilter
from Notification.views import noti_not_checked
import datetime, time
from django.db.models import F
from Notification import views as noti_views

def homepage(request):
    return render(request=request,
    			  template_name="main/inicio.html",
    			  )

def criar_tarefa(request):
    return render(request=request,
    			  template_name="main/criarTarefa.html",
    			  context={'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def mais_info(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	if Sala.Objects.get(espaco_idespaco= tarefa.buscar) != '':
		sala_buscar = Sala.Objects.get(espaco_idespaco= tarefa.buscar)
	else:
		sala_buscar = Anfiteatro.Objects.get(espaco_idespaco= tarefa.buscar)
	if Sala.Objects.get(espaco_idespaco= tarefa.levar) != '':
		sala_levar= Sala.Objects.get(espaco_idespaco= tarefa.levar)
	else:
		sala_levar= Anfiteatro.Objects.get(espaco_idespaco= tarefa.levar)
	context={'tarefa':tarefa,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request), 'sala_buscar':sala_b, "sala_levar":sala_v}
	return render(request=request,
				template_name="main/info_atividade.html",
				context=context)

def same(object,list,string,string1,string2):
	for n in list:
		if isinstance(n[string2],datetime.time) and isinstance(object.horario_hora,Horario) and isinstance(n[string1],datetime.date) and isinstance(object.dia_dia,Dia):
			split=str(object.horario_hora).split(":")
			time=datetime.time(int(split[0]),int(split[1]),int(split[2]))
			split=str(object.dia_dia).split("-")
			date=datetime.date(int(split[0]),int(split[1]),int(split[2]))
			#print(str(n[string2]>=time and n[string1]==date and n[string]==object.colaborador_utilizador_idutilizador.pk))
			if n[string2]>=time and n[string1]==date and n[string]==object.colaborador_utilizador_idutilizador.pk:
				return True
	return False

def has(list,o):
	for l in list:
		if o==l.colaborador_utilizador_idutilizador.pk:
			return True
	return False

def disponibilidades(string):
	tarefas= Tarefa.objects \
		.select_related('colaborador_utilizador_idutilizador','hora_inicio','dia_dia','sessao_idsessao','sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora','sessao_idsessao__atividade_idatividade__duracao','sessao_idsessao__horario_has_dia_id_dia_hora__dia_dia').all()\
		.values(colab=F('colaborador_utilizador_idutilizador'),hora_i_a=F('hora_inicio'),dia_a=F('dia_dia'),hora_i_b=F('sessao_idsessao__horario_has_dia_id_dia_hora__horario_hora'),
			    				dia_b=F('sessao_idsessao__horario_has_dia_id_dia_hora__dia_dia'),hora_f_b=F('sessao_idsessao__atividade_idatividade__duracao'))
	disponibilidades=Disponibilidade.objects.all()
	for tare in tarefas:
		if isinstance(tare['hora_f_b'],float):
			min=int(tare['hora_f_b']+tare['hora_i_b'].minute)%60
			num=int(((tare['hora_f_b']+tare['hora_i_b'].minute)/60)+int(tare['hora_i_b'].hour))%24
			tare['hora_f_b']=datetime.time(num,min)
	dispos=[]
	#print(disponibilidades)
	for dispo in disponibilidades:
		#print(str(same(dispo,tarefas,'colab','dia_a','hora_i_a') or same2(dispo,tarefas,'colab','dia_b','hora_i_b','hora_f_b')))
		if not(same(dispo,tarefas,'colab','dia_a','hora_i_a')) and (dispo.tipo_de_tarefa==string or dispo.tipo_de_tarefa=='Sem preferência'):
			dispos.append(dispo)
	return dispos

def criar_tarefa_atividade(request):
	user_coord = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user_coord)
	new_form = Tarefa(concluida = 0, coordenador_utilizador_idutilizador = coord_user)
	form = TarefasFormAtividade(request.POST, instance = new_form)
	dispo = Disponibilidade.objects.exclude(tipo_de_tarefa= 'Guiar Grupo')
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			new_tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST['idsession'])
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['id_colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
				new_tarefa.save()
				noti_views.new_noti(request,colaborador_user.pk,'Tarefa','Foi atribuido uma Nova Tarefa')
			else:
				new_tarefa.save()
			print(new_tarefa)
			messages.success(request, f'Tarefa Criada com Sucesso!')
			return redirect("tarefa_coordenador:consultar_tarefa")

	return render(request=request,
				  template_name="main/criarTarefaAtividade.html",
				  context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'dispo':dispos})

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
	user2 = Utilizador.objects.get(idutilizador = request.session["user_id"])
	coord_user = Coordenador.objects.get(utilizador_idutilizador = user2)
	new_form = Tarefa(concluida = 0, coordenador_utilizador_idutilizador = coord_user)
	form = TarefasFormGroup(request.POST, instance = new_form)
	dispo = Disponibilidade.objects.exclude(tipo_de_tarefa= 'Ajudar Docente')
	if request.method == "POST":
		if form.is_valid():
			new_tarefa = form.save(commit = False)
			new_tarefa.hora_inicio = request.POST['hora_inicio']
			new_tarefa.dia_dia = Dia.objects.get(dia=request.POST['dia_dia'])
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				user = Utilizador.objects.get(idutilizador = request.POST['id_colaborador_utilizador_idutilizador']) #Vamos Buscar o Utilizador com o ID especificado no formulario
				colaborador_user = Colaborador.objects.get(utilizador_idutilizador = user)	#Vamos buscar o colaborador associado aquele objeto utilizador
				new_tarefa.colaborador_utilizador_idutilizador = colaborador_user	#Enviamos esse colaborador para a nova tarefa
			ativid = Atividade.objects.get(idatividade = request.POST['atividade_idatividade'])
			new_tarefa.buscar = Espaco.objects.get(idespaco = ativid.espaco_idespaco.idespaco)
			new_tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
			grupo = Inscricao.objects.get(idinscricao = request.POST['grupos'])
			new_tarefa.inscricao_coletiva_inscricao_idinscricao = InscricaoColetiva.objects.get(inscricao_idinscricao = grupo)
			new_tarefa.save()
			if request.POST['id_colaborador_utilizador_idutilizador'] != '':
				noti_views.new_noti(request,colaborador_user.pk,'Tarefa','Foi atribuido uma Nova Tarefa')
			messages.success(request, f'Tarefa Criada com Sucesso!')
			return redirect("tarefa_coordenador:consultar_tarefa")
	
	return render(request=request,
				  template_name="main/criarTarefaAcompanhar.html",
				  context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request),'dispo':dispo})

def load_cities(request):
	atividade = request.POST.get('atividade_idatividade')
	sessao = Sessao.objects.filter(atividade_idatividade = atividade) 
	return render(request=request,
				  template_name="main/sessao_dropdown.html",
				  context={'sessao':sessao,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)})

def consultar_tarefa(request):
	tarefas = Tarefa.objects.filter(coordenador_utilizador_idutilizador = request.session["user_id"])
	sessao = Sessao.objects.all()
	colab = Colaborador.objects.all()
	iduo = Coordenador.objects.get(pk = Utilizador.objects.get(pk= request.session["user_id"])).unidade_organica_iduo
	atividade = Atividade.objects.all()
	sala = Sala.objects.all()
	anfi = Anfiteatro.objects.all()

	context={'atividade':atividade,
			'tarefas': tarefas,
			'sessao': sessao,
			'colab': colab,
			'anfi':anfi,
			'sala':sala,
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
	myFilter = TarefaFilter(request.GET, queryset=tarefas)
	tarefas = myFilter.qs

	context={'atividade':atividade,
			'unidade':unidade,
			'tarefas': tarefas,
			'sessao': sessao,
			'myFilter': myFilter,
			'colab': colab,
			'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request)}
	return render(request=request,
				  template_name="main/consultarTarefaAdmin.html",
 				  context=context)				   

def editar_tarefa(request, pk):
	tarefa = Tarefa.objects.get(idtarefa = pk)
	if tarefa.sessao_idsessao == None:
		dispos=disponibilidades('Guiar Grupo')
		template="main/editarTarefaAcompanhar.html"
		form = TarefasFormGroup(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormGroup(request.POST, instance = tarefa)
			if form.is_valid():
				tarefa.nome= request.POST["nome"]
				tarefa.dia_dia = Dia.objects.get(dia = request.POST["dia_dia"])
				tarefa.hora_inicio = request.POST["hora_inicio"]
				if request.POST['colaborador_utilizador_idutilizador'] != '':
					tarefa.colaborador_utilizador_idutilizador = Colaborador.objects.get(utilizador_idutilizador = Utilizador.objects.get(idutilizador= request.POST["colaborador_utilizador_idutilizador"]))
				ativid = Atividade.objects.get(idatividade = request.POST['atividade_idatividade'])
				tarefa.buscar = Espaco.objects.get(idespaco = ativid.espaco_idespaco.idespaco)
				tarefa.levar = Espaco.objects.get(idespaco = request.POST['levar'])
				grupo = Inscricao.objects.get(idinscricao = request.POST['grupos'])
				tarefa.inscricao_coletiva_inscricao_idinscricao = InscricaoColetiva.objects.get(inscricao_idinscricao = grupo)
				tarefa.save()
				messages.success(request, f'Tarefa Editada com Sucesso!')
				return redirect("tarefa_coordenador:consultar_tarefa")
	else:
		dispos=disponibilidades('Ajudar Docente')
		template="main/editarTarefaAtividade.html"
		form = TarefasFormAtividade(instance = tarefa)
		if request.method == "POST":
			form = TarefasFormAtividade(request.POST, instance = tarefa)
			if form.is_valid():
				tarefa.nome= request.POST["nome"]
				tarefa.sessao_idsessao = Sessao.objects.get(idsessao = request.POST["idsession"])
				tarefa.colaborador_utilizador_idutilizador = Colaborador.objects.get(utilizador_idutilizador = Utilizador.objects.get(idutilizador= request.POST["colaborador_utilizador_idutilizador"]))
				tarefa.save()
				messages.success(request, f'Tarefa Editada com Sucesso!')
				return redirect("tarefa_coordenador:consultar_tarefa")
	return render(request = request,
				 template_name=template,
				 context={'form':form,'i':len(noti_not_checked(request)),'not_checked':noti_not_checked(request), 'dispo':dispos})

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
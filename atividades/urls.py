from django.contrib import admin
from django.urls import path
from atividades import views as atividades
from django.contrib.staticfiles.urls import static

app_name = 'atividades'
urlpatterns = [
    path('home', atividades.home_view, name='home_page'),
    # atividades:
    path('create', atividades.atividade_create_view, name='criar_atividade'),
    path('my_activities', atividades.my_activities_view, name='consultar_minhas_atividades'),
    path('all_activities', atividades.all_activities_view, name='consultar_atividades'),
    path('validar/<int:idActivity>/', atividades.validar_atividade_view, name='aceitar_atividade'),
    path('deletar/<int:idActivity>/', atividades.deletar_atividade_view, name='apagar_atividade'),
    path('editar/<int:idActivity>/', atividades.editar_atividade_view, name='editar_atividade'),
    path('coordinator_activities', atividades.coordinator_activities_view, name='consultar_atividades_coodernador'),
    # sessões:
    path('session/<int:idActivity>/', atividades.activity_session_view, name='ver_sessoes'),
    path('editar_sessao/<int:idActivity>/', atividades.create_edit_session_view, name='criar_editar_sessao'),
    path('deletar_sessao/<int:idSession>/', atividades.delete_session, name='apagar_sessao'),
    # local:
    path('criar_sala', atividades.criar_sala_view, name='criar_sala'),
    path('especificar_espaco/<int:idEspaco>/', atividades.especificar_espaco, name='especificar_espaco'),
    path('editar_local/<int:idActivity>/', atividades.editar_local_view, name='editar_local'),
    path('apagar_espaco/<int:idEspaco>/', atividades.deletar_espaco_view, name='apagar_local'),
    # imagens:
    path('show_image/<int:image>/', atividades.show_image, name='display_image'),
    # campus:
    path('criar_campus', atividades.criar_campus_view, name='criar_campus'),
    path('apagar_campus/<int:idCampus>/', atividades.apagar_campus_view, name='apagar_campus'),
    # Unidade Orgânica:
    path('criar_uo', atividades.criar_uo_view, name='criar_uo'),
    path('apagar_uo/<int:idUo>/', atividades.apagar_uo_view, name='apagar_uo'),
    # Departamento:
    path('criar_departamento', atividades.criar_departamento_view, name='criar_departamento'),
    path('apagar_departamento/<int:idDepartamento>/', atividades.apagar_departamento_view, name='apagar_departamento'),
    # extras:
    path('logout', atividades.logout_view, name='logout'),
    path('login', atividades.login_view, name="login"),

]

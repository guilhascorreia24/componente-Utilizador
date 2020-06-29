"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = "tarefa_coordenador"
urlpatterns = [
    path("criar_tarefa/", views.criar_tarefa, name="criar_tarefa"),
	path("criar_tarefa_atividade/", views.criar_tarefa_atividade, name='criar_tarefa_atividade'),
    path("criar_tarefa_grupo/", views.criar_tarefa_grupo, name='criar_tarefa_grupo'),
	path("consultar_tarefa/", views.consultar_tarefa, name='consultar_tarefa'),
    path("consultar_tarefa_admin/", views.consultar_tarefa_admin, name='consultar_tarefa_admin'),
    path("eliminar_tarefa/<str:pk>/", views.eliminar_tarefa, name='eliminar_tarefa'),
    path("editar_tarefa/<str:pk>/", views.editar_tarefa, name='editar_tarefa'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-espaco/', views.load_espaco, name='ajax_load_espaco'),
    path('ajax/load-grupo/', views.load_grupo, name='ajax_load_grupo'),
]

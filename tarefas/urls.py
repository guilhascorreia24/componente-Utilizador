from django.urls import path
from . import views

app_name = 'tarefas'
urlpatterns = [
    path('disponibilidade', views.consultar_tarefas, name='disponibilidade'),
    path('tarefas', views.consultar_tarefas2, name='tarefas'),
    path('delete', views.mudar_estado, name='mudar_estado')

]
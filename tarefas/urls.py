from django.urls import path
from . import views

app_name = 'tarefas'
urlpatterns = [
    path('disponibilidade', views.disponibilidade, name='disponibilidade'),
]
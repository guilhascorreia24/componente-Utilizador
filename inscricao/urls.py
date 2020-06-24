from django.urls import path
from . import views

app_name = 'inscricao'
urlpatterns = [
    path('consulta',views.consultar_inscricao,name='consulta'),
    path('register',views.inscricao_form,name='register'),
    path('register_individual',views.inscricao_individual_form,name='register_individual'),
    path('delete/<int:inscricao>',views.inscricao_delete,name='delete'),
    path('alterar/<int:inscricao>',views.inscricao_alterar,name='alterar'),
]
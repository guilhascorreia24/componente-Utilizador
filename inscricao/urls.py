from django.urls import path
from . import views

app_name = 'inscricao'
urlpatterns = [
    path('consulta',views.consultar_inscricao,name='consulta'),
    path('register',views.inscricao_form,name='register'),
    path('test',views.test,name='test')
]
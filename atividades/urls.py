from django.urls import path
from . import views

urlpatterns = [
    path('test',views.test,name='test'),
    path('show', views.atividades_show, name='atividades_show'),
    path('register', views.atividades_register, name='atividades_register'),
    path('create', views.atividades_create, name='atividades_create'),
    path('validate', views.atividades_validate, name='atividades_validate')
]
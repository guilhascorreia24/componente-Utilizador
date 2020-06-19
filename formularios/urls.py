from django.contrib import admin
from django.urls import path
from formularios import views 
app_name = 'formularios'
urlpatterns = [
    path('curso/', views.curso_form, name='cursos'),
    path('curso_delete/<str:idcurso>',views.delete_curso,name="delete_curso")]
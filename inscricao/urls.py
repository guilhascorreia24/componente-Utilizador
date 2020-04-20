from django.urls import path
from . import views

urlpatterns = [
    path('test1',views.test1,name='test1'),
    path('test',views.test,name='test'),
    path('register',views.inscricao_form,name="inscricao")
]
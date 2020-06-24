"""les URL Configuration

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
from .views import *

app_name = 'menu'

urlpatterns = [
    path('menu/', menu_list_view, name='menu_list'),
    path('menu/criar/', menu_create_view, name='menu_criar'),
    path('menu/criarprato/', prato_create_view, name='prato_criar'),
    path('menu/<int:id>/details/', menu_detail_view, name='menu_detail'),
    path('menu/update/<int:id>', menu_update_view, name='menu_update'),
    path('menu/updateprat/<int:id>', prato_update_view, name='prato_update'),
    path('menu/apagar/<int:id>', menu_delete_view, name='menu_delete'),
    path('menu/apagarprato/<int:id>', prato_delete_view, name='prato_delete'),
    
    path('transporte/', transporte_list_view, name='transporte-list'),
    path('transporte/criar/', transporte_create_view, name='transporte-criar'),
    path('transporte/criarhorario/', transportehora_create_view, name='transportehora-criar'),
    path('horario/', horario_create_view, name='horario-list'),
    path('transporte/details/<int:id>', transporte_detail_view, name='transporte-detail'),
    path('transporte/update/<int:id>', transporte_update_view, name='transporte-update'),
    path('/update2/<int:id>', transporte_update2_view, name='transporte-update2'),
    path('transporte/apagar/<int:id>', transporte_delete_view, name='transporte-delete'),
    
    path('', index, name='index'),
    path('diaaberto/', diaaberto_list, name='diaaberto_list'),
    path('criar/', diaaberto_create, name='diaaberto_create'),
    path('diaaberto/update/<int:id>', diaaberto_update, name='diaaberto_update'),
    path('diaaberto/apagar/<int:id>', diaaberto_delete, name='diaaberto_delete'),
    path('diaaberto/<int:id>/details/', diaaberto_details, name='diaaberto_details'),
]

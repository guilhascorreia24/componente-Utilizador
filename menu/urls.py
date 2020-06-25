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
from . import views

app_name = 'menu'

urlpatterns = [
    path('menu/', views.menu_list_view, name='menu_list'),
    path('menu/criar/', views.menu_create_view, name='menu_criar'),
    path('menu/criarprato/', views.prato_create_view, name='prato_criar'),
    path('menu/<int:id>/details/', views.menu_detail_view, name='menu_detail'),
    path('menu/update/<int:id>', views.menu_update_view, name='menu_update'),
    path('menu/updateprato/<int:id>', views.prato_update_view, name='prato_update'),
    path('menu/apagar/<int:id>', views.menu_delete_view, name='menu_delete'),
    path('menu/apagarprato/<int:id>', views.prato_delete_view, name='prato_delete'),
    

    path('transporte/', views.transporte_list_view, name='transporte-list'),
    path('transporte/criar/', views.transporte_create_view, name='transporte-criar'),
    path('transporte/criarhora/', views.transportehora_create_view, name='transportehora-criar'),
    path('horario/', views.horario_create_view, name='horario-list'),
    path('transporte/details/<int:id>', views.transporte_detail_view, name='transporte-detail'),
    path('transporte/update/<int:id>', views.transporte_update_view, name='transporte-update'),
    path('update2/<int:id>', views.transporte_update2_view, name='transporte-update2'),
    path('transporte/apagar/<int:id>', views.transporte_delete_view, name='transporte-delete'),
    path('transporte/grupos/<int:id>', views.transporte_grupo_view, name='transporte-grupo'),
    path('transporte/criarhorarario/', views.horariotransporte_create_view, name='transporte-horario'),
    
    path('', views.index, name='index'),
    path('diaaberto/', views.diaaberto_list, name='diaaberto_list'),
    path('criar/', views.diaaberto_create, name='diaaberto_create'),
    path('diaaberto/update/<int:id>', views.diaaberto_update, name='diaaberto_update'),
    path('diaaberto/apagar/<int:id>', views.diaaberto_delete, name='diaaberto_delete'),
    path('diaaberto/<int:id>/details/', views.diaaberto_details, name='diaaberto_details'),
]

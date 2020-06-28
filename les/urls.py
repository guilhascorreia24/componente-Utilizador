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
from django.contrib import admin
from django.urls import path,include
from user import views as user_views
from Notification import views as notificacao_views
from tarefas import urls
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',notificacao_views.createnot,name="create_not"),
    path('notificacao/',notificacao_views.checknot,name="check_not"),
    path('notificacao/<str:id>/',notificacao_views.noti,name="noti"),
    path('notificacao/enviadas',notificacao_views.enviados,name="check_not_enviadas"),
    path('register/', user_views.register, name='register'),
    path('login/',user_views.login_request,name='login'),
    path('logout/',user_views.logout_request,name='logout'),
    path('login/recuperacao_password/',user_views.reset,name="recuperacao_password"),
    path('login/recuperacao_password/<str:id>/',user_views.change_password,name="reset"),
    path('inscricao/',include('inscricao.urls', namespace='inscricao'), name='inscricao'),
    path('profile/<int:id>',user_views.profile,name="profile"),
    path('profiles_list/',user_views.profile_list,name='profile_list'),
   # path("profiles_list/<int:id>/",user_views.profile,name="profile_user"),
    path("profile_edit/<int:id>",user_views.modify_user,name="profile_edit"),
    path("profiles_list/delete/<int:id>/",user_views.delete_user,name="delete"),
    path('validacoes/<int:acao>/<int:id>',user_views.validacoes,name="validacoes"),
    path('tarefas/',include('tarefas.urls')),
    #path('config_campus/',include('Campus.url',namespace="campus")),
    path('', include("blog.urls")),
    path("formularios/",include("formularios.urls")),
    path("user_type",user_views.getUserType,name="user_type"),
    path('atividades/', include('atividades.urls')),
    path('menu/',include('menu.urls')),
    path('tarefa_coordenador/', include('main.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

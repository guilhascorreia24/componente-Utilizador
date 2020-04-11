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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/',user_views.login_request,name='login'),
    path('logout/',user_views.logout_request,name='logout'),
    path('login/recuperacao_password/',user_views.reset,name="recuperacao_password"),
    path('login/recuperacao_password/<str:id>/',user_views.change_password,name="reset"),
    path('atividades/',include('atividades.urls')),
    path('profile/<str:id>',user_views.profile,name="profile"),
    path('profiles_list/',user_views.profile_list,name='profile_list'),
    path("profiles_list/<str:id>/",user_views.profile,name="profile_user"),
    path("profile_edit/<str:id>",user_views.modify_user,name="edit_user"),
    path("profiles_list/delete/<str:id>/",user_views.delete_user,name="delete"),
    path("notificacao/",notificacao_views.checknot,name="not-search"),
    path('validacoes/<str:id>',user_views.validacoes,name="validacoes"),
    path('', include("blog.urls"))
]

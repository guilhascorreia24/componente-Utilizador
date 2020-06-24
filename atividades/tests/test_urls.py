from django.test import TestCase, SimpleTestCase
from atividades.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_criar_atividade(self):
        url = reverse('atividades:criar_atividade')
        self.assertEquals(resolve(url).func, atividade_create_view)
    
    def test_consultar_minhas_atividades(self):
        url = reverse('atividades:consultar_minhas_atividades')
        self.assertEquals(resolve(url).func, my_activities_view)
    
    def test_consultar_atividades(self):
        url = reverse('atividades:consultar_atividades')
        self.assertEquals(resolve(url).func, all_activities_view)
    
    def test_aceitar_atividade(self):
        url = reverse('atividades:aceitar_atividade',args=[52])
        self.assertEquals(resolve(url).func, validar_atividade_view)
    
    def test_apagar_atividade(self):
        url = reverse('atividades:apagar_atividade',args=[52])
        self.assertEquals(resolve(url).func, deletar_atividade_view)
    
    def test_editar_atividade(self):
        url = reverse('atividades:editar_atividade',args=[52])
        self.assertEquals(resolve(url).func, editar_atividade_view)
    
    def test_consultar_atividades_coodernador(self):
        url = reverse('atividades:consultar_atividades_coodernador')
        self.assertEquals(resolve(url).func, coordinator_activities_view)
    
    def test_ver_sessoes(self):
        url = reverse('atividades:ver_sessoes',args=[52])
        self.assertEquals(resolve(url).func, activity_session_view)

    def test_criar_editar_sessao(self):
        url = reverse('atividades:criar_editar_sessao',args=[52])
        self.assertEquals(resolve(url).func, create_edit_session_view)

    def test_apagar_sessao(self):
        url = reverse('atividades:apagar_sessao',args=[52])
        self.assertEquals(resolve(url).func, delete_session)

    def test_criar_sala(self):
        url = reverse('atividades:criar_sala')
        self.assertEquals(resolve(url).func, criar_sala_view)

    def test_editar_local(self):
        url = reverse('atividades:editar_local',args=[52])
        self.assertEquals(resolve(url).func, editar_local_view)

    def test_apagar_local(self):
        url = reverse('atividades:apagar_local',args=[52])
        self.assertEquals(resolve(url).func, deletar_espaco_view)
    
    def test_display_image(self):
        url = reverse('atividades:display_image',args=[52])
        self.assertEquals(resolve(url).func, show_image)

    def test_criar_campus(self):
        url = reverse('atividades:criar_campus')
        self.assertEquals(resolve(url).func, criar_campus_view)

    def test_apagar_campus(self):
        url = reverse('atividades:apagar_campus',args=[52])
        self.assertEquals(resolve(url).func, apagar_campus_view)

    def test_criar_uo(self):
        url = reverse('atividades:criar_uo')
        self.assertEquals(resolve(url).func, criar_uo_view)

    def test_apagar_uo(self):
        url = reverse('atividades:apagar_uo',args=[52])
        self.assertEquals(resolve(url).func, apagar_uo_view)

    def test_criar_departamento(self):
        url = reverse('atividades:criar_departamento')
        self.assertEquals(resolve(url).func, criar_departamento_view)

    def test_apagar_departamento(self):
        url = reverse('atividades:apagar_departamento',args=[52])
        self.assertEquals(resolve(url).func, apagar_departamento_view)

    def test_logout(self):
        url = reverse('atividades:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_login(self):
        url = reverse('atividades:login')
        self.assertEquals(resolve(url).func, login_view)
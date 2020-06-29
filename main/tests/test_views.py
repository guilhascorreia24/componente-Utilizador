import unittest
from main.models import *
from django.test import SimpleTestCase, Client
from django.urls import reverse

class TestViews(SimpleTestCase):
    
    def setUp(self):
        self.client=Client()
        self.criar_url=reverse('tarefa_coordenador:criar_tarefa')

    def test_criar_tarefa_GET(self):
        response = self.client.get(self.criar_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'main/criarTarefa.html')
    
class Testviews2(unittest.TestCase):
    
    def setUp(self):
        self.client=Client()
        self.consultar_admin_url=reverse('tarefa_coordenador:consultar_tarefa_admin')
        self.editar_url=reverse('tarefa_coordenador:editar_tarefa', args=[23])
        self.sessao_url=reverse('tarefa_coordenador:ajax_load_cities')
        self.espaco_url=reverse('tarefa_coordenador:ajax_load_espaco')
        self.grupo_url=reverse('tarefa_coordenador:ajax_load_grupo')

    def test_consultar_admin_GET(self):
        response = self.client.get(self.consultar_admin_url)
        self.assertEquals(response.status_code,200)

    def test_editar_GET(self):
        response = self.client.get(self.editar_url)
        self.assertEquals(response.status_code,200)

    def test_ajax_sessao_GET(self):
        response = self.client.get(self.sessao_url)
        self.assertEquals(response.status_code,200)

    def test_ajax_espaco_GET(self):
        response = self.client.get(self.espaco_url)
        self.assertEquals(response.status_code,200)

    def test_ajax_grupo_GET(self):
        response = self.client.get(self.grupo_url)
        self.assertEquals(response.status_code,200)
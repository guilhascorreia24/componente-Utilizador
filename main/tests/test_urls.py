from django.test import TestCase, SimpleTestCase
from main.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_ciar_tarefa(self):
        url = reverse('tarefa_coordenador:criar_tarefa')
        self.assertEquals(resolve(url).func, criar_tarefa)

    def test_criar_tarefa_atividade(self):
        url = reverse('tarefa_coordenador:criar_tarefa_atividade')
        self.assertEquals(resolve(url).func, criar_tarefa_atividade)

    def test_criar_tarefa_grupo(self):
        url = reverse('tarefa_coordenador:criar_tarefa_grupo')
        self.assertEquals(resolve(url).func, criar_tarefa_grupo)

    def test_consultar_tarefa(self):
        url = reverse('tarefa_coordenador:consultar_tarefa')
        self.assertEquals(resolve(url).func, consultar_tarefa)
    
    def test_consultar_tarefa_admin(self):
        url = reverse('tarefa_coordenador:consultar_tarefa_admin')
        self.assertEquals(resolve(url).func, consultar_tarefa_admin)
    
    def test_eliminar_tarefa(self):
        url = reverse('tarefa_coordenador:eliminar_tarefa', args=[23])
        self.assertEquals(resolve(url).func, eliminar_tarefa)

    def test_editar_tarefa(self):
        url = reverse('tarefa_coordenador:editar_tarefa', args=[23])
        self.assertEquals(resolve(url).func, editar_tarefa)

    def test_ajax_load_cities(self):
        url = reverse('tarefa_coordenador:ajax_load_cities')
        self.assertEquals(resolve(url).func, load_cities)

    def test_ajax_load_espaco(self):
        url = reverse('tarefa_coordenador:ajax_load_espaco')
        self.assertEquals(resolve(url).func, load_espaco)
    
    def test_ajax_load_grupo(self):
        url = reverse('tarefa_coordenador:ajax_load_grupo')
        self.assertEquals(resolve(url).func, load_grupo)
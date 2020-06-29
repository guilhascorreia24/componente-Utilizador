from django.test import TestCase, SimpleTestCase
from tarefas.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_disponibilidade(self):
        url = reverse('tarefas:disponibilidade')
        self.assertEquals(resolve(url).func, consultar_tarefas)
    
    def test_tarefas(self):
        url = reverse('tarefas:tarefas')
        self.assertEquals(resolve(url).func, consultar_tarefas2)
    
    def test_estado(self):
        url = reverse('tarefas:mudar_estado')
        self.assertEquals(resolve(url).func, mudar_estado)
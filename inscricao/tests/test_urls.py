from django.test import TestCase, SimpleTestCase
from inscricao.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_consultar_inscricao(self):
        url = reverse('inscricao:consulta')
        self.assertEquals(resolve(url).func, consultar_inscricao)
    
    def test_register(self):
        url = reverse('inscricao:register')
        self.assertEquals(resolve(url).func, inscricao_form)
    
    def test_register_individual(self):
        url = reverse('inscricao:register_individual')
        self.assertEquals(resolve(url).func, inscricao_individual_form)
    
    def test_inscricao_delete(self):
        url = reverse('inscricao:delete',args=[52])
        self.assertEquals(resolve(url).func, inscricao_delete)
    
    def test_inscricao_alterar(self):
        url = reverse('inscricao:alterar',args=[52])
        self.assertEquals(resolve(url).func, inscricao_alterar)
import unittest
from user.models import *
from django.test import Client,SimpleTestCase,TransactionTestCase 
from django.urls import reverse
from blog.views import encrypt

class Testviews(unittest.TestCase):
    def setUp(self):
        self.client=Client()
        self.consultar_tarefas=reverse('consultar_tarefas')
        self.consultar_tarefas2=reverse('consultar_tarefas2')

    def test_consultar_tarefas_GET(self):
        response = self.client.get(self.consultar_tarefas)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'tarefas/consultar_tarefas.html')

    def test_consultar_tarefas2_GET(self):
        response = self.client.get(self.consultar_tarefas2)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'tarefas/consultar_tarefas2.html')

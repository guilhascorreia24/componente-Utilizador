from django.test import TestCase, Client 
from django.urls import reverse
import json

class TestViews(TestCase):
    
    def test_GET(self):
        client = Client()
        response = client.get(reverse('criar_tarefa'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/criarTarefa.htmls')

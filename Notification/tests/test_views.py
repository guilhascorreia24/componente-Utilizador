import unittest
from Notification.models import *
from django.test import Client
from django.urls import reverse

class TestViews(unittest.TestCase):
    
    def setUp(self):
        self.client=Client()

        self.create_url=reverse("create_not")

    def test_create(self):
        response=self.client.post(self.create_url,{
        'Descricao':'Ola boa tarde',
        'Assunto':'Teste',
        'Destinatario':'teste_teste@gmail.com',
        })
        self.assertEquals(response.status_code,200)


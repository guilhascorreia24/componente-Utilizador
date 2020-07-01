import unittest
from main.models import *
from django.test import SimpleTestCase, Client
from django.urls import reverse

class Testviews2(unittest.TestCase):
    
    def setUp(self):
        self.client=Client()
        self.diaaberto_list_url=reverse('menu:diaaberto_list')
        #self.diaaberto_create_url=reverse('menu:diaaberto_create',args=[1002])


        self.menu_list_url=reverse('menu:menu_list')
        self.menu_create_url=reverse('menu:menu_criar')
        self.prato_create_url=reverse('menu:prato_criar')


        self.transporte_list_url=reverse('menu:transporte-list')
        self.transporte_create_url=reverse('menu:transporte-criar')
        self.transportehora_create_url=reverse('menu:transportehora-criar')
        self.horario_create_url=reverse('menu:horario-list')

#Dia Aberto
    def test_diaaberto_list_GET(self):
        response = self.client.get(self.diaaberto_list_url)
        self.assertEquals(response.status_code,200)
    
    #def test_diaaberto_create_GET(self):
    #    u=Utilizador.objects.create(nome="Admin1",email="admin1@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=4)
    #    a=Administrador.objects.create(pk=u.pk)
    #    response = self.client.get(self.diaaberto_create_url,args=[u.pk])
    #    self.assertEquals(response.status_code,200)

#Menu
    def test_menu_list_GET(self):
        response = self.client.get(self.menu_list_url)
        self.assertEquals(response.status_code,200)

    def test_menu_create_GET(self):
        response = self.client.get(self.menu_create_url)
        self.assertEquals(response.status_code,200)

    def test_prato_create_GET(self):
        response = self.client.get(self.prato_create_url)
        self.assertEquals(response.status_code,200)

#Transporte
    def test_transporte_list_GET(self):
        response = self.client.get(self.transporte_list_url)
        self.assertEquals(response.status_code,200)
    
    def test_transporte_create_GET(self):
        response = self.client.get(self.transporte_create_url)
        self.assertEquals(response.status_code,200)
    
    def test_transportehora_create_GET(self):
        response = self.client.get(self.transportehora_create_url)
        self.assertEquals(response.status_code,200)

    def test_horario_create_GET(self):
        response = self.client.get(self.horario_create_url)
        self.assertEquals(response.status_code,200)

    


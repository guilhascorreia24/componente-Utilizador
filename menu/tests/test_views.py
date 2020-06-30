import unittest
from main.models import *
from django.test import SimpleTestCase, Client
from django.urls import reverse

class Testviews2(unittest.TestCase):
    
    def setUp(self):
        self.client=Client()
        self.diaaberto_list_url=reverse('menu:diaaberto_list')
        self.menu_list_url=reverse('menu:menu_list')
        self.transporte_list_url=reverse('menu:transporte-list')

    def test_diaaberto_list_GET(self):
        response = self.client.get(self.diaaberto_list_url)
        self.assertEquals(response.status_code,200)

    def test_menu_list_GET(self):
        response = self.client.get(self.menu_list_url)
        self.assertEquals(response.status_code,200)

    def test_transporte_list_GET(self):
        response = self.client.get(self.transporte_list_url)
        self.assertEquals(response.status_code,200)


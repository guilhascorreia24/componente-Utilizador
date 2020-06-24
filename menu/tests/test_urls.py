from django.test import TestCase, SimpleTestCase
from menu.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_disponibilidade(self):
        url = reverse('menu_list')
        self.assertEquals(resolve(url).func, menu_list_view)
    
    def test_menu_create(self):
        url = reverse('menu_criar')
        self.assertEquals(resolve(url).func, menu_create_view)
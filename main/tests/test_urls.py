from django.test import TestCase, SimpleTestCase
from main.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_criar_tarefa(self):
        url = reverse('homepage')
        self.assertEquals(resolve(url).func, homepage)


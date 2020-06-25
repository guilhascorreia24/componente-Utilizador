from django.test import TestCase, SimpleTestCase
from formularios.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_cursos(self):
        url = reverse('formularios:cursos')
        self.assertEquals(resolve(url).func, curso_form)
    
    def test_delete_cursos(self):
        url = reverse('formularios:delete_curso',args=[52])
        self.assertEquals(resolve(url).func, delete_curso)
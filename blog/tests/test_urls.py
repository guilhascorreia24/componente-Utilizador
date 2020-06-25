from django.test import TestCase, SimpleTestCase
from blog.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_cursos(self):
        url = reverse('blog:blog-home')
        self.assertEquals(resolve(url).func, home)
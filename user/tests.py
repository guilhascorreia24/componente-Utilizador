from django.test import TestCase, Client
from django.urls import reverse
from .models import *
import json

# Create your tests here.
class TestUser(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('blog:blog-home')
        Utilizador.objects.create(pk=1000,	nome=	'admin', email=	'admin@admin.com', telefone=	988323330	,password='7bd0854665d161be3d4504443e438c409ea9db07156fdbc3d5d143bc72ff4c39', validada=4,	remember_me="Z0FBQUFBQmU3N29ZM202R21vVHRFcUh6T2t4SEl0U29KODhjOEQ2VVJjV0RtRW1MeXNUelBXOVpyYVEwSmt1QlB6MzNFbWhMeEx4c3o0US03ck9KamhtakpGT0xrN2JsaHc9PQ=="	)

    def test_project_register_GET(self):
        response=client.get(reverse('blog-home'))

        self.asssertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
    
    def test_project_login_GET(self):
        response =self.client.get(self.detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')




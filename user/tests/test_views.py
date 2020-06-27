import unittest
from user.models import *
from django.test import Client
from django.urls import reverse
from blog.views import encrypt

class Testviews(unittest.TestCase):
    def setUp(self):
        self.client=Client()
        self.register_url=reverse("register")
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')
        self.recuperacao_password_url=reverse('recuperacao_password')
        self.reset_url=reverse('reset',args=[encrypt(self.usr.pk)])
        self.profile_list_url=reverse('profile_list')
        '''self.profile_edit_url=reverse('profile_edit',args=[self.usr.pk])
        self.validacao_url=reverse('validacoes',args=[1,self.usr.pk])''' 

    
    def test_register(self):
        self.usr=Utilizador.objects.create(nome="Sabino",email="sabino1@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        response=self.client.post(self.register_url,{
            'name':'Sabino',
            'email':'sabino@hotmail.com',
            'telefone':'123456789',
            'password1':'Admin1',
            'password2':'Admin1',
            'funcao':0
        })
        self.assertEquals(response.status_code,200)
        self.usr.delete()

    '''def test_login(self):
        response=self.client.post(self.login_url,{
            'email':'sabino@hotmail.com',
            'password':'Admin1'
        })
        self.assertEquals(response.status_code,200)
    
    def test_logout(self):
        response=self.client.get(self.logout_url)
        self.assertEquals(response.statuc_code,200)

    def test_reset(self):
        response=self.client.post(self.recuperacao_passowrd_url,{
            'email':'sabino@hotmail.com'
        })
        self.assertEquals(response.status_code,200)
    
    def test_change_password(self):
        response=self.client.post(self.reset_url,{
            'password':'Admin2',
            'confirm_password': 'Admin2'
        })
        self.assertEquals(response.status_code,200)
    
    def done(self):
        self.usr.delete()'''
    
    

        
    
import unittest
from user.models import *
from django.test import Client,SimpleTestCase,TransactionTestCase 
from django.urls import reverse
from blog.views import encrypt

class Testviews(unittest.TestCase):
    def setUp(self):
        self.client=Client()
        self.login_url=reverse('login')
        self.logout_url=reverse('logout')
        self.recuperacao_password_url=reverse('recuperacao_password')
        self.profile_list_url=reverse('profile_list')
        #self.profile_edit_url=reverse('profile_edit',args=[self.usr.pk])


    
    def test_register(self):
        response=self.client.post(reverse("register"),{
            'name':'Sabino',
            'email':'sabino@hotmail.com',
            'telefone':'123456789',
            'password1':'Admin1',
            'password2':'Admin1',
            'funcao':0 
        })
        self.assertEquals(response.status_code,302)
        Utilizador.objects.filter(email='sabino@hotmail.com').delete()

    def test_login(self):
        Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        response=self.client.post(self.login_url,{
            'email':'sabino@hotmail.com',
            'password':'Admin1',
            'tentatives':5,
        })
        self.assertEquals(response.status_code,302)
        response=self.client.post(self.login_url,{
            'email':'sabino@hotmail.com',
            'password':'Admi1',
            'tentatives':5,
        })
        self.assertEquals(response.status_code,200)
        Utilizador.objects.filter(email='sabino@hotmail.com').delete()

    def test_reset(self):
        #Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        response=self.client.post(self.recuperacao_password_url,{
            'email':'sabino@hotmail.com'
        })
        self.assertEquals(response.status_code,200)
        Utilizador.objects.filter(email="sabino@hotmail.com").delete()
        response=self.client.post(self.recuperacao_password_url,{
            'email':'sabino@hotmail.com'
        })
        self.assertEquals(response.status_code,200)
    
    def test_change_password(self):
        Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        response=self.client.post(reverse('reset',args=[encrypt(Utilizador.objects.get(email="sabino@hotmail.com").pk)]),{
            'password':'Admin2',
            'confirm_password': 'Admin2'
        })
        self.assertEquals(response.status_code,302)
        response=self.client.post(reverse('reset',args=[encrypt(Utilizador.objects.get(email="sabino@hotmail.com").pk)]),{
            'password':'admin2',
            'confirm_password': 'admin2'
        })
        self.assertEquals(response.status_code,200)
        Utilizador.objects.filter(email="sabino@hotmail.com").delete()
    
    def test_profile_list(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=4)
        #u=Utilizador.objects.get(email="sabino@hotmail.com")
        Administrador.objects.create(pk=u.pk)
        session =self.client.session
        session['user_id']=u.pk

        session.save()
        response=self.client.get(self.profile_list_url)
        self.assertEquals(response.status_code,200)
        #Utilizador.objects.filter(email="sabino@hotmail.com").delete()
        Administrador.objects.filter(pk=session['user_id']).delete()
        
        campus=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="PP",campus_idcampus=campus)
        coord=Coordenador.objects.create(pk=u.pk,unidade_organica_iduo=uo)
        response=self.client.get(self.profile_list_url)
        self.assertEquals(response.status_code,200)
        u.delete()
        assert 'list_users.html' in (t.name for t in response.templates)

        
        campus.delete()
        uo.delete()
        coord.delete()

    def test_validacoes(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=4)
        a=Administrador.objects.create(pk=u.pk)
        session =self.client.session
        session['user_id']=u.pk
        session.save()
        validacao_url=reverse('validacoes',args=[1,u.pk])
        response=self.client.get(validacao_url)
        self.assertEquals(response.status_code,302)
        
        Utilizador.objects.filter(pk=u.pk).update(validada=1)
        validacao_url=reverse('validacoes',args=[1,u.pk])
        response=self.client.get(validacao_url)
        self.assertEquals(response.status_code,302)
        u.delete()

    def test_user_delete(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=4)
        a=Administrador.objects.create(pk=u.pk)

        delete_url=reverse('delete',args=[u.pk])
        response=self.client.get(delete_url)
        self.assertEquals(response.status_code,302)

    def test_profile_edit(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=4)
        a=Administrador.objects.create(pk=u.pk)
        session =self.client.session
        session['user_id']=u.pk
        session.save()
        modify_url=reverse('profile_edit',args=[u.pk])
        response=self.client.get(modify_url)
        self.assertEquals(response.status_code,200)
        assert 'profile_modify.html' in (t.name for t in response.templates)
        u1=Utilizador.objects.create(nome="Sabino",email="sabino2@hotmail.com",telefone="123465789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=2)
        modify_url=reverse('profile_edit',args=[u.pk])
        response=self.client.get(modify_url)
        self.assertEquals(response.status_code,200)
        assert 'profile_modify.html' in (t.name for t in response.templates)
        u.delete()
        u1.delete()
    
    def test_profile_own(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        session =self.client.session
        session['user_id']=u.pk
        session.save()
        profile_url=reverse('profile_edit',args=[u.pk])
        response=self.client.get(profile_url)
        self.assertEquals(response.status_code,200)
        assert 'profile_modify.html' in (t.name for t in response.templates)
        u.delete()



    
    

        
    
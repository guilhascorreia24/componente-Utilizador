from django.test import TestCase, SimpleTestCase
from user.views import *
from django.urls import reverse,resolve

class TestUrls(SimpleTestCase):

    def test_user_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_user_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_request)

    def test_user_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_request)
    
    def test_recuperação_password(self):
        url = reverse('recuperacao_password')
        self.assertEquals(resolve(url).func, reset)
    
    def test_recuperação_password_id(self):
        url = reverse('reset',args=[52])
        self.assertEquals(resolve(url).func, change_password)
    
    def test_user_profile(self):
        url = reverse('profile',args=[52])
        self.assertEquals(resolve(url).func, profile)

    def test_profile_list(self):
        url = reverse('profile_list')
        self.assertEquals(resolve(url).func, profile_list)

    def test_profile_edit(self):
        url = reverse('profile_edit',args=[52])
        self.assertEquals(resolve(url).func, modify_user)

    def test_delete_user(self):
        url = reverse('delete',args=[52])
        self.assertEquals(resolve(url).func, delete_user)
    
    def test_validacoes(self):
        url = reverse('validacoes',args=[1,52])
        self.assertEquals(resolve(url).func, validacoes)

    def test_user_type(self):
        url = reverse('user_type')
        self.assertEquals(resolve(url).func, getUserType)
from django.test import SimpleTestCase
from user.forms import *

class TestForms(SimpleTestCase):

    def test_User_RegisterForm_filled(self):
        form = UserRegisterForm(data={
            'name': 'Guilherme',
            'email': 'Teste@gmail.com',
            'telefone': '969123456',
            'password1':'12345Abcd',
            'password2': '12345Abcd',
            'funcao': '2',
            'curso':'1',
            'Preferencias': 'Palestras de manhã',
            'UO': '4',
            'departamento': '2',
        })

        self.assertTrue(form.is_valid())
    
    def test_User_RegisterForm_Empty(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),7)
    
    
    def test_User_AutenticationForm_filled(self):
        form = AuthenticationForm(data={
            'email': 'Teste@gmail.com',
            'password':'12345Abcd',
        })

        self.assertTrue(form.is_valid())
    
    def test_AutenticationFor_Empty(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),7)

    def test_ModifyForm_filled(self):
        form = ModifyForm(data={
            'name': 'Guilherme',
            'email': 'Teste@gmail.com',
            'telefone': '969123456',
            'funcao': 'Coordenador',
            'UO': 'FCT',
            'dep':'DEI',
            'curso':'LEI',
            'ano': '2020',
            'preferencia': 'Palestras de tarde',
        })

        self.assertTrue(form.is_valid())
    
    def test_ModifyForm_Empty(self):
        form = ModifyForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),9)

    
    def test_PasswordChangeForm_filled(self):
        form = PasswordChangeForm(data={
            'password': 'NovaPass123',
            'confirm_password': 'NovaPass123',
        })

        self.assertTrue(form.is_valid())

    def test_PasswordChangeForm_Empty(self):
        form = PasswordChangeForm(data={})

        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors),0)
    
    def test_EmailSenderForm_filled(self):
        form = EmailSender(data={
            'email': 'teste@gmail.com',
        })

        self.assertTrue(form.is_valid())

    def test_EmailSenderForm_empty(self):
        form = EmailSender(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_DeleteUserForm_filled(self):
        form = DeleteUser(data={
            'iduser': 52,
        })

        self.assertTrue(form.is_valid())
    
    def test_DeleteUserForm_empty(self):
        form = DeleteUser(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
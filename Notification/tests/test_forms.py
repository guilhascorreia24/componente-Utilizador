from django.test import SimpleTestCase
from Notification.forms import *

'''class TestForms(SimpleTestCase):

    def test_NotificationForm_filled(self):
        form = NotificationForm(data={
            'Destinatario': 'Guilherme',
            'Assunto': 'Teste',
            'Descricao': 'Django test',

        })

        self.assertTrue(form.is_valid())
    
    def test_NotificationForm_Empty(self):
        form = NotificationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)'''
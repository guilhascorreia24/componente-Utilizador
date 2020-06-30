import unittest
from Notification.models import *
from django.test import Client
from django.urls import reverse

class TestViews(unittest.TestCase):
    
    def setUp(self):
        self.client=Client()
        self.create_url=reverse('create_not')
        self.check_url=reverse('check_not')
        self.noti_url=reverse('noti',args=[52])
        self.check_not_enviadas_url=reverse('check_not_enviadas')

    def test_create(self):
        u = Utilizador.objects.create(idutilizador='1112277',nome='ze',email='hello123@gmail.com',telefone='915401216',password='0cfb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc',validada=0)
        session =self.client.session
        session['user_id']=u.pk
        session.save()
        response=self.client.post(reverse("create_not"),{
            'Destinatario':u,
            'Assunto':'teste',
            'Descricao':'Ola bom dia',
        })
        self.assertEquals(response.status_code,200)
        u.delete()

    '''def test_check(self):
        n = Notificacao.objects.create(descricao='Ola boa tarde', criadoem='2019-06-29 11:28:18.131219', idutilizadorenvia='32',utilizadorrecebe='20',assunto='Teste')
        session =self.client.session
        session['user_id']=n.pk
        #session.save()
        response=self.client.post(reverse("check_not"),{
            'idutilizadorenvia':n,
        })
        self.assertEquals(response.status_code,200)
        n.delete()'''
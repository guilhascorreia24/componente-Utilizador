from django.test import TestCase, SimpleTestCase
from Notification.models import Notificacao
from Notification.views import createnot,checknot,noti,enviados
from django.urls import reverse,resolve


class TestUrls(SimpleTestCase):

    def test_create_not_url(self):
        url = reverse('create_not')
        self.assertEquals(resolve(url).func, createnot)

    def test_check_not_url(self):
        url = reverse('check_not')
        self.assertEquals(resolve(url).func, checknot)

    '''def test_noti_url(self):
        url = reverse('noti')
        self.assertEquals(resolve(url).func.view_class, noti)'''
    
    def test_check_not_enviadas(self):
        url = reverse('check_not_enviadas')
        self.assertEquals(resolve(url).func, enviados)
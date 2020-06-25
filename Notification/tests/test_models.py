from django.test import TestCase
from Notification.models import Notificacao

'''class NotificacaoTestCase(TestCase):
    
    def setUp1(self):
        return Notificacao.objects.get_or_create(Notificacao.objects.create(descricao="hello django", criadoem="2020-06-19 22:05:48.547718",idutilizadorenvia="54",utilizadorrecebe="55",assunto="teste1"))[0] 

    def setUp2(self):
        Notificacao.objects.create(descricao="django hello", criadoem="2019-05-23 21:03:22.537718",idutilizadorenvia="10",utilizadorrecebe="11",assunto="teste2")[0]
        return Notificacao.objects.get_or_create(Notificacao.objects.create(descricao="django hello", criadoem="2019-05-23 21:03:22.537718",idutilizadorenvia="10",utilizadorrecebe="11",assunto="teste2"))[0]
    
    def test(self):
       Nots=[setUp1(),setUp2(),]
       self.assertEquals(str(Nots[0]),"django hello")'''
import unittest
from Notification.models import *

class NotificacaoTestCase(unittest.TestCase):
    
    '''def test_Notificacao(self):
        n = Notificacao.objects.create(descricao='Ola boa tarde', criadoem='2019-06-29 11:28:18.131219', idutilizadorenvia='32',utilizadorrecebe='20',assunto='Teste')
        self.assertEquals(Notificacao.objects.filter(pk=n.pk).exists(),True)
        n.delete()
    
    def test_Utilizador_Has_Notificacao(self):
        u = Utilizador.objects.create(idutilizador='1032',nome='ze',email='miguel@gmail.com',telefone='964876216',password='0cfb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc',validada=0)
        n = Notificacao.objects.create(descricao='Ola boa tarde', criadoem='2019-06-29 11:28:18.131219', idutilizadorenvia='32',utilizadorrecebe='20',assunto='Teste')
        uai = UtilizadorHasNotificacao.objects.create(utilizador_idutilizador=u,notificacao_id=int(n.pk),estado=1)
        self.assertEquals(Notificacao.objects.filter(pk=uai.pk).exists(),True)
        n.delete()
        u.delete()
        uai.delete()'''

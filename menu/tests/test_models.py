import unittest
from menu.models import *

class TestModels(unittest.TestCase):

    def test_diaaberto(self):
        u = Utilizador.objects.create(nome='Admin1', email='admin1@admin.com', telefone='978989829', password='0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc', validada=4)
        a = Administrador.objects.create(pk=u.pk)
        d = DiaAberto.objects.create(ano=2022, descricao='Dia Aberto 2022!!!!!!!!!!', emaildiaaberto='dia@aberto.com', enderecopaginaweb='http://www.diaaberto.com', datadiaabertoinicio='2021-07-20', datadiaabertofim='2021-07-24', datainscricaonasatividadesinicio='2021-06-25', datainscricaonasatividadesfim='2021-06-30', datapropostaatividadeinicio='2021-06-25', datapropostaatividadesfim='2020-06-30', administrador_utilizador_idutilizador=a, preco_almoco_estudante = 2.8, preco_almoco_professor = 4.2)
        self.assertEquals(DiaAberto.objects.filter(pk=d.pk).exists(),True)
        d.delete()
        a.delete()
        u.delete()

    def test_almoco(self):
        d = Dia.objects.create(dia='2020-05-30')
        h = Horario.objects.create(hora='12:00:01')
        dh = HorarioHasDia.objects.create(dia_dia=d, horario_hora =h)
        c = Campus.objects.create(nome ='Gambela')
        m = Menu.objects.create(menu='Menu do dia 30', descricao='Sopa:Juliana e Sobremesa:Mousse', campus_idcampus=c, horario_has_dia_id_dia_hora =dh, nralmocosdisponiveis=200)
        self.assertEquals(Menu.objects.filter(pk=m.pk).exists(),True)
        m.delete()
        c.delete()
        dh.delete()
        h.delete()
        d.delete()

    def test_prato(self):
        d = Dia.objects.create(dia='2020-05-30')
        h = Horario.objects.create(hora='12:00:01')
        dh = HorarioHasDia.objects.create(dia_dia=d, horario_hora =h)
        c = Campus.objects.create(nome ='Gambela')
        m = Menu.objects.create(menu='Menu do dia 30', descricao='Sopa:Juliana e Sobremesa:Mousse', campus_idcampus=c, horario_has_dia_id_dia_hora =dh, nralmocosdisponiveis=200)
        p = Prato.objects.create(idprato =10000,tipo='Carne', descricao='Carne de Porco à Alentejana', nralmocos=0, menu_idmenu =m)
        self.assertEquals(Prato.objects.filter(pk=p.pk).exists(),True)
        p.delete()
        m.delete()
        c.delete()
        dh.delete()
        h.delete()
        d.delete()

    def test_transporte(self):
        d = Dia.objects.create(dia='2020-05-30')
        h = Horario.objects.create(hora='09:00:01')
        dh = HorarioHasDia.objects.create(dia_dia=d, horario_hora =h)
        p = Paragem.objects.create(paragem = "Gambelas 1")
        o = Paragem.objects.create(paragem = "Terminal 1")
        t = Transporte.objects.create(capacidade=20,identificacao= "Proximo 20")
        th = TransporteHasHorario.objects.create(transporte_idtransporte=t, origem=o, destino=p, horario_has_dia_id_dia_hora=dh, n_passageiros = 20)
        self.assertEquals(TransporteHasHorario.objects.filter(pk=th.pk).exists(),True)
        th.delete()
        t.delete()
        o.delete()
        p.delete()
        dh.delete()
        h.delete()
        d.delete()
        


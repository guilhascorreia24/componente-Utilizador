from django.test import SimpleTestCase
from menu.forms import *
import unittest

class TestForms(SimpleTestCase):

    def test_transporte_form_valid_data(self):
        form = TransportForm (data={
            'capacidade': 30,
            'identificacao' : 'Proixmo 20',
        })

        self.assertTrue(form.is_valid())

    def test_transporte_form_no_data(self):
        form = TransportForm (data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
#
#
#
#
#    def test_transportehorario_form_valid_data(self):
#        form = TransporteHorarioForm (data={
#            'transporte_idtransporte': '2',
#            'origem':'Terminal' ,
#            'destino':'Gambelas' ,
#            'horario_has_dia_id_dia_hora' :'12',
#            'n_passageiros': '20',
#        })
#        print(form.errors)
#	
#        self.assertTrue(form.is_valid())
#
#    def test_transportehorario_form_no_data(self):
#        form = TransporteHorarioForm (data={})
#
#        self.assertFalse(form.is_valid())
#        self.assertEquals(len(form.errors),3)

class TestForms(unittest.TestCase):

    def test_diaaberto_form_valid_data(self):
        form = DiaAbertoForm (data={
            'ano': '2021',
            'descricao': 'Dia Aberto 2020!!!!!!!!!!',
            'emaildiaaberto' : 'dia@aberto.com',
            'enderecopaginaweb': 'http://www.diaaberto.com',
            'datainscricaonasatividadesinicio':"2020-07-20",
            'datainscricaonasatividadesfim': "2020-07-21",
            'datadiaabertoinicio': "2020-06-25",
            'datadiaabertofim': "2020-07-04",
            'datapropostaatividadeinicio': "2020-06-25",
            'datapropostaatividadesfim': "2020-07-04",
            'administrador_utilizador_idutilizador':'1002',
            'preco_almoco_estudante': '2.8',
            'preco_almoco_professor': '4.2',
        })
        self.assertTrue(form.is_valid())
          

    def test_menu_form_valid_data(self):
        form = MenuModelForm (data={
            'menu': 'Menu do Dia 15',
            'descricao': 'Sopa e Sobremesa',
            'campus_idcampus': '5',
            'horario_has_dia_id_dia_hora': '7',
            'nralmocosdisponiveis': '229',
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_menu_form_no_data(self):
        form = MenuModelForm (data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)

    
    def test_prato_form_valid_data(self):
        form = PratoForm (data={
            'tipo': 'Carne', 
            'descricao': ' Carne de Porco',
            'nralmocos': '0', 
            'menu_idmenu': '14', 
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_prato_form_no_data(self):
        form = PratoForm (data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

    
    def test_hora_form_valid_data(self):
        form = HoraForm (data={
            'hora': '12:09:00', 
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_hora_form_no_data(self):
        form = HoraForm (data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_dia_form_valid_data(self):
        form = DiaForm (data={
            'dia': '2020-06-25', 
        })
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_dia_form_no_data(self):
        form = DiaForm (data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    
    #def test_horario_form_valid_data(self):
    #        form = HorarioForm (data={
    #            'horario_hora': '12:08:00',
    #            'dia_dia': '2020-06-20',
#
    #        })
    #        print(form.errors)
    #        self.assertTrue(form.is_valid())
#
    #def test_dia_form_no_data(self):
    #    form = HorarioForm (data={})
    #    self.assertFalse(form.is_valid())
    #    self.assertEquals(len(form.errors),2)
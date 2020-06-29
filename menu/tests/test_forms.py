from django.test import SimpleTestCase
from menu.forms import *

#class TestForms(SimpleTestCase):
#
#    def test_diaaberto_form_valid_data(self):
#        form = DiaAbertoForm (data={
#            'ano': '2020',
#            'descricao': 'Dia Aberto 2020!!!!!!!!!!',
#            'emaildiaaberto' : 'dia@aberto.com',
#            'enderecopaginaweb': 'http://www.diaaberto.com',
#            'datainscricaonasatividadesinicio':'2020-07-20',
#            'datainscricaonasatividadesfim': '2020-07-21',
#            'datadiaabertoinicio': '2020-06-25',
#            'datadiaabertofim': '2020-07-04',
#            'datapropostaatividadeinicio': '2020-06-25',
#            'datapropostaatividadesfim': '2020-07-04',
#            'administrador_utilizador_idutilizador':'1002',
#            'preco_almoco_estudante': '2.8',
#            'preco_almoco_professor': '4.2',
#        })
#        self.assertTrue(form.is_valid())
        
#
#    def test_diaaberto_form_no_data(self):
#        form = DiaAbertoForm (data={})
#
#        self.assertFalse(form.is_valid())
#        self.assertEquals(len(form.errors),13)

#    def test_transporte_form_valid_data(self):
#        form = TransportForm (data={
#            'capacidade': 30,
#            'identificacao' : 'Proixmo 20',
#        })
#
#        self.assertTrue(form.is_valid())
#
#    def test_transporte_form_no_data(self):
#        form = TransportForm (data={})
#
#        self.assertFalse(form.is_valid())
#        self.assertEquals(len(form.errors),2)
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
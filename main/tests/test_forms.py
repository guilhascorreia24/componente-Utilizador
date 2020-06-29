from django.test import SimpleTestCase
from main.forms import *

class TestForms(SimpleTestCase):

    def test_form_group_valid_data(self):
        form=TarefasFormGroup(data={
            'nome':'teste1',
            'hora_inicio':'23:59:00',
            'colaborador_utilizador_idutilizador': '1006',
            'coordenador_utilizador_idutilizador': '1004',
            'dia_dia':'2020-07-20',
            'concluida': '1',
            'atividade_idatividade':'7',
            'buscar': '7',
            'campus_levar':'6',
            'levar': '8',
            'inscricao_coletiva_inscricao_idinscricao':'7',
        })
        self.assertTrue(form.is_valid())

    def test_form_group_no_valid_data(self):
        form=TarefasFormGroup(data={})
        self.assertFalse(form.is_valid())

    def test_form_atividade_valid_data(self):
        form=TarefasFormAtividade(data={
            'idtarefa': '2',
            'nome':'teste1',
            'colaborador_utilizador_idutilizador': '1006',
            'coordenador_utilizador_idutilizador': '1007',
            'concluida': '1',
            'atividade_idatividade' : '6',
            'sessao_idesessao': '5',
        })
        self.assertTrue(form.is_valid())

    def test_form_atividade_no_valid_data(self):
        form=TarefasFormAtividade(data={})
        self.assertFalse(form.is_valid())
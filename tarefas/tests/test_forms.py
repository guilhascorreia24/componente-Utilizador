from django.test import SimpleTestCase
from tarefas.forms import *
 
class FormsTest(SimpleTestCase):
 
    def test_Form_Disponibilidade_filled(self):
        form = Form_Disponibilidade(data={
            'dia_dia': '20-05-2020',
            'horario_hora': '12:00:00',
            'horario_hora1': '12:30:00',
            'tipo_de_tarefa':'Tarefa teste',
        })

        self.assertTrue(form.is_valid())

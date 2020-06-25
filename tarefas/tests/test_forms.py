from django.test import SimpleTestCase
from tarefas.forms import *
 
class testForms(SimpleTestCase):
 
    def test_Form_Disponibilidade_filled(self):
        form = Form_Disponibilidade(data={
            'dia_dia': '12-12-2012',
            'horario_hora': '20:20:02',
            'horario_hora1': '21:22:11',
            'tipo_de_tarefa':'Tarefa teste',
        })

        self.assertTrue(form.is_valid())
    
    '''def test_User_RegisterForm_Empty(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),7)'''
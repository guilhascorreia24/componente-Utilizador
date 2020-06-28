import unittest
import random
import string
from blog.models import *


class TestModels(unittest.TestCase):

    def test_Atividade(self):
        c = Campus.objects.create(nome="boliqueime")
        uo = UnidadeOrganica.objects.create(sigla="EE", campus_idcampus=c)
        d = Departamento.objects.create(nome="TT", unidade_organica_iduo=uo)
        letters = string.ascii_lowercase
        stringText = ''.join(random.choice(letters) for i in range(8)) + "@hotmail.com"
        u = Utilizador.objects.create(nome="Sabino", email=stringText, telefone=str(random.randint(111111111,999999999)),
                                      password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",
                                      validada=0)
        e = Espaco.objects.create(nome="sala", campus_idcampus=c)
        p = ProfessorUniversitario.objects.create(pk=u.pk, departamento_iddepartamento=d)
        atv = Atividade.objects.create(titulo="Atividade", capacidade=20, publico_alvo="pessoas", duracao=20,
                                       descricao="algo",
                                       validada=0, professor_universitario_utilizador_idutilizador=p,
                                       unidade_organica_iduo=uo,
                                       departamento_iddepartamento=d, espaco_idespaco=e, tematica="coisa",
                                       nrcolaborador=2)
        self.assertEquals(Atividade.objects.filter(pk=atv.pk).exists(), True)
        Campus.objects.all().delete()
        UnidadeOrganica.objects.all().delete()
        Departamento.objects.all().delete()
        Utilizador.objects.all().delete()
        Espaco.objects.all().delete()
        Atividade.objects.all().delete()

    def test_Sessao(self):
        c = Campus.objects.create(nome="boliqueime")
        uo = UnidadeOrganica.objects.create(sigla="EE", campus_idcampus=c)
        d = Departamento.objects.create(nome="TT", unidade_organica_iduo=uo)
        letters = string.ascii_lowercase
        stringText = ''.join(random.choice(letters) for i in range(8)) + "@hotmail.com"
        u = Utilizador.objects.create(nome="Sabino", email=stringText, telefone=str(random.randint(111111111, 999999999)),
                                      password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",
                                      validada=0)
        e = Espaco.objects.create(nome="sala", campus_idcampus=c)
        p = ProfessorUniversitario.objects.create(pk=u.pk, departamento_iddepartamento=d)
        atv = Atividade.objects.create(titulo="Atividade", capacidade=20, publico_alvo="pessoas", duracao=20,
                                       descricao="algo",
                                       validada=0, professor_universitario_utilizador_idutilizador=p,
                                       unidade_organica_iduo=uo,
                                       departamento_iddepartamento=d, espaco_idespaco=e, tematica="coisa",
                                       nrcolaborador=2)
        h = Horario.objects.create(hora='23:00:00')
        di = Dia.objects.create(dia='2020-01-20')
        horario = HorarioHasDia.objects.create(horario_hora=h, dia_dia=di)
        s = Sessao.objects.create(nrinscritos=0, capacidade=20, atividade_idatividade=atv,
                                  horario_has_dia_id_dia_hora=horario)
        self.assertEquals(Sessao.objects.filter(pk=s.pk).exists(), True)
        Campus.objects.all().delete()
        UnidadeOrganica.objects.all().delete()
        Departamento.objects.all().delete()
        Utilizador.objects.all().delete()
        Espaco.objects.all().delete()
        Atividade.objects.all().delete()
        horario.delete()
        h.delete()
        di.delete()



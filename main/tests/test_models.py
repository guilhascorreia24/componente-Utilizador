import unittest
from main.models import *

class TestModels(unittest.TestCase):

    def test_Colaborador(self):
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        p=Curso.objects.create(nome="UU",unidade_organica_iduo=uo)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        a=Colaborador.objects.create(pk=u.pk,curso_idcurso=p)
        self.assertEquals(Colaborador.objects.filter(pk=u.pk).exists(),True)
        u.delete()
        a.delete()
        c.delete()

    def test_Participante(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        a=Participante.objects.create(pk=u.pk)
        self.assertEquals(Participante.objects.filter(pk=u.pk).exists(),True)
        u.delete()
        a.delete()
    
    def test_Coordenador(self):
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        a=Coordenador.objects.create(pk=u.pk,unidade_organica_iduo=uo)
        self.assertEquals(Coordenador.objects.filter(pk=u.pk).exists(),True)
        u.delete()
        a.delete()
        c.delete()

    def test_Atividade(self):
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        d=Departamento.objects.create(nome="TT",unidade_organica_iduo=uo)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        e=Espaco.objects.create(nome='Sala 1.21', campus_idcampus=c, img='images/frases-bonitas-1000x500.jpg')
        prof=ProfessorUniversitario.objects.create(pk=u.pk,departamento_iddepartamento=d)
        a=Atividade.objects.create(titulo='Brincar Com Números', capacidade=20, publico_alvo="Estudantes", duracao=30, descricao="brincadeirinha", validada=1, professor_universitario_utilizador_idutilizador=prof,
        unidade_organica_iduo=uo, departamento_iddepartamento=d, espaco_idespaco=e, tematica="tema", nrcolaborador=10) 
        c.delete()
        uo.delete()
        d.delete()
        u.delete()
        e.delete()
        prof.delete()
        a.delete()

    def test_Sessao(self):
        h=Horario.objects.create(hora='23:00:00')
        dia=Dia.objects.create(dia='2020-01-20')
        horario=HorarioHasDia.objects.create(horario_hora=h, dia_dia=dia)
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        d=Departamento.objects.create(nome="TT",unidade_organica_iduo=uo)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        e=Espaco.objects.create(nome='Sala 1.21', campus_idcampus=c, img='images/frases-bonitas-1000x500.jpg')
        prof=ProfessorUniversitario.objects.create(pk=u.pk,departamento_iddepartamento=d)
        a=Atividade.objects.create(titulo='Brincar Com Números', capacidade=20, publico_alvo="Estudantes", duracao=30, descricao="brincadeirinha", validada=1, professor_universitario_utilizador_idutilizador=prof,
        unidade_organica_iduo=uo, departamento_iddepartamento=d, espaco_idespaco=e, tematica="tema", nrcolaborador=10)
        s=Sessao.objects.create(nrinscritos=7, capacidade=20,atividade_idatividade=a,horario_has_dia_id_dia_hora=horario)
        horario.delete() 
        h.delete()
        dia.delete()      
        c.delete()
        uo.delete()
        d.delete()
        u.delete()
        e.delete()
        prof.delete()
        a.delete()
        s.delete()

    def test_Tarefa(self):
        h=Horario.objects.create(hora='23:00:00')
        dia=Dia.objects.create(dia='2020-01-20')
        horario=HorarioHasDia.objects.create(horario_hora=h, dia_dia=dia)
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        d=Departamento.objects.create(nome="TT",unidade_organica_iduo=uo)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        e=Espaco.objects.create(nome='Sala 1.21', campus_idcampus=c, img='images/frases-bonitas-1000x500.jpg')
        prof=ProfessorUniversitario.objects.create(pk=u.pk,departamento_iddepartamento=d)
        a=Atividade.objects.create(titulo='Brincar Com Números', capacidade=20, publico_alvo="Estudantes", duracao=30, descricao="brincadeirinha", validada=1, professor_universitario_utilizador_idutilizador=prof,
        unidade_organica_iduo=uo, departamento_iddepartamento=d, espaco_idespaco=e, tematica="tema", nrcolaborador=10)
        s=Sessao.objects.create(nrinscritos=7, capacidade=20,atividade_idatividade=a,horario_has_dia_id_dia_hora=horario)
        horario.delete()
        h.delete()
        dia.delete()
        c.delete()
        uo.delete()
        d.delete()
        u.delete()
        e.delete()
        prof.delete()
        a.delete()
        s.delete()
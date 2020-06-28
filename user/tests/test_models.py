import unittest
from user.models import *
class TestModels(unittest.TestCase):

    def test_utilizadores(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        self.assertEquals(Utilizador.objects.filter(email="sabino@hotmail.com").exists(),True)
        u.delete()
    
    def test_Administrador(self):
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        a=Administrador.objects.create(pk=u.pk)
        self.assertEquals(Administrador.objects.filter(pk=u.pk).exists(),True)
        u.delete()
        a.delete()
    
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
    
    def test_professor(self):
        c=Campus.objects.create(nome="boliqueime")
        uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        d=Departamento.objects.create(nome="TT",unidade_organica_iduo=uo)
        u=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        a=ProfessorUniversitario.objects.create(pk=u.pk,departamento_iddepartamento=d)
        self.assertEquals(ProfessorUniversitario.objects.filter(pk=u.pk).exists(),True)
        u.delete()
        a.delete()
        c.delete()

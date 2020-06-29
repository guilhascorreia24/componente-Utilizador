import unittest
from inscricao.models import *
from django.apps.registry import Apps
from django.db import models
from datetime import datetime
import time
class TestModels(unittest.TestCase):

    @classmethod
    def setUpTestData(cls):
        #Inscricao.objects.create(ano=2020, local='sdfsdfsdf', areacientifica='fghfghfgh', transporte='0')
        self.user=Utilizador.objects.create(nome="Sabino",email="sabino@hotmail.com",telefone="123455789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        self.user1=Utilizador.objects.create(nome="admin",email="adm@hotmail.com",telefone="123435789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        self.user2=Utilizador.objects.create(nome="coord",email="coord@hotmail.com",telefone="123425789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        self.user3=Utilizador.objects.create(nome="prof",email="prof@hotmail.com",telefone="123125789",password="0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc",validada=0)
        
        self.campus=Campus.objects.create(nome="boliqueime")
        self.uo=UnidadeOrganica.objects.create(sigla="EE",campus_idcampus=c)
        self.departamento=Departamento.objects.create(nome="TT",unidade_organica_iduo=uo)
        self.espaco = Espaco.objects.create(nome="Espaço",campus_idcampus=self.campus)

        self.horario=Horario.objects.create(pk=time.localtime())
        self.dia=Dia.objects.create(pk=datetime.date.today())
        self.horarioDia=HorarioHasDia.objects.create(dia_dia=self.dia,horario_hora=self.horario)

        self.part=Participante.objects.create(pk=self.user.pk)
        self.admin=Administrador.objects.create(pk=user1.pk)
        self.coord=Coordenador.objects.create(pk=user2.pk,unidade_organica_iduo=self.uo)
        self.prof=ProfessorUniversitario.objects.create(pk=self.user3.pk,departamento_iddepartamento=self.departamento)

        self.atividade1=Atividade(titulo='atividade1',capacidade=10,publico_alvo="Publico",duracao=30,descricao="Algo",validada=0,professor_universitario_utilizador_idutilizador=self.prof,unidade_organica_iduo=self.uo,departamento_iddepartamento=self.departamento,espaco_idespaco=self.espaco,tematica=" ",nrcolaborador=0)

        self.sessao1=Sessao(nrinscritos=0,capacidade=30,atividade_idatividade=self.atividade1,horario_has_dia_id_dia_hora=self.horarioDia)
    
    def testInscricaoIndividual(self):
        inscricao =  Inscricao.objects.create(ano=2020,local="Algo",areacientifica="algo",transporte=1)
        self.assertEquals(Inscricao.objects.filter(pk=inscricao.pk).exists(),True)
        individual = InscricaoIndividual.objects.create(nracompanhantes=1,participante_utilizador_idutilizador=self.part,inscricao_idinscricao=inscricao,telefone=987567874)
        self.assertEquals(InscricaoIndividual.objects.filter(pk=individual.pk).exists(),True)
        inscricao.delete()
        individual.delete()

    
    def testInscricaoColetiva(self):
        escola = Escola.objects.create(nome="Name",local='jskdfh',telefone="789678123",email="kjsdhfkjsdf@gmail.com")
        self.assertEquals(Escola.objects.filter(pk=escola.pk).exists(),True)
        inscricao =  Inscricao.objects.create(ano=2020,local="Algo",areacientifica="algo",transporte=1)
        self.assertEquals(Inscricao.objects.filter(pk=inscricao.pk).exists(),True)
        coletiva = InscricaoIndividual.objects.create(nresponsaveis=1,turma='A',participante_utilizador_idutilizador=self.part,inscricao_idinscricao=inscricao,telefone=987567874,escola_idescola=escola)
        self.assertEquals(InscricaoColetiva.objects.filter(pk=coletiva.pk).exists(),True)
        escola.delete()
        inscricao.delete()
        coletiva.delete()


    @classmethod
    def tearDownClass(self):
        self.user.delete()
        self.user1.delete()
        self.user2.delete()
        self.user3.delete()
        
        self.campus.delete()
        self.uo.delete()
        self.departamento.delete()
        self.espaco.delete()

        self.horario.delete()
        self.dia.delete()
        self.horarioDia.delete()

        self.part.delete()
        self.admin.delete()
        self.coord.delete()
        self.prof.delete()

        self.atividade1.delete()
        self.sessao1.delete()
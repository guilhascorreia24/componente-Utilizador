from django.db import models

# Create your models here.

class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    duracao = models.FloatField()
    descricao = models.CharField(max_length=250)
    professor_universitario_utilizador_idutilizador = models.ForeignKey('ProfessorUniversitario', models.DO_NOTHING, db_column='Professor Universitario_Utilizador_idutilizador')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade Organica_idUO')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    espaco_idespaco = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='espaco_idespaco')

    class Meta:
        managed = False
        db_table = 'atividade'
    
    def __str__(self):
        return self.idatividade


class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    telefone = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador'
    
    def __str__(self):
        return self.idutilizador


class Administrador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'
    
    def __str__(self):
        return self.utilizador_idutilizador

class Colaborador(models.Model):
    curso = models.CharField(max_length=45)
    preferencia = models.CharField(max_length=45, blank=True, null=True)
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    dia_aberto_ano = models.ForeignKey('DiaAberto', models.DO_NOTHING, db_column='Dia Aberto_ano')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'colaborador'
    
    def __str__(self):
        return self.utilizador_idutilizador

class Participante(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participante'
    
    def __str__(self):
        return self.utilizador_idutilizador

class ProfessorUniversitario(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade Organica_idUO')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'professor universitario'
    
    def __str__(self):
        return self.utilizador_idutilizador

class Coordenador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade Organica_idUO')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'coordenador'
    
    def __str__(self):
        return self.utilizador_idutilizador
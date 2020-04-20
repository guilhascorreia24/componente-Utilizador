from django.db import models

class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45,unique=True)
    email = models.CharField(unique=True, max_length=45)
    telefone = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.
    validada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utilizador'

    def __str__(self):
        return self.idutilizador

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Departamento(models.Model):
    iddepartamento = models.AutoField(primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45)
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'
    
    def __str__(self):
        return str(self.iddepartamento)


class Participante(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participante'
    
    def __str__(self):
        return self.utilizador_idutilizador

class ProfessorUniversitario(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor_universitario'

class Administrador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'
    
    def __str__(self):
        return self.utilizador_idutilizador

class Coordenador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'coordenador'
    
    def __str__(self):
        return self.utilizador_idutilizador

class Colaborador(models.Model):
    curso_idcurso = models.ForeignKey('Curso', models.DO_NOTHING, db_column='curso_idcurso', blank=True, null=True)
    preferencia = models.CharField(max_length=45, blank=True, null=True)
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    dia_aberto_ano = models.ForeignKey('DiaAberto', models.DO_NOTHING, db_column='Dia_Aberto_ano')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'colaborador'
    
    def __str__(self):
        return self.utilizador_idutilizador

class DiaAberto(models.Model):
    ano = models.TextField(primary_key=True)  # This field type is a guess.
    descricao = models.CharField(max_length=120, blank=True, null=True)
    datainscricao = models.DateField()
    emaildiaaberto = models.CharField(db_column='emailDiaAberto', max_length=120)  # Field name made lowercase.
    enderecopaginaweb = models.CharField(db_column='enderecoPaginaWeb', max_length=60)  # Field name made lowercase.
    datadiainscricaoatividadesinicio = models.DateField(db_column='dataDiainscricaoAtividadesInicio')  # Field name made lowercase.
    datadiaabertoinicio = models.DateField(db_column='dataDiaAbertoInicio')  # Field name made lowercase.
    datainscricaoatividadesfim = models.DateField(db_column='dataInscricaoAtividadesfim')  # Field name made lowercase.
    datadiaabertofim = models.DateField(db_column='dataDiaAbertofim')  # Field name made lowercase.
    datapropostaatividadeinicio = models.DateField(db_column='dataPropostaAtividadeInicio')  # Field name made lowercase.
    datapropostaatividadesfim = models.DateField(db_column='dataPropostaAtividadesFim')  # Field name made lowercase.
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dia_aberto'

    def __str__(self):
        return self.ano

class Campus(models.Model):
    idcampus = models.AutoField(db_column='idCampus', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'campus'
    
    def __str__(self):
        return self.idcampus
        
class UnidadeOrganica(models.Model):
    iduo = models.AutoField(db_column='idUO', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(max_length=5)
    campus_idcampus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='Campus_idCampus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidade_organica'
    
    def __str__(self):
        return str(self.iduo)

class Curso(models.Model):
    idcurso = models.IntegerField(primary_key=True)
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.
    nome = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'curso'
    
    def __str__(self):
        return self.idcurso

class Escola(models.Model):
    idescola = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'


class Inscricao(models.Model):
    idinscricao = models.AutoField(primary_key=True)
    ano = models.IntegerField()
    local = models.CharField(max_length=255)
    areacientifica = models.CharField(max_length=255)
    transporte = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inscricao'

class InscricaoColetiva(models.Model):
    nresponsaveis = models.IntegerField()
    turma = models.CharField(max_length=1)
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    escola_idescola = models.ForeignKey(Escola, models.DO_NOTHING, db_column='escola_idescola')
    nparticipantes = models.IntegerField()
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_coletiva'


class InscricaoIndividual(models.Model):
    nracompanhades = models.IntegerField()
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)
    telefone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inscricao_individual'
        
class Espaco(models.Model):
    idespaco = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    campus_idcampus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='campus_idCampus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'espaco'

class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    publico_alvo = models.CharField(max_length=45)
    duracao = models.FloatField()
    descricao = models.CharField(max_length=250)
    validada = models.IntegerField()
    professor_universitario_utilizador_idutilizador = models.ForeignKey('ProfessorUniversitario', models.DO_NOTHING, db_column='professor_universitario_Utilizador_idutilizador')  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    espaco_idespaco = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='espaco_idespaco', blank=True, null=True)
    tematica = models.CharField(max_length=250, blank=True, null=True)
    nrcolaborador = models.CharField(db_column='nrColaborador', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'

class Dia(models.Model):
    dia = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dia'

class Tarefa(models.Model):
    idtarefa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    concluida = models.IntegerField()
    coordenador_utilizador_idutilizador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='Coordenador_Utilizador_idutilizador')  # Field name made lowercase.
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    atividade_idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade', blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.TimeField()
    dia_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='dia_dia')

    class Meta:
        managed = False
        db_table = 'tarefa'


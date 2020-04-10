# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class Administrador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class Anfiteatro(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    espaco_idespaco = models.OneToOneField('Espaco', models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'anfiteatro'


class Arlivre(models.Model):
    descricao = models.CharField(max_length=45)
    espaco_idespaco = models.OneToOneField('Espaco', models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'arlivre'


class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    duracao = models.FloatField()
    descricao = models.CharField(max_length=250)
    validada = models.IntegerField()
    professor_universitario_utilizador_idutilizador = models.ForeignKey('ProfessorUniversitario', models.DO_NOTHING, db_column='professor_universitario_Utilizador_idutilizador')  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    espaco_idespaco = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='espaco_idespaco')

    class Meta:
        managed = False
        db_table = 'atividade'


class AtividadeHasMaterial(models.Model):
    atividade_idatividade = models.OneToOneField(Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade', primary_key=True)  # Field name made lowercase.
    material_idmaterial = models.ForeignKey('Material', models.DO_NOTHING, db_column='Material_idMaterial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade_has_material'
        unique_together = (('atividade_idatividade', 'material_idmaterial'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campus(models.Model):
    idcampus = models.AutoField(db_column='idCampus', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'campus'


class Colaborador(models.Model):
    curso = models.CharField(max_length=45)
    preferencia = models.CharField(max_length=45, blank=True, null=True)
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    dia_aberto_ano = models.ForeignKey('DiaAberto', models.DO_NOTHING, db_column='dia_aberto_ano')

    class Meta:
        managed = False
        db_table = 'colaborador'


class ColaboradorHasHorario(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    dia_dia = models.ForeignKey('Dia', models.DO_NOTHING, db_column='dia_dia')

    class Meta:
        managed = False
        db_table = 'colaborador_has_horario'


class ColaboradorHasUnidadeOrganica(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'colaborador_has_unidade_organica'


class Coordenador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador'


class CoordenadorHasDepartamento(models.Model):
    coordenador_utilizador_idutilizador = models.OneToOneField(Coordenador, models.DO_NOTHING, db_column='Coordenador_Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador_has_departamento'
        unique_together = (('coordenador_utilizador_idutilizador', 'departamento_iddepartamento'),)


class Departamento(models.Model):
    iddepartamento = models.AutoField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45)
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Dia(models.Model):
    dia = models.DateField(primary_key=True)
    horario_hora = models.ForeignKey('Horario', models.DO_NOTHING, db_column='horario_hora')

    class Meta:
        managed = False
        db_table = 'dia'


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
    utilizador_idutilizador = models.ForeignKey('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador')  # Field name made lowercase.
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dia_aberto'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Escola(models.Model):
    idescola = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    local = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escola'


class Espaco(models.Model):
    idespaco = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'espaco'


class Horario(models.Model):
    hora = models.TimeField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Idioma(models.Model):
    nome = models.CharField(primary_key=True, max_length=24)
    sigla = models.CharField(unique=True, max_length=45)
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'idioma'


class Inscricao(models.Model):
    idinscricao = models.AutoField(primary_key=True)
    ano = models.TextField()  # This field type is a guess.
    local = models.CharField(max_length=45)
    areacientifica = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'inscricao'


class InscricaoColetiva(models.Model):
    nresponsaveis = models.IntegerField()
    turma = models.CharField(max_length=1)
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    escola_idescola = models.ForeignKey(Escola, models.DO_NOTHING, db_column='escola_idescola')
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_coletiva'


class InscricaoHasPrato(models.Model):
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')
    prato_idprato = models.ForeignKey('Prato', models.DO_NOTHING, db_column='Prato_idPrato')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inscricao_has_prato'


class InscricaoHasSessao(models.Model):
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')
    sessao_idsessao = models.ForeignKey('Sessao', models.DO_NOTHING, db_column='sessao_idsessao')

    class Meta:
        managed = False
        db_table = 'inscricao_has_sessao'


class InscricaoIndividual(models.Model):
    nracompanhades = models.IntegerField()
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_individual'


class Material(models.Model):
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'material'


class Menu(models.Model):
    idmenu = models.AutoField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    precoaluno = models.FloatField(db_column='precoAluno')  # Field name made lowercase.
    precoprofessor = models.FloatField(db_column='PrecoProfessor')  # Field name made lowercase.
    tipo = models.CharField(max_length=45)
    menu = models.CharField(max_length=45)
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.
    campus_idcampus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='Campus_idCampus')  # Field name made lowercase.
    dia_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='dia_dia')

    class Meta:
        managed = False
        db_table = 'menu'


class Notificacao(models.Model):
    descricao = models.CharField(max_length=45)
    criadoem = models.DateTimeField(auto_now_add=True)
    idutilizadorenvia = models.IntegerField()
    utilizadorrecebe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notificacao'


class Participante(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participante'


class Prato(models.Model):
    idprato = models.AutoField(db_column='idPrato', primary_key=True)  # Field name made lowercase.
    nralomocosdisponiveis = models.IntegerField()
    descricao = models.CharField(max_length=125)
    menu_idmenu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='Menu_idMenu')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'prato'


class ProfessorUniversitario(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor_universitario'


class Responsaveis(models.Model):
    idresponsavel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    idinscricao = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='idInscricao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'responsaveis'


class Sala(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    gabinete = models.CharField(max_length=45, blank=True, null=True)
    espaco_idespaco = models.OneToOneField(Espaco, models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Sessao(models.Model):
    idsessao = models.AutoField(primary_key=True)
    nrinscritos = models.IntegerField()
    vagas = models.IntegerField()
    atividade_idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade')  # Field name made lowercase.
    dia_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='dia_dia')

    class Meta:
        managed = False
        db_table = 'sessao'


class Tarefa(models.Model):
    idtarefa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    concluida = models.IntegerField()
    coordenador_utilizador_idutilizador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='Coordenador_Utilizador_idutilizador')  # Field name made lowercase.
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    atividade_idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefa'


class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    capacidade = models.IntegerField()
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.
    identificacao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'transporte'


class TransporteHasHorario(models.Model):
    transporte_idtransporte = models.ForeignKey(Transporte, models.DO_NOTHING, db_column='transporte_idtransporte')
    dia_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='dia_dia')

    class Meta:
        managed = False
        db_table = 'transporte_has_horario'


class TransporteHasInscricao(models.Model):
    transporte_idtransporte = models.OneToOneField(Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')

    class Meta:
        managed = False
        db_table = 'transporte_has_inscricao'
        unique_together = (('transporte_idtransporte', 'inscricao_idinscricao'),)


class TransportePessoal(models.Model):
    transporte_idtransporte = models.OneToOneField(Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_pessoal'


class TransporteUniversitario(models.Model):
    capacidade = models.IntegerField()
    transporte_idtransporte = models.OneToOneField(Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_universitario'


class UnidadeOrganica(models.Model):
    iduo = models.AutoField(db_column='idUO', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(max_length=5)
    campus_idcampus = models.ForeignKey(Campus, models.DO_NOTHING, db_column='Campus_idCampus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidade_organica'


class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    telefone = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    username = models.CharField(db_column='userName', max_length=45)  # Field name made lowercase.
    validada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utilizador'


class UtilizadorHasNotificacao(models.Model):
    utilizador_idutilizador = models.ForeignKey(Utilizador, models.DO_NOTHING, db_column='Utilizador_idutilizador')  # Field name made lowercase.
    notificacao = models.ForeignKey(Notificacao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utilizador_has_notificacao'
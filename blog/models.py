# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    # Field name made lowercase.
    utilizador_idutilizador = models.OneToOneField(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Anfiteatro(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    espaco_idespaco = models.OneToOneField(
        'Espaco', models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'anfiteatro'


class Arlivre(models.Model):
    descricao = models.CharField(max_length=45)
    espaco_idespaco = models.OneToOneField(
        'Espaco', models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'arlivre'


class Atividade(models.Model):
    # Field name made lowercase.
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)
    titulo = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    publico_alvo = models.CharField(max_length=45)
    duracao = models.FloatField()
    descricao = models.CharField(max_length=250)
    validada = models.IntegerField()
    professor_universitario_utilizador_idutilizador = models.ForeignKey(
        'ProfessorUniversitario', models.DO_NOTHING, db_column='professor_universitario_Utilizador_idutilizador')  # Field name made lowercase.
    # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    espaco_idespaco = models.ForeignKey('Espaco', models.DO_NOTHING, db_column='espaco_idespaco', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atividade'


class AtividadeHasMaterial(models.Model):
    # Field name made lowercase.
    atividade_idatividade = models.OneToOneField(
        Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade', primary_key=True)
    # Field name made lowercase.
    material_idmaterial = models.ForeignKey(
        'Material', models.DO_NOTHING, db_column='Material_idMaterial')

    class Meta:
        managed = False
        db_table = 'atividade_has_material'
        unique_together = (('atividade_idatividade', 'material_idmaterial'),)


class Campus(models.Model):
    # Field name made lowercase.
    idcampus = models.AutoField(db_column='idCampus', primary_key=True)
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'campus'


class Colaborador(models.Model):
    curso = models.CharField(max_length=45)
    preferencia = models.CharField(max_length=45, blank=True, null=True)
    # Field name made lowercase.
    utilizador_idutilizador = models.OneToOneField(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)
    dia_aberto_ano = models.ForeignKey(
        'DiaAberto', models.DO_NOTHING, db_column='dia_aberto_ano')

    class Meta:
        managed = False
        db_table = 'colaborador'


class ColaboradorHasHorario(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(
        Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    horario_has_dia_id_dia_hora = models.ForeignKey(
        'HorarioHasDia', models.DO_NOTHING, db_column='horario_has_dia_id_dia_hora')

    class Meta:
        managed = False
        db_table = 'colaborador_has_horario'


class ColaboradorHasUnidadeOrganica(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(
        Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey(
        'UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')

    class Meta:
        managed = False
        db_table = 'colaborador_has_unidade_organica'


class Coordenador(models.Model):
    # Field name made lowercase.
    utilizador_idutilizador = models.OneToOneField(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)
    # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey(
        'UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')

    class Meta:
        managed = False
        db_table = 'coordenador'


class CoordenadorHasDepartamento(models.Model):
    coordenador_utilizador_idutilizador = models.OneToOneField(
        Coordenador, models.DO_NOTHING, db_column='Coordenador_Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey(
        'Departamento', models.DO_NOTHING, db_column='Departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador_has_departamento'
        unique_together = (
            ('coordenador_utilizador_idutilizador', 'departamento_iddepartamento'),)


class Departamento(models.Model):
    # Field name made lowercase.
    iddepartamento = models.AutoField(
        db_column='idDepartamento', primary_key=True)
    nome = models.CharField(max_length=45)
    # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey(
        'UnidadeOrganica', models.DO_NOTHING, db_column='unidade_organica_idUO')

    class Meta:
        managed = False
        db_table = 'departamento'


class Dia(models.Model):
    dia = models.DateField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dia'


class DiaAberto(models.Model):
    ano = models.TextField(primary_key=True)  # This field type is a guess.
    descricao = models.CharField(max_length=120, blank=True, null=True)
    datainscricao = models.DateField()
    # Field name made lowercase.
    emaildiaaberto = models.CharField(
        db_column='emailDiaAberto', max_length=120)
    # Field name made lowercase.
    enderecopaginaweb = models.CharField(
        db_column='enderecoPaginaWeb', max_length=60)
    datadiainscricaoatividadesinicio = models.DateField(
        db_column='dataDiainscricaoAtividadesInicio')  # Field name made lowercase.
    # Field name made lowercase.
    datadiaabertoinicio = models.DateField(db_column='dataDiaAbertoInicio')
    # Field name made lowercase.
    datainscricaoatividadesfim = models.DateField(
        db_column='dataInscricaoAtividadesfim')
    # Field name made lowercase.
    datadiaabertofim = models.DateField(db_column='dataDiaAbertofim')
    # Field name made lowercase.
    datapropostaatividadeinicio = models.DateField(
        db_column='dataPropostaAtividadeInicio')
    # Field name made lowercase.
    datapropostaatividadesfim = models.DateField(
        db_column='dataPropostaAtividadesFim')
    # Field name made lowercase.
    utilizador_idutilizador = models.ForeignKey(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador')
    administrador_utilizador_idutilizador = models.ForeignKey(
        Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dia_aberto'


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


class HorarioHasDia(models.Model):
    horario_hora = models.ForeignKey(
        Horario, models.DO_NOTHING, db_column='horario_hora')
    # Field name made lowercase.
    dia_dia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='Dia_dia')
    id_dia_hora = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'horario_has_dia'


class Idioma(models.Model):
    nome = models.CharField(primary_key=True, max_length=24)
    sigla = models.CharField(unique=True, max_length=45)
    administrador_utilizador_idutilizador = models.ForeignKey(
        Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

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
    participante_utilizador_idutilizador = models.ForeignKey(
        'Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    escola_idescola = models.ForeignKey(
        Escola, models.DO_NOTHING, db_column='escola_idescola')
    inscricao_idinscricao = models.OneToOneField(
        Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_coletiva'


class InscricaoHasPrato(models.Model):
    inscricao_idinscricao = models.ForeignKey(
        Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')
    # Field name made lowercase.
    prato_idprato = models.ForeignKey(
        'Prato', models.DO_NOTHING, db_column='Prato_idPrato')

    class Meta:
        managed = False
        db_table = 'inscricao_has_prato'


class InscricaoHasSessao(models.Model):
    inscricao_idinscricao = models.ForeignKey(
        Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')
    sessao_idsessao = models.ForeignKey(
        'Sessao', models.DO_NOTHING, db_column='sessao_idsessao')

    class Meta:
        managed = False
        db_table = 'inscricao_has_sessao'


class InscricaoIndividual(models.Model):
    nracompanhades = models.IntegerField()
    participante_utilizador_idutilizador = models.ForeignKey(
        'Participante', models.DO_NOTHING, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    inscricao_idinscricao = models.OneToOneField(
        Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_individual'


class Material(models.Model):
    # Field name made lowercase.
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'material'


class Menu(models.Model):
    # Field name made lowercase.
    idmenu = models.AutoField(db_column='idMenu', primary_key=True)
    # Field name made lowercase.
    precoaluno = models.FloatField(db_column='precoAluno')
    # Field name made lowercase.
    precoprofessor = models.FloatField(db_column='PrecoProfessor')
    tipo = models.CharField(max_length=45)
    menu = models.CharField(max_length=45)
    administrador_utilizador_idutilizador = models.ForeignKey(
        Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.
    # Field name made lowercase.
    campus_idcampus = models.ForeignKey(
        Campus, models.DO_NOTHING, db_column='Campus_idCampus')
    horario_has_dia_id_dia_hora = models.ForeignKey(
        HorarioHasDia, models.DO_NOTHING, db_column='horario_has_dia_id_dia_hora')

    class Meta:
        managed = False
        db_table = 'menu'


class Notificacao(models.Model):
    descricao = models.CharField(max_length=45)
    criadoem = models.DateTimeField()
    idutilizadorenvia = models.IntegerField()
    utilizadorrecebe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notificacao'


class Participante(models.Model):
    # Field name made lowercase.
    utilizador_idutilizador = models.OneToOneField(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)

    class Meta:
        managed = False
        db_table = 'participante'


class Prato(models.Model):
    # Field name made lowercase.
    idprato = models.AutoField(db_column='idPrato', primary_key=True)
    nralomocosdisponiveis = models.IntegerField()
    descricao = models.CharField(max_length=125)
    # Field name made lowercase.
    menu_idmenu = models.ForeignKey(
        Menu, models.DO_NOTHING, db_column='Menu_idMenu')

    class Meta:
        managed = False
        db_table = 'prato'


class ProfessorUniversitario(models.Model):
    # Field name made lowercase.
    utilizador_idutilizador = models.OneToOneField(
        'Utilizador', models.DO_NOTHING, db_column='Utilizador_idutilizador', primary_key=True)
    departamento_iddepartamento = models.ForeignKey(
        Departamento, models.DO_NOTHING, db_column='departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor_universitario'


class Responsaveis(models.Model):
    idresponsavel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    # Field name made lowercase.
    idinscricao = models.ForeignKey(
        Inscricao, models.DO_NOTHING, db_column='idInscricao')

    class Meta:
        managed = False
        db_table = 'responsaveis'


class Sala(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    gabinete = models.CharField(max_length=45, blank=True, null=True)
    espaco_idespaco = models.OneToOneField(
        Espaco, models.DO_NOTHING, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Sessao(models.Model):
    idsessao = models.AutoField(primary_key=True)
    nrinscritos = models.IntegerField()
    vagas = models.IntegerField()
    # Field name made lowercase.
    atividade_idatividade = models.ForeignKey(
        Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade')
    horario_has_dia_id_dia_hora = models.ForeignKey(
        HorarioHasDia, models.DO_NOTHING, db_column='horario_has_dia_id_dia_hora')

    class Meta:
        managed = False
        db_table = 'sessao'


class Tarefa(models.Model):
    idtarefa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    concluida = models.IntegerField()
    coordenador_utilizador_idutilizador = models.ForeignKey(
        Coordenador, models.DO_NOTHING, db_column='Coordenador_Utilizador_idutilizador')  # Field name made lowercase.
    colaborador_utilizador_idutilizador = models.ForeignKey(
        Colaborador, models.DO_NOTHING, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    # Field name made lowercase.
    atividade_idatividade = models.ForeignKey(
        Atividade, models.DO_NOTHING, db_column='Atividade_idAtividade')

    class Meta:
        managed = False
        db_table = 'tarefa'


class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    capacidade = models.IntegerField()
    administrador_utilizador_idutilizador = models.ForeignKey(
        Administrador, models.DO_NOTHING, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.
    identificacao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'transporte'


class TransporteHasHorario(models.Model):
    transporte_idtransporte = models.ForeignKey(
        Transporte, models.DO_NOTHING, db_column='transporte_idtransporte')
    horario_has_dia_id_dia_hora = models.ForeignKey(
        HorarioHasDia, models.DO_NOTHING, db_column='horario_has_dia_id_dia_hora')

    class Meta:
        managed = False
        db_table = 'transporte_has_horario'


class TransporteHasInscricao(models.Model):
    transporte_idtransporte = models.OneToOneField(
        Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)
    inscricao_idinscricao = models.ForeignKey(
        Inscricao, models.DO_NOTHING, db_column='inscricao_idinscricao')

    class Meta:
        managed = False
        db_table = 'transporte_has_inscricao'
        unique_together = (
            ('transporte_idtransporte', 'inscricao_idinscricao'),)


class TransportePessoal(models.Model):
    transporte_idtransporte = models.OneToOneField(
        Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_pessoal'


class TransporteUniversitario(models.Model):
    capacidade = models.IntegerField()
    transporte_idtransporte = models.OneToOneField(
        Transporte, models.DO_NOTHING, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_universitario'


class UnidadeOrganica(models.Model):
    # Field name made lowercase.
    iduo = models.AutoField(db_column='idUO', primary_key=True)
    sigla = models.CharField(max_length=5)
    # Field name made lowercase.
    campus_idcampus = models.ForeignKey(
        Campus, models.DO_NOTHING, db_column='Campus_idCampus')

    class Meta:
        managed = False
        db_table = 'unidade_organica'


class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    email = models.CharField(unique=True, max_length=45)
    telefone = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45)
    # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=45)
    validada = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utilizador'


class UtilizadorHasNotificacao(models.Model):
    # Field name made lowercase.
    utilizador_idutilizador = models.ForeignKey(
        Utilizador, models.DO_NOTHING, db_column='Utilizador_idutilizador')
    notificacao = models.ForeignKey(Notificacao, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utilizador_has_notificacao'

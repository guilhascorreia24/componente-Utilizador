# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from inscricao import validators 
from inscricao.validators import email_validator, not_zero_validator, telefone_validator,escola_ano_validator,smaller_zero_validator
from django.dispatch import receiver
from django.db.models import F, DEFERRED
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.utils.translation import gettext_lazy as _


class Administrador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.CASCADE, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class Anfiteatro(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    espaco_idespaco = models.OneToOneField('Espaco', models.CASCADE, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'anfiteatro'


class Arlivre(models.Model):
    descricao = models.CharField(max_length=255)
    espaco_idespaco = models.OneToOneField('Espaco', models.CASCADE, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'arlivre'


class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=45)
    capacidade = models.IntegerField()
    publico_alvo = models.CharField(max_length=45)
    duracao = models.FloatField()
    descricao = models.CharField(max_length=250)
    validada = models.IntegerField()
    professor_universitario_utilizador_idutilizador = models.ForeignKey('ProfessorUniversitario', models.CASCADE, db_column='professor_universitario_Utilizador_idutilizador')  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.CASCADE, db_column='unidade_organica_idUO')  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.CASCADE, db_column='Departamento_idDepartamento')  # Field name made lowercase.
    espaco_idespaco = models.ForeignKey('Espaco', models.CASCADE, db_column='espaco_idespaco', blank=True, null=True)
    tematica = models.CharField(max_length=250, blank=True, null=True)
    nrcolaborador = models.CharField(db_column='nrColaborador', max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __id__(self):
        return self.idatividade

    class Meta:
        managed = False
        db_table = 'atividade'


class AtividadeHasMaterial(models.Model):
    atividade_idatividade = models.OneToOneField(Atividade, models.CASCADE, db_column='Atividade_idAtividade', primary_key=True)  # Field name made lowercase.
    material_idmaterial = models.ForeignKey('Material', models.CASCADE, db_column='Material_idMaterial')  # Field name made lowercase.

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
    group = models.ForeignKey(AuthGroup, models.CASCADE)
    permission = models.ForeignKey('AuthPermission', models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE)
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
    user = models.ForeignKey(AuthUser, models.CASCADE)
    group = models.ForeignKey(AuthGroup, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.CASCADE)
    permission = models.ForeignKey(AuthPermission, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Campus(models.Model):
    idcampus = models.AutoField(db_column='idCampus', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255)

    def __str__(self):
        return str(self.nome)

    class Meta:
        managed = False
        db_table = 'campus'


class Colaborador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.CASCADE, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    curso_idcurso = models.ForeignKey('Curso', models.CASCADE, db_column='curso_idcurso', blank=True, null=True)

    def __id__(self):
        return self.utilizador_idutilizador.idutilizador

    class Meta:
        managed = False
        db_table = 'colaborador'


class ColaboradorHasHorario(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.CASCADE, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    horario_has_dia_id_dia_hora = models.ForeignKey('HorarioHasDia', models.CASCADE, db_column='horario_has_dia_id_dia_hora')
    colaborador_has_horario_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'colaborador_has_horario'


class ColaboradorHasUnidadeOrganica(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.CASCADE, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.CASCADE, db_column='unidade_organica_idUO')  # Field name made lowercase.
    colaborador_has_unidade_organica_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'colaborador_has_unidade_organica'


class Coordenador(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.CASCADE, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.CASCADE, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador'


class CoordenadorHasDepartamento(models.Model):
    coordenador_utilizador_idutilizador = models.OneToOneField(Coordenador, models.CASCADE, db_column='Coordenador_Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey('Departamento', models.CASCADE, db_column='Departamento_idDepartamento')  # Field name made lowercase.

    def __id__(self):
        return self.utilizador_idutilizador.idutilizador

    class Meta:
        managed = False
        db_table = 'coordenador_has_departamento'


class Curso(models.Model):
    idcurso = models.AutoField(primary_key=True)
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.CASCADE, db_column='unidade_organica_idUO')  # Field name made lowercase.
    nome = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'curso'


class Departamento(models.Model):
    iddepartamento = models.AutoField(db_column='idDepartamento', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=255)
    unidade_organica_iduo = models.ForeignKey('UnidadeOrganica', models.CASCADE, db_column='unidade_organica_idUO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departamento'


class Dia(models.Model):
    dia = models.DateField(primary_key=True)

    def __id__(self):
        return self.dia

    def __str__(self):
        return str(self.dia)

    class Meta:
        managed = False
        db_table = 'dia'


class DiaAberto(models.Model):
    ano = models.TextField(primary_key=True)  # This field type is a guess.
    descricao = models.CharField(max_length=120, blank=True, null=True)
    emaildiaaberto = models.CharField(db_column='emailDiaAberto', max_length=120)  # Field name made lowercase.
    enderecopaginaweb = models.CharField(db_column='enderecoPaginaWeb', max_length=60)  # Field name made lowercase.
    datadiaabertoinicio = models.DateField(db_column='dataDiaAbertoInicio')  # Field name made lowercase.
    datadiaabertofim = models.DateField(db_column='dataDiaAbertofim')  # Field name made lowercase.
    datainscricaonasatividadesinicio = models.DateField()
    datainscricaonasatividadesfim = models.DateField()
    datapropostaatividadeinicio = models.DateField(db_column='dataPropostaAtividadeInicio')  # Field name made lowercase.
    datapropostaatividadesfim = models.DateField(db_column='dataPropostaAtividadesFim')  # Field name made lowercase.
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.CASCADE, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.
    preco_almoco_estudante = models.FloatField()
    preco_almoco_professor = models.FloatField()

    class Meta:
        managed = False
        db_table = 'dia_aberto'


class Disponibilidade(models.Model):
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.CASCADE, db_column='colaborador_Utilizador_idutilizador')  # Field name made lowercase.
    dia_dia = models.ForeignKey(Dia, models.CASCADE, db_column='dia_dia')
    horario_hora = models.ForeignKey('Horario', models.CASCADE, db_column='horario_hora',related_name="disponibilidade_hora_inicio")
    horario_hora1 = models.ForeignKey('Horario', models.CASCADE, db_column='horario_hora1',related_name="disponibilidade_hora_fim")
    tipo_de_tarefa = models.CharField(max_length=45)
    disponibilidade_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'disponibilidade'

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)

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
    nome = models.CharField(max_length=255)
    local = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45,validators=[telefone_validator])
    email = models.CharField(max_length=255, blank=True, null=True,validators=[email_validator])

    class Meta:
        managed = False
        db_table = 'escola'


class Espaco(models.Model):
    idespaco = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    campus_idcampus = models.ForeignKey(Campus, models.CASCADE, db_column='campus_idCampus')  # Field name made lowercase.
    img = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'espaco'


class Horario(models.Model):
    hora = models.TimeField(primary_key=True)

    def __str__(self):
        return str(self.hora)

    class Meta:
        managed = False
        db_table = 'horario'


class HorarioHasDia(models.Model):
    horario_hora = models.ForeignKey(Horario, models.CASCADE, db_column='horario_hora')
    dia_dia = models.ForeignKey(Dia, models.CASCADE, db_column='Dia_dia')  # Field name made lowercase.
    id_dia_hora = models.AutoField(primary_key=True)

    def __id__(self):
        return self.id_dia_hora

    def __str__(self):
        return self.horario_hora.__str__() + " de " + self.dia_dia.__str__()

    class Meta:
        managed = False
        db_table = 'horario_has_dia'


class Idioma(models.Model):
    nome = models.CharField(primary_key=True, max_length=255)
    sigla = models.CharField(unique=True, max_length=45)
    administrador_utilizador_idutilizador = models.ForeignKey(Administrador, models.CASCADE, db_column='Administrador_Utilizador_idutilizador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'idioma'


class Inscricao(models.Model):
    idinscricao = models.AutoField(primary_key=True)
    ano = models.IntegerField(validators=[escola_ano_validator])
    local = models.CharField(max_length=255)
    areacientifica = models.CharField(max_length=255)
    transporte = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inscricao'


class InscricaoColetiva(models.Model):
    nresponsaveis = models.IntegerField()
    turma = models.CharField(max_length=1)
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.CASCADE, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    escola_idescola = models.ForeignKey(Escola, models.CASCADE, db_column='escola_idescola')
    nparticipantes = models.IntegerField(validators=[not_zero_validator,smaller_zero_validator])
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.CASCADE, db_column='inscricao_idinscricao', primary_key=True)

    class Meta:
        managed = False
        db_table = 'inscricao_coletiva'


class InscricaoHasPrato(models.Model):
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.CASCADE, db_column='inscricao_idinscricao')
    prato_idprato = models.ForeignKey('Prato', models.CASCADE, db_column='Prato_idPrato')  # Field name made lowercase.
    inscricao_has_prato_id = models.AutoField(primary_key=True)
    nralmocos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inscricao_has_prato'

@receiver(models.signals.pre_delete, sender=InscricaoHasPrato)
def delete_Inscricao_prato(sender, instance, using, **kwargs):
    instance.prato_idprato.delete()
    #delete_prato(None,instance.prato_idprato,None)

class InscricaoHasSessao(models.Model):
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.CASCADE, db_column='inscricao_idinscricao')
    sessao_idsessao = models.ForeignKey('Sessao', models.CASCADE, db_column='sessao_idsessao')
    inscricao_has_sessao_id = models.AutoField(primary_key=True)
    nr_inscritos = models.IntegerField(validators=[smaller_zero_validator,not_zero_validator])

    def save(self, *args, **kwargs):
        Sessao.objects.filter(idsessao=self.sessao_idsessao.pk).update(nrinscritos=F('nrinscritos')+self.nr_inscritos)
        return super(InscricaoHasSessao, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        insc = InscricaoHasSessao.objects.filter(inscricao_idinscricao=self.inscricao_idinscricao).nr_inscritos
        delta = self.nr_inscritos-insc
        Sessao.objects.filter(idsessao=self.sessao_idsessao.pk).update(nrinscritos=F('nrinscritos')+delta)
        super(InscricaoHasSessao,self).update(*args, **kwargs)


    class Meta:
        managed = False
        db_table = 'inscricao_has_sessao'

@receiver(models.signals.post_delete, sender=InscricaoHasSessao)
def delete_sessao_inscricao(sender, instance, using, **kwargs):
    Sessao.objects.filter(idsessao=instance.sessao_idsessao.pk).update(nrinscritos=F('nrinscritos')-instance.nr_inscritos)


class InscricaoIndividual(models.Model):
    nracompanhantes = models.IntegerField()
    participante_utilizador_idutilizador = models.ForeignKey('Participante', models.CASCADE, db_column='Participante_Utilizador_idutilizador')  # Field name made lowercase.
    inscricao_idinscricao = models.OneToOneField(Inscricao, models.CASCADE, db_column='inscricao_idinscricao', primary_key=True)
    telefone = models.IntegerField(validators=[telefone_validator])

    class Meta:
        managed = False
        db_table = 'inscricao_individual'


class Material(models.Model):
    idmaterial = models.AutoField(db_column='idMaterial', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'material'


class Menu(models.Model):
    idmenu = models.AutoField(db_column='idMenu', primary_key=True)  # Field name made lowercase.
    menu = models.CharField(max_length=45)
    descricao = models.CharField(max_length=125, blank=True, null=True)
    campus_idcampus = models.ForeignKey(Campus, models.CASCADE, db_column='Campus_idCampus')  # Field name made lowercase.
    horario_has_dia_id_dia_hora = models.ForeignKey(HorarioHasDia, models.CASCADE, db_column='horario_has_dia_id_dia_hora')
    nralmocosdisponiveis = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu'


class Notificacao(models.Model):
    descricao = models.CharField(max_length=255)
    criadoem = models.DateTimeField()
    idutilizadorenvia = models.IntegerField()
    utilizadorrecebe = models.IntegerField()
    assunto = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'notificacao'


class Paragem(models.Model):
    paragem = models.CharField(primary_key=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'paragem'


class Participante(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.CASCADE, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'participante'


class Prato(models.Model):
    idprato = models.AutoField(db_column='idPrato', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45)
    descricao = models.CharField(max_length=125)
    nralmocos = models.IntegerField(blank=True, null=True)
    menu_idmenu = models.ForeignKey(Menu, models.CASCADE, db_column='menu_idMenu')  # Field name made lowercase.
        
        
    def save(self, *args, **kwargs):
        obj = Menu.objects.get(idmenu=self.menu_idmenu.pk)
        Menu.objects.filter(idmenu=self.menu_idmenu.pk).update(nralmocosdisponiveis=F('nralmocosdisponiveis')-self.nralmocos)
        return super(Prato, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        insc = Prato.objects.filter(inscricao_idinscricao=self.inscricao_idinscricao).nralmocos
        delta = self.nralmocos-insc
        Menu.objects.filter(idmenu=self.menu_idmenu.pk).update(nralmocosdisponiveis=F('nralmocosdisponiveis')-delta)
        super(Prato,self).update(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'prato'

@receiver(models.signals.pre_delete, sender=Prato)
def delete_prato(sender, instance, using, **kwargs):
    Menu.objects.filter(idmenu=instance.menu_idmenu.pk).update(nralmocosdisponiveis=F('nralmocosdisponiveis')+instance.nralmocos)


class ProfessorUniversitario(models.Model):
    utilizador_idutilizador = models.OneToOneField('Utilizador', models.CASCADE, db_column='Utilizador_idutilizador', primary_key=True)  # Field name made lowercase.
    departamento_iddepartamento = models.ForeignKey(Departamento, models.CASCADE, db_column='departamento_idDepartamento')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor_universitario'


class Responsaveis(models.Model):
    idresponsavel = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255,validators=[email_validator])
    telefone = models.CharField(max_length=45,validators=[telefone_validator])
    idinscricao = models.ForeignKey(Inscricao, models.CASCADE, db_column='idInscricao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'responsaveis'


class Sala(models.Model):
    edificio = models.CharField(max_length=45)
    andar = models.CharField(max_length=45)
    gabinete = models.CharField(max_length=45, blank=True, null=True)
    espaco_idespaco = models.OneToOneField(Espaco, models.CASCADE, db_column='espaco_idespaco', primary_key=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Sessao(models.Model):
    idsessao = models.AutoField(primary_key=True)
    nrinscritos = models.IntegerField()
    capacidade = models.IntegerField()
    atividade_idatividade = models.ForeignKey(Atividade, models.CASCADE, db_column='Atividade_idAtividade')  # Field name made lowercase.
    horario_has_dia_id_dia_hora = models.ForeignKey(HorarioHasDia, models.CASCADE, db_column='horario_has_dia_id_dia_hora')

    def __id__(self):
        return self.idsessao
        
    class Meta:
        managed = False
        db_table = 'sessao'


class SessaoHasHorarioHasDia(models.Model):
    sessao_idsessao = models.ForeignKey(Sessao, models.CASCADE, db_column='sessao_idsessao')
    horario_has_dia_id_dia_hora = models.ForeignKey(HorarioHasDia, models.CASCADE, db_column='horario_has_dia_id_dia_hora')
    sessao_has_horario_has_dia_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sessao_has_horario_has_dia'


class Tarefa(models.Model):
    idtarefa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    concluida = models.IntegerField()
    coordenador_utilizador_idutilizador = models.ForeignKey(Coordenador, models.CASCADE, db_column='Coordenador_Utilizador_idutilizador')  # Field name made lowercase.
    colaborador_utilizador_idutilizador = models.ForeignKey(Colaborador, models.CASCADE, db_column='colaborador_Utilizador_idutilizador', blank=True, null=True)  # Field name made lowercase.
    hora_inicio = models.TimeField(blank=True, null=True)
    dia_dia = models.ForeignKey(Dia, models.CASCADE, db_column='dia_dia', blank=True, null=True)
    sessao_idsessao = models.ForeignKey(Sessao, models.CASCADE, db_column='sessao_idsessao', blank=True, null=True)
    buscar = models.ForeignKey(Espaco, models.CASCADE, db_column='buscar', blank=True, null=True,related_name="Tarefa_buscar")
    levar = models.ForeignKey(Espaco, models.CASCADE, db_column='levar', blank=True, null=True,related_name="Tarefa_levar")
    inscricao_coletiva_inscricao_idinscricao = models.ForeignKey(InscricaoColetiva, models.CASCADE, db_column='inscricao_coletiva_inscricao_idinscricao', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarefa'


class Transporte(models.Model):
    idtransporte = models.AutoField(primary_key=True)
    capacidade = models.IntegerField()
    identificacao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'transporte'


class TransporteHasHorario(models.Model):
    transporte_idtransporte = models.ForeignKey(Transporte, models.CASCADE, db_column='transporte_idtransporte')
    id_transporte_has_horario = models.IntegerField(primary_key=True)
    origem = models.ForeignKey(Paragem, models.CASCADE, db_column='origem',related_name="origem")
    destino = models.ForeignKey(Paragem, models.CASCADE, db_column='destino',related_name="destino")
    horario_has_dia_id_dia_hora = models.ForeignKey(HorarioHasDia, models.CASCADE, db_column='horario_has_dia_id_dia_hora')
    n_passageiros = models.IntegerField(blank=True, null=True,validators=[not_zero_validator,smaller_zero_validator])

    def __str__(self):
        return self.origem.paragem + " -> " + self.destino.paragem + " | " + self.horario_has_dia_id_dia_hora.__str__() + " | Lugares restantes: " + str(self.transporte_idtransporte.capacidade - self.n_passageiros)

    class Meta:
        managed = False
        db_table = 'transporte_has_horario'


#Validation is checked
class TransporteHasInscricao(models.Model):
    inscricao_idinscricao = models.ForeignKey(Inscricao, models.CASCADE, db_column='inscricao_idinscricao')
    transporte_has_inscricao_id = models.AutoField(primary_key=True)
    horario = models.ForeignKey(TransporteHasHorario, models.CASCADE, db_column='transporte_has_horario_id_transporte_has_horario')
    n_passageiros = models.IntegerField(validators=[smaller_zero_validator])

    def save(self, *args, **kwargs):
        TransporteHasHorario.objects.filter(id_transporte_has_horario=self.horario.pk).update(n_passageiros=F('n_passageiros')+self.n_passageiros)
        return super(TransporteHasInscricao, self).save(*args, **kwargs)
    
    def update(self, *args, **kwargs):
        old = TransporteHasInscricao.objects.filter(transporte_has_inscricao_id=self.transporte_has_inscricao_id).n_passageiros
        delta = self.n_passageiros - old
        TransporteHasHorario.objects.filter(id_transporte_has_horario=self.horario).update(n_passageiros=F('n_passageiros')+delta)
        super(TransporteHasInscricao,self).update(*args, **kwargs)
    
    def clean(self):
        super().clean()
        try:
            data = TransporteHasHorario.objects.select_related('transporte_idtransporte').get(id_transporte_has_horario=self.horario.pk)
        except:
            raise ValidationError({'horario': "Opção inválida"})
        capacidade = data.transporte_idtransporte.capacidade - data.n_passageiros
        print(str(data.n_passageiros) + " - " + str(data.transporte_idtransporte.capacidade))
        if capacidade < self.n_passageiros:
            #Check for equal entry already in database
            try:
                curr = TransporteHasInscricao.objects.get(transporte_has_inscricao_id=self.transporte_has_inscricao_id).n_passageiros
                passageiros = self.n_passageiros - curr
                if capacidade < passageiros:
                    error = validators.TRANSPORTE_FULL.replace('_NUM_',str(capacidade))
                    raise ValidationError({'n_passageiros': error})

            except ObjectDoesNotExist:
                print("Error")
                error = validators.TRANSPORTE_FULL.replace('_NUM_',str(capacidade))
                raise ValidationError({'n_passageiros': error}) 

    class Meta:
        managed = False
        db_table = 'transporte_has_inscricao'

@receiver(models.signals.post_delete, sender=TransporteHasInscricao)
def delete_transporte(sender, instance, using, **kwargs):
    TransporteHasHorario.objects.filter(id_transporte_has_horario=instance.horario.pk).update(n_passageiros=F('n_passageiros')-instance.n_passageiros)


class TransportePessoal(models.Model):
    transporte_idtransporte = models.OneToOneField(Transporte, models.CASCADE, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_pessoal'


class TransporteUniversitario(models.Model):
    capacidade = models.IntegerField()
    transporte_idtransporte = models.OneToOneField(Transporte, models.CASCADE, db_column='transporte_idtransporte', primary_key=True)

    class Meta:
        managed = False
        db_table = 'transporte_universitario'


class UnidadeOrganica(models.Model):
    iduo = models.AutoField(db_column='idUO', primary_key=True)  # Field name made lowercase.
    sigla = models.CharField(max_length=255)
    campus_idcampus = models.ForeignKey(Campus, models.CASCADE, db_column='Campus_idCampus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'unidade_organica'


class Utilizador(models.Model):
    idutilizador = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255,validators=[email_validator])
    telefone = models.CharField(unique=True, max_length=45,validators=[telefone_validator])
    password = models.CharField(max_length=255)
    validada = models.IntegerField()
    remember_me = models.CharField(max_length=255, blank=True, null=True)
    dia_aberto_ano = models.ForeignKey(DiaAberto, models.CASCADE, db_column='dia_aberto_ano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador'


class UtilizadorHasNotificacao(models.Model):
    utilizador_idutilizador = models.ForeignKey(Utilizador, models.CASCADE, db_column='Utilizador_idutilizador')  # Field name made lowercase.
    notificacao = models.ForeignKey(Notificacao, models.CASCADE)
    utilizador_has_notificacao_id = models.AutoField(primary_key=True)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'utilizador_has_notificacao'

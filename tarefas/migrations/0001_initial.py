# Generated by Django 3.0.3 on 2020-05-23 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('idatividade', models.AutoField(db_column='idAtividade', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=45)),
                ('capacidade', models.IntegerField()),
                ('publico_alvo', models.CharField(max_length=45)),
                ('duracao', models.FloatField()),
                ('descricao', models.CharField(max_length=250)),
                ('validada', models.IntegerField()),
                ('tematica', models.CharField(blank=True, max_length=250, null=True)),
                ('nrcolaborador', models.CharField(blank=True, db_column='nrColaborador', max_length=45, null=True)),
            ],
            options={
                'db_table': 'atividade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('idcampus', models.AutoField(db_column='idCampus', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'campus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColaboradorHasHorario',
            fields=[
                ('colaborador_has_horario_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'colaborador_has_horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ColaboradorHasUnidadeOrganica',
            fields=[
                ('colaborador_has_unidade_organica_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'colaborador_has_unidade_organica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddepartamento', models.AutoField(db_column='idDepartamento', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('dia', models.DateField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DiaAberto',
            fields=[
                ('ano', models.TextField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(blank=True, max_length=120, null=True)),
                ('emaildiaaberto', models.CharField(db_column='emailDiaAberto', max_length=120)),
                ('enderecopaginaweb', models.CharField(db_column='enderecoPaginaWeb', max_length=60)),
                ('datadiaabertoinicio', models.DateField(db_column='dataDiaAbertoInicio')),
                ('datadiaabertofim', models.DateField(db_column='dataDiaAbertofim')),
                ('datapropostaatividadeinicio', models.DateField(db_column='dataPropostaAtividadeInicio')),
                ('datapropostaatividadesfim', models.DateField(db_column='dataPropostaAtividadesFim')),
                ('preco_almoco_estudante', models.FloatField()),
                ('preco_almoco_professor', models.FloatField()),
            ],
            options={
                'db_table': 'dia_aberto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('tipo_tarefa', models.CharField(db_column='TIpo_tarefa', max_length=255)),
                ('disponibilidade_id', models.IntegerField(db_column='Disponibilidade_id', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'disponibilidade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('idescola', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=45)),
                ('telefone', models.CharField(max_length=45)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'escola',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Espaco',
            fields=[
                ('idespaco', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'espaco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('hora', models.TimeField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HorarioHasDia',
            fields=[
                ('id_dia_hora', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'horario_has_dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('nome', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sigla', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'idioma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('idinscricao', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('local', models.CharField(max_length=255)),
                ('areacientifica', models.CharField(max_length=255)),
                ('transporte', models.IntegerField()),
            ],
            options={
                'db_table': 'inscricao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscricaoHasPrato',
            fields=[
                ('inscricao_has_prato_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'inscricao_has_prato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscricaoHasSessao',
            fields=[
                ('inscricao_has_sessao_id', models.AutoField(primary_key=True, serialize=False)),
                ('nr_inscritos', models.IntegerField()),
            ],
            options={
                'db_table': 'inscricao_has_sessao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('idmaterial', models.AutoField(db_column='idMaterial', primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('idmenu', models.AutoField(db_column='idMenu', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=45)),
                ('menu', models.CharField(max_length=45)),
                ('nralmoçosdisponiveis', models.IntegerField(db_column='nralmocosdisponiveis')),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('criadoem', models.DateTimeField()),
                ('idutilizadorenvia', models.IntegerField()),
                ('utilizadorrecebe', models.IntegerField()),
                ('assunto', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'notificacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paragem',
            fields=[
                ('paragem', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'paragem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('idprato', models.AutoField(db_column='idPrato', primary_key=True, serialize=False)),
                ('nralmocos', models.IntegerField()),
                ('descricao', models.CharField(max_length=125)),
            ],
            options={
                'db_table': 'prato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Responsaveis',
            fields=[
                ('idresponsavel', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'responsaveis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('idsessao', models.AutoField(primary_key=True, serialize=False)),
                ('nrinscritos', models.IntegerField()),
                ('capacidade', models.IntegerField(db_column='capacidade')),
            ],
            options={
                'db_table': 'sessao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SessaoHasHorarioHasDia',
            fields=[
                ('sessao_has_horario_has_dia_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sessao_has_horario_has_dia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('idtarefa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('concluida', models.IntegerField()),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tarefa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('idtransporte', models.AutoField(primary_key=True, serialize=False)),
                ('capacidade', models.IntegerField()),
                ('identificacao', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'transporte',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransporteHasHorario',
            fields=[
                ('id_transporte_has_horario', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'transporte_has_horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransporteHasInscricao',
            fields=[
                ('transporte_has_inscricao_id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_passageiros', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'transporte_has_inscricao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UnidadeOrganica',
            fields=[
                ('iduo', models.AutoField(db_column='idUO', primary_key=True, serialize=False)),
                ('sigla', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'unidade_organica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('idutilizador', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('telefone', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('validada', models.IntegerField()),
                ('remember_me', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'utilizador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtilizadorHasNotificacao',
            fields=[
                ('utilizador_has_notificacao_id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'utilizador_has_notificacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('utilizador_idutilizador', models.OneToOneField(db_column='Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Utilizador')),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Anfiteatro',
            fields=[
                ('edificio', models.CharField(max_length=45)),
                ('andar', models.CharField(max_length=45)),
                ('espaco_idespaco', models.OneToOneField(db_column='espaco_idespaco', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Espaco')),
            ],
            options={
                'db_table': 'anfiteatro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arlivre',
            fields=[
                ('descricao', models.CharField(max_length=255)),
                ('espaco_idespaco', models.OneToOneField(db_column='espaco_idespaco', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Espaco')),
            ],
            options={
                'db_table': 'arlivre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AtividadeHasMaterial',
            fields=[
                ('atividade_idatividade', models.OneToOneField(db_column='Atividade_idAtividade', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Atividade')),
            ],
            options={
                'db_table': 'atividade_has_material',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('utilizador_idutilizador', models.OneToOneField(db_column='Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Utilizador')),
            ],
            options={
                'db_table': 'colaborador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('utilizador_idutilizador', models.OneToOneField(db_column='Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Utilizador')),
            ],
            options={
                'db_table': 'coordenador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscricaoColetiva',
            fields=[
                ('nresponsaveis', models.IntegerField()),
                ('turma', models.CharField(max_length=1)),
                ('nparticipantes', models.IntegerField()),
                ('inscricao_idinscricao', models.OneToOneField(db_column='inscricao_idinscricao', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Inscricao')),
            ],
            options={
                'db_table': 'inscricao_coletiva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscricaoIndividual',
            fields=[
                ('nracompanhades', models.IntegerField()),
                ('inscricao_idinscricao', models.OneToOneField(db_column='inscricao_idinscricao', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Inscricao')),
                ('telefone', models.IntegerField()),
            ],
            options={
                'db_table': 'inscricao_individual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('utilizador_idutilizador', models.OneToOneField(db_column='Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Utilizador')),
            ],
            options={
                'db_table': 'participante',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProfessorUniversitario',
            fields=[
                ('utilizador_idutilizador', models.OneToOneField(db_column='Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Utilizador')),
            ],
            options={
                'db_table': 'professor_universitario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('edificio', models.CharField(max_length=45)),
                ('andar', models.CharField(max_length=45)),
                ('gabinete', models.CharField(blank=True, max_length=45, null=True)),
                ('espaco_idespaco', models.OneToOneField(db_column='espaco_idespaco', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Espaco')),
            ],
            options={
                'db_table': 'sala',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransportePessoal',
            fields=[
                ('transporte_idtransporte', models.OneToOneField(db_column='transporte_idtransporte', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Transporte')),
            ],
            options={
                'db_table': 'transporte_pessoal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TransporteUniversitario',
            fields=[
                ('capacidade', models.IntegerField()),
                ('transporte_idtransporte', models.OneToOneField(db_column='transporte_idtransporte', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Transporte')),
            ],
            options={
                'db_table': 'transporte_universitario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoordenadorHasDepartamento',
            fields=[
                ('coordenador_utilizador_idutilizador', models.OneToOneField(db_column='Coordenador_Utilizador_idutilizador', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='tarefas.Coordenador')),
            ],
            options={
                'db_table': 'coordenador_has_departamento',
                'managed': False,
            },
        ),
    ]

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_curso'),
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
            name='Tarefa',
            fields=[
                ('idtarefa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('concluida', models.IntegerField()),
                ('hora_inicio', models.TimeField()),
            ],
            options={
                'db_table': 'tarefa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InscricaoColetiva',
            fields=[
                ('nresponsaveis', models.IntegerField()),
                ('turma', models.CharField(max_length=1)),
                ('nparticipantes', models.IntegerField()),
                ('inscricao_idinscricao', models.OneToOneField(db_column='inscricao_idinscricao', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Inscricao')),
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
                ('inscricao_idinscricao', models.OneToOneField(db_column='inscricao_idinscricao', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='user.Inscricao')),
                ('telefone', models.IntegerField()),
            ],
            options={
                'db_table': 'inscricao_individual',
                'managed': False,
            },
        ),
    ]

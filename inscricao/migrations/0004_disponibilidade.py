# Generated by Django 3.0.3 on 2020-05-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricao', '0003_anfiteatro_arlivre_atividadehasmaterial_authgroup_authgrouppermissions_authpermission_authuser_authu'),
    ]

    operations = [
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
    ]

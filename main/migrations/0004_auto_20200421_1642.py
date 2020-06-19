# Generated by Django 3.0.3 on 2020-04-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200416_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('idcurso', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'curso',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='InscricaoHasSessao',
        ),
    ]

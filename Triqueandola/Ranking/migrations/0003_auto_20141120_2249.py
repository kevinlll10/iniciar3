# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0002_auto_20141118_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
                ('ciclo', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dictado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semestre', models.IntegerField()),
                ('exigencia', models.PositiveIntegerField()),
                ('pedagogia', models.PositiveIntegerField()),
                ('conocimiento', models.PositiveIntegerField()),
                ('pasabilidad', models.PositiveIntegerField()),
                ('curso', models.ForeignKey(to='Ranking.Curso')),
                ('profesor', models.ForeignKey(to='Ranking.Profesor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cursodictado',
            name='profesores',
        ),
        migrations.AddField(
            model_name='curso',
            name='profesores',
            field=models.ManyToManyField(to='Ranking.Profesor', through='Ranking.Dictado'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='curso',
        ),
        migrations.DeleteModel(
            name='CursoDictado',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='profesor',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='escuela',
        ),
        migrations.AddField(
            model_name='comentario',
            name='cursoDictado',
            field=models.ForeignKey(to='Ranking.Dictado', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='conocimientoP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='exigenciaP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='pasabilidadP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='pedagogiaP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]

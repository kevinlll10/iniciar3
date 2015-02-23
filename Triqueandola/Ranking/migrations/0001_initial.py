# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contenido', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField(verbose_name=b'Fecha de comentario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CursoDictado',
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
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
                ('escuela', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cursodictado',
            name='profesor',
            field=models.ManyToManyField(to='Ranking.Profesor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(to='Ranking.Estudiante'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='curso',
            field=models.ForeignKey(to='Ranking.CursoDictado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='profesor',
            field=models.ForeignKey(to='Ranking.Profesor'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0004_curso_escuela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictado',
            name='conocimiento',
        ),
        migrations.RemoveField(
            model_name='dictado',
            name='exigencia',
        ),
        migrations.RemoveField(
            model_name='dictado',
            name='pasabilidad',
        ),
        migrations.RemoveField(
            model_name='dictado',
            name='pedagogia',
        ),
        migrations.AddField(
            model_name='comentario',
            name='conocimiento',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='exigencia',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='pasabilidad',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='pedagogia',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictado',
            name='conocimientoP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictado',
            name='exigenciaP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictado',
            name='pasabilidadP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dictado',
            name='pedagogiaP',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]

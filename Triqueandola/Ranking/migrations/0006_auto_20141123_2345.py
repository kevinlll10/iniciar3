# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0005_auto_20141122_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictado',
            name='puntajeP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profesor',
            name='puntajeP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dictado',
            name='conocimientoP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dictado',
            name='exigenciaP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dictado',
            name='pasabilidadP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dictado',
            name='pedagogiaP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='conocimientoP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='exigenciaP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='pasabilidadP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profesor',
            name='pedagogiaP',
            field=models.DecimalField(default=0, max_digits=4, decimal_places=2),
            preserve_default=True,
        ),
    ]

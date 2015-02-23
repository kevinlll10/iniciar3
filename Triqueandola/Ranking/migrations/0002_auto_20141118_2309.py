# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursodictado',
            name='profesor',
        ),
        migrations.AddField(
            model_name='cursodictado',
            name='profesores',
            field=models.ManyToManyField(to='Ranking.Profesor'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0003_auto_20141120_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='escuela',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0006_auto_20141123_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dictado',
            name='semestre',
        ),
    ]

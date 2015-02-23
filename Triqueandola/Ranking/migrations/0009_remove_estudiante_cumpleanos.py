# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ranking', '0008_auto_20141126_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='cumpleanos',
        ),
    ]

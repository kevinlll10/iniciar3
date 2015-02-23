# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ranking', '0007_remove_dictado_semestre'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='cumpleanos',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='curso',
            name='escuela',
            field=models.CharField(default=b' ', max_length=20),
            preserve_default=True,
        ),
    ]

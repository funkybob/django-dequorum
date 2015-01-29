# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dequorum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='tags',
            field=models.ManyToManyField(to='dequorum.Tag', blank=True),
            preserve_default=True,
        ),
    ]

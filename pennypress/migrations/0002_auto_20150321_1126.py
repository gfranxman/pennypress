# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pennypress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='last_bad_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='last_good_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pennypress', '0003_auto_20150314_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=4, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='point',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=4, blank=True),
            preserve_default=True,
        ),
    ]

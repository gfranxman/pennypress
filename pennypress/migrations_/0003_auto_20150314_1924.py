# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pennypress', '0002_auto_20150314_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='one_off_dateline',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='park',
            name='name',
            field=models.CharField(default='was null', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='park',
            name='sports',
            field=models.ManyToManyField(to='pennypress.Sport', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='pennypress.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='sports',
            field=models.ManyToManyField(to='pennypress.Sport', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sport',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(to='pennypress.Tag', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.ManyToManyField(to='pennypress.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]

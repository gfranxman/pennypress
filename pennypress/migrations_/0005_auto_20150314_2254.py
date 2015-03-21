# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import multiselectfield.db.fields
from django.conf import settings
import pennypress.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pennypress', '0004_auto_20150314_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('live', models.NullBooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='pennypress_eventtype_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_eventtype_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('live', models.NullBooleanField(default=True)),
                ('created_by', models.ForeignKey(related_name='pennypress_nav_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(blank=True, to='pennypress.Nav', null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_nav_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'addresses'},
        ),
        migrations.AlterModelOptions(
            name='church',
            options={'verbose_name_plural': 'churches'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name_plural': 'counties'},
        ),
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'stories'},
        ),
        migrations.RemoveField(
            model_name='church',
            name='organization_ptr',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='address_ptr',
        ),
        migrations.RemoveField(
            model_name='park',
            name='address_ptr',
        ),
        migrations.RemoveField(
            model_name='place',
            name='point_ptr',
        ),
        migrations.RemoveField(
            model_name='school',
            name='organization_ptr',
        ),
        migrations.AddField(
            model_name='church',
            name='address',
            field=models.ForeignKey(blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_church_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 51, 42, 897008, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='church',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='church',
            name='name',
            field=models.CharField(default='defult', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='church',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_church_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='church',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 52, 46, 499925, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventtypes',
            field=multiselectfield.db.fields.MultiSelectField(default=[1], max_length=200, verbose_name=pennypress.models.EventType),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='eventtypes',
            field=multiselectfield.db.fields.MultiSelectField(default=[1], max_length=200, verbose_name=pennypress.models.EventType),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.ForeignKey(blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_organization_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 53, 29, 222487, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_organization_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 53, 39, 713310, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='address',
            field=models.ForeignKey(blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='park',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_park_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='park',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 53, 46, 133967, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='park',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_park_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='park',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 54, 5, 797396, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_place_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 54, 10, 356591, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='point',
            field=models.ForeignKey(default=1, to='pennypress.Point'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_place_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 54, 28, 579913, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.ForeignKey(blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_school_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 54, 33, 389927, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='name',
            field=models.CharField(default='scool', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_school_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 15, 2, 54, 51, 757563, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zipcode',
            name='point',
            field=models.ForeignKey(blank=True, to='pennypress.Point', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='point',
            unique_together=set([('latitude', 'longitude')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(related_name='pennypress_county_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_county_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dateline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('starts', models.DateTimeField()),
                ('ends', models.DateTimeField(null=True, blank=True)),
                ('one_off_address', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(verbose_name=b'name')),
                ('description', models.TextField(null=True, blank=True)),
                ('one_off_address', models.TextField(null=True, blank=True)),
                ('start_time', models.TimeField(null=True, blank=True)),
                ('duration', models.DecimalField(help_text=b'Hours', max_digits=5, decimal_places=2)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('repeat_expression', models.CharField(help_text=b'Use the days of the Week or other expressions like:\n        weekly style:\n            Monday\n            Monday, Wednesday, Friday\n        monthly style:\n            first Sunday\n            last friday\n            biweekly wednesdays\n    ', max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('alt_text', models.CharField(max_length=200, null=True, blank=True)),
                ('target', models.CharField(blank=True, max_length=50, null=True, choices=[(b'_blank', b'New Window'), (b'', b'Same Window')])),
                ('created_by', models.ForeignKey(related_name='pennypress_link_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_link_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('subtitle', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'')),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='pennypress_photo_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('latitude', models.DecimalField(max_digits=7, decimal_places=4)),
                ('longitude', models.DecimalField(max_digits=7, decimal_places=4)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('point_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Point')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.point',),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('place_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Place')),
                ('addr1', models.CharField(max_length=100, null=True, blank=True)),
                ('addr2', models.CharField(max_length=100, null=True, blank=True)),
                ('one_off_city', models.CharField(max_length=100)),
                ('one_off_state', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.place',),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Address')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.address',),
        ),
        migrations.CreateModel(
            name='Church',
            fields=[
                ('organization_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Organization')),
                ('denomination', models.CharField(blank=True, max_length=20, null=True, choices=[(b'christian', b'Christian'), (b'satanic', b'Satanic')])),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.organization',),
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Address')),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.address',),
        ),
        migrations.CreateModel(
            name='PollingStation',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Address')),
                ('hours', models.TextField()),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.address',),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('organization_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pennypress.Organization')),
                ('grades', multiselectfield.db.fields.MultiSelectField(max_length=55, choices=[(-1, b'Pre-K'), (0, b'Kindergarten'), (1, b'First Grade'), (2, b'Second Grade'), (3, b'Third Grade'), (4, b'Fourth Grade'), (5, b'Fifth Grade'), (6, b'Sixth Grade'), (7, b'Seventh Grade'), (8, b'Eight Grade'), (9, b'HS Freshman'), (10, b'HS Sophomore'), (11, b'HS Junior'), (12, b'HS Senior Grade'), (13, b'Freshman'), (14, b'Sophomore'), (15, b'Junior'), (16, b'Senior'), (17, b'Associates'), (18, b'Bachellors'), (19, b'Masters'), (20, b'Doctorate')])),
            ],
            options={
                'abstract': False,
            },
            bases=('pennypress.organization',),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('external_rss_source', models.URLField(help_text=b'Links come from this source.', null=True, blank=True)),
                ('external_page', models.URLField(help_text=b'Links to this section will redirect to this url.', null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='pennypress_section_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(verbose_name=b'name')),
                ('created_by', models.ForeignKey(related_name='pennypress_sport_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_sport_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('abbr', models.CharField(max_length=10)),
                ('created_by', models.ForeignKey(related_name='pennypress_state_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_state_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('subtitle', models.CharField(max_length=200)),
                ('tease', models.TextField(max_length=200, null=True, blank=True)),
                ('body', models.TextField(max_length=10000, null=True, blank=True)),
                ('footer', models.TextField(max_length=200, null=True, blank=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='pennypress_story_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('dateline', models.ForeignKey(blank=True, to='pennypress.Dateline', null=True)),
                ('lead_photo', models.ForeignKey(blank=True, to='pennypress.Photo', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('slug', models.SlugField()),
                ('created_by', models.ForeignKey(related_name='pennypress_tag_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(blank=True, to='pennypress.Tag', null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_tag_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('subtitle', models.CharField(max_length=200)),
                ('video', models.URLField()),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='pennypress_video_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('photo', models.ForeignKey(blank=True, to='pennypress.Photo', null=True)),
                ('tags', models.ManyToManyField(to='pennypress.Tag')),
                ('updated_by', models.ForeignKey(related_name='pennypress_video_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('city', models.ForeignKey(to='pennypress.City')),
                ('created_by', models.ForeignKey(related_name='pennypress_zipcode_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('updated_by', models.ForeignKey(related_name='pennypress_zipcode_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='story',
            name='tags',
            field=models.ManyToManyField(to='pennypress.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_story_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='excluded_tags',
            field=models.ManyToManyField(related_name='excluded_from', to='pennypress.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='included_tags',
            field=models.ManyToManyField(related_name='included_in', to='pennypress.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='section',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_section_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='sports',
            field=models.ManyToManyField(to='pennypress.Sport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='point',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_point_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='point',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_point_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(to='pennypress.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='photo',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_photo_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='park',
            name='sports',
            field=models.ManyToManyField(to='pennypress.Sport'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='address',
            field=models.ForeignKey(related_name='eventtemplates_for_this_address', blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_eventtemplate_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='organization',
            field=models.ForeignKey(related_name='eventtemplates', blank=True, to='pennypress.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventtemplate',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_eventtemplate_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.ForeignKey(related_name='events_at_this_address', blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_event_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='eventtemplate',
            field=models.ForeignKey(blank=True, to='pennypress.EventTemplate', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='organization',
            field=models.ForeignKey(related_name='events', blank=True, to='pennypress.Organization', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_event_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dateline',
            name='address',
            field=models.ForeignKey(blank=True, to='pennypress.Address', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dateline',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_dateline_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dateline',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_dateline_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='county',
            field=models.ForeignKey(to='pennypress.County'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='created_by',
            field=models.ForeignKey(related_name='pennypress_city_creator', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(to='pennypress.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='updated_by',
            field=models.ForeignKey(related_name='pennypress_city_updater', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='zipcode',
            field=models.ForeignKey(to='pennypress.ZipCode'),
            preserve_default=True,
        ),
    ]

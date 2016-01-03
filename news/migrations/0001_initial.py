# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields
import filer.fields.image
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.CharField(unique=True, max_length=100)),
                ('publication_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('text', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', on_delete=django.db.models.deletion.SET_NULL, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'news',
            },
        ),
    ]

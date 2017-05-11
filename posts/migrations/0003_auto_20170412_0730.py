# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170411_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]

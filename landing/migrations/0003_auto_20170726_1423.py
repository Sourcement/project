# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20170726_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0002_auto_20180320_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrestdata',
            name='ARRESTLOCATION',
            field=models.TextField(),
        ),
    ]

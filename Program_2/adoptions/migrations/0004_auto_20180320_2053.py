# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-21 00:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0003_auto_20180320_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrestdata',
            name='AGE',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='ARRESTLOCATION',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='ARRESTTIME',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='CCR',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='COUNCIL_DISTRICT',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='GENDER',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='INCIDENTLOCATION',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='INCIDENTNEIGHBORHOOD',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='INCIDENTTRACT',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='INCIDENTZONE',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='OFFENSES',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='PUBLIC_WORKS_DIVISION',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='RACE',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='X',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='Y',
        ),
        migrations.RemoveField(
            model_name='arrestdata',
            name='_id',
        ),
    ]
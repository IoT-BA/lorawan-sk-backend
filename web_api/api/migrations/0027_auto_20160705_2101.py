# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_rawpoint_node'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20160821_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='rawpoint',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Rawpoint'),
        ),
    ]

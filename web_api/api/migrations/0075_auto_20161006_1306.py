# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-06 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0074_node_lorawan_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='lorawan_band',
        ),
        migrations.AddField(
            model_name='gateway',
            name='lorawan_band',
            field=models.IntegerField(blank=True, choices=[(0, b'EU863-870'), (1, b'US902-928'), (2, b'CN779-787')], null=True),
        ),
    ]

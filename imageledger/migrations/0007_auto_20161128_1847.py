# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageledger', '0006_image_last_synced_with_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='last_synced_with_source',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]

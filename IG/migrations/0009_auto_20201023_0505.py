# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-23 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IG', '0008_auto_20201022_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='owner',
            new_name='user',
        ),
    ]

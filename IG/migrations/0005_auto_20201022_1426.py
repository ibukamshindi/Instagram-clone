# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-22 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IG', '0004_auto_20201019_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='owner',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 13:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20180117_1906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerprofile',
            old_name='user',
            new_name='seller',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhairdressings', '0006_remove_adminhairdressing_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminHairdressing',
            new_name='Hairdressing',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhairdressings', '0005_adminhairdressing_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminhairdressing',
            name='image',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhairdressings', '0007_auto_20160502_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairdressing',
            name='image',
            field=models.FileField(default=1, upload_to=b'myhairdressings/static/img'),
            preserve_default=False,
        ),
    ]

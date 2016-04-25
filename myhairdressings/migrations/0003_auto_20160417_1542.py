# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhairdressings', '0002_auto_20160417_1538'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hairdressing',
            new_name='AdminHairDressing',
        ),
    ]

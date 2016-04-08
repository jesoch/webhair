# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminHairDressing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('url', models.URLField(blank=True, null=True)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('street', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('city', models.TextField(default='')),
                ('zipcode', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(max_length=9)),
                ('schedule', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=8, verbose_name='Euro amount', decimal_places=2, blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

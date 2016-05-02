# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myhairdressings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hairdresser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('speciality', models.TextField(max_length=100, help_text=' Redacta les teves funcionalitats')),
            ],
        ),
        migrations.CreateModel(
            name='Hairdressing',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('zipcode', models.TextField(null=True, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('description', models.TextField(help_text='Descriu informació necessaria de la perruqueria')),
                ('url', models.URLField(null=True, blank=True)),
                ('publish_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('day', models.PositiveSmallIntegerField(default=1, choices=[(1, 'Lunes'), (2, 'Martes'), (3, 'Miercoles'), (4, 'Jueves'), (5, 'Viernes'), (6, 'Sabado')], verbose_name='Día')),
                ('hour', models.PositiveSmallIntegerField(default=1, choices=[(9, '09:00h'), (10, '10:00h'), (11, '11:00h'), (12, '12:00h'), (13, '13:00h'), (14, '14:00h'), (15, '15:00h'), (16, '16:00h'), (17, '17:00h'), (18, '18:00h'), (19, '19:00h'), (20, '20:00h')], verbose_name='Hora')),
                ('hairdresser', models.ForeignKey(to='myhairdressings.Hairdresser', related_name='schedule')),
            ],
        ),
        migrations.RemoveField(
            model_name='adminhairdressing',
            name='user',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdminHairdressing',
        ),
        migrations.DeleteModel(
            name='client',
        ),
        migrations.AddField(
            model_name='hairdresser',
            name='hairdressing',
            field=models.ForeignKey(to='myhairdressings.Hairdressing', related_name='hairdressers'),
        ),
        migrations.AddField(
            model_name='citation',
            name='id_schedule',
            field=models.ForeignKey(to='myhairdressings.Schedule', related_name='citation'),
        ),
        migrations.AddField(
            model_name='citation',
            name='id_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='citation'),
        ),
    ]

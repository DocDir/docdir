# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_auto_20150722_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp record created', null=True),
        ),
        migrations.AddField(
            model_name='datasource',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp record created', null=True),
        ),
        migrations.AddField(
            model_name='insurer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp record created', null=True),
        ),
        migrations.AddField(
            model_name='plan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp record created', null=True),
        ),
        migrations.AddField(
            model_name='specialty',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp record created', null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='rip',
            field=models.BooleanField(help_text='whether the doctor is alive', default=False),
        ),
    ]

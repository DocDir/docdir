# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='organization name')),
                ('source_type', models.CharField(max_length=1, choices=[('C', 'Crawled'), ('V', 'Official Release csv'), ('P', 'Official Release pdf')])),
                ('notes', models.CharField(help_text='assorted notes re: data source', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='timestamp record created'),
        ),
        migrations.AddField(
            model_name='contract',
            name='score',
            field=models.FloatField(default=1.0, verbose_name='data reliability score'),
        ),
        migrations.AddField(
            model_name='doctorcontact',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='timestamp record created'),
        ),
        migrations.AddField(
            model_name='doctorcontact',
            name='score',
            field=models.FloatField(default=1.0, verbose_name='data reliability score'),
        ),
        migrations.AddField(
            model_name='doctorspecialty',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='timestamp record created'),
        ),
        migrations.AddField(
            model_name='doctorspecialty',
            name='score',
            field=models.FloatField(default=1.0, verbose_name='data reliability score'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='start',
            field=models.DateTimeField(null=True, default=None),
        ),
        migrations.AlterField(
            model_name='doctorcontact',
            name='start',
            field=models.DateTimeField(null=True, default=None),
        ),
        migrations.AlterField(
            model_name='doctorspecialty',
            name='start',
            field=models.DateTimeField(null=True, default=None),
        ),
        migrations.AddField(
            model_name='contract',
            name='source',
            field=models.ForeignKey(help_text='where relationship data comes from', to='plans.DataSource', default=None, null=True),
        ),
        migrations.AddField(
            model_name='doctorcontact',
            name='source',
            field=models.ForeignKey(help_text='where relationship data comes from', to='plans.DataSource', default=None, null=True),
        ),
        migrations.AddField(
            model_name='doctorspecialty',
            name='source',
            field=models.ForeignKey(help_text='where relationship data comes from', to='plans.DataSource', default=None, null=True),
        ),
    ]

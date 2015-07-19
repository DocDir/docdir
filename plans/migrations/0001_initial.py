# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=1, verbose_name='the phone #', blank=True)),
                ('address', models.TextField(verbose_name='the address')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(default=None, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rip', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(default=None, null=True)),
                ('active', models.BooleanField(verbose_name="if the doc's contact is active", default=True)),
                ('contact', models.ForeignKey(to='plans.Contact')),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(default=None, null=True)),
                ('active', models.BooleanField(verbose_name="if the doc's specialty is active", default=True)),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, help_text='the name of the insurer', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, help_text='the name of the plan')),
                ('insurer', models.ForeignKey(help_text='the insurer who operates the plan', verbose_name='operating insurer', to='plans.Insurer')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='doctorspecialty',
            name='specialty',
            field=models.ForeignKey(to='plans.Specialty'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='contacts',
            field=models.ManyToManyField(verbose_name="doctor's contacts", through='plans.DoctorContact', to='plans.Contact'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='plans',
            field=models.ManyToManyField(verbose_name="doctor's plans", through='plans.Contract', to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(verbose_name="doctor's specialties", through='plans.DoctorSpecialty', to='plans.Specialty'),
        ),
        migrations.AddField(
            model_name='contract',
            name='doctor',
            field=models.ForeignKey(to='plans.Doctor'),
        ),
        migrations.AddField(
            model_name='contract',
            name='plan',
            field=models.ForeignKey(to='plans.Plan'),
        ),
    ]

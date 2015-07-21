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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=16, verbose_name='the phone #', blank=True)),
                ('address', models.TextField(verbose_name='the address', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True, default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rip', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True, default=None)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True, default=None)),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the insurer', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the plan', max_length=200)),
                ('insurer', models.ForeignKey(verbose_name='operating insurer', help_text='the insurer who operates the plan', to='plans.Insurer')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            field=models.ManyToManyField(to='plans.Contact', through='plans.DoctorContact', verbose_name="doctor's contacts"),
        ),
        migrations.AddField(
            model_name='doctor',
            name='plans',
            field=models.ManyToManyField(to='plans.Plan', through='plans.Contract', verbose_name="doctor's plans"),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(to='plans.Specialty', through='plans.DoctorSpecialty', verbose_name="doctor's specialties"),
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

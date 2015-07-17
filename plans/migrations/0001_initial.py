# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [('plans', '0001_initial'), ('plans', '0002_auto_20150717_0313')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, verbose_name='the phone #', max_length=1)),
                ('address', models.TextField(verbose_name='the address')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name="if the doc's contact is active", default=True)),
                ('contact', models.ForeignKey(to='plans.Contact')),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name="if the doc's specialty is active", default=True)),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text='the name of the insurer', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text='the name of the plan')),
                ('insurer', models.ForeignKey(to='plans.Insurer', help_text='the insurer who operates the plan', verbose_name='operating insurer')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
            field=models.ManyToManyField(through='plans.DoctorContact', verbose_name="doctor's contacts", to='plans.Contact'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='plans',
            field=models.ManyToManyField(through='plans.Contract', verbose_name="doctor's plans", to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(through='plans.DoctorSpecialty', verbose_name="doctor's specialties", to='plans.Specialty'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(verbose_name="if the doc's contract is active", default=True)),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
                ('plan', models.ForeignKey(to='plans.Plan')),
            ],
        ),
    ]

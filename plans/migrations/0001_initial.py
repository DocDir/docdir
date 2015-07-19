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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(verbose_name='the phone #', max_length=1, blank=True)),
                ('address', models.TextField(verbose_name='the address')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name="if the doc's contract is active")),
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
                ('active', models.BooleanField(default=True, verbose_name="if the doc's contact is active")),
                ('contact', models.ForeignKey(to='plans.Contact')),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name="if the doc's specialty is active")),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the insurer', unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the plan', max_length=200)),
                ('insurer', models.ForeignKey(help_text='the insurer who operates the plan', to='plans.Insurer', verbose_name='operating insurer')),
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
            field=models.ManyToManyField(through='plans.DoctorContact', to='plans.Contact', verbose_name="doctor's contacts"),
        ),
        migrations.AddField(
            model_name='doctor',
            name='plans',
            field=models.ManyToManyField(through='plans.Contract', to='plans.Plan', verbose_name="doctor's plans"),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(through='plans.DoctorSpecialty', to='plans.Specialty', verbose_name="doctor's specialties"),
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

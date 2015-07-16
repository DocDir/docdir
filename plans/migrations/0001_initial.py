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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, verbose_name='the phone #', max_length=1)),
                ('address', models.TextField(verbose_name='the address')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name="if the doc's contact is active")),
                ('contact', models.ForeignKey(to='plans.Contact')),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSpecialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name="if the doc's specialty is active")),
                ('doctor', models.ForeignKey(to='plans.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Insurer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, help_text='the name of the insurer', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(help_text='the name of the plan', max_length=200)),
                ('insurer', models.ForeignKey(verbose_name='operating insurer', help_text='the insurer who operates the plan', to='plans.Insurer')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
            field=models.ManyToManyField(verbose_name="doctor's plans", to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(through='plans.DoctorSpecialty', verbose_name="doctor's specialties", to='plans.Specialty'),
        ),
    ]

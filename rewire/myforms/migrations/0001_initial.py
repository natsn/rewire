# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GreenSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('supervisor_name', models.CharField(max_length=255)),
                ('ee_num', models.CharField(max_length=255)),
                ('aep_status_type', models.IntegerField(choices=[(1, 'Regular'), (2, 'On Call'), (3, 'Temp (six months'), (4, 'Work Study'), (5, 'Intern')])),
                ('aep_period_type', models.IntegerField(choices=[(1, 'Monthly'), (2, 'Hourly')])),
                ('aep_hire_type', models.IntegerField(choices=[(1, 'New Hire'), (2, 'Rehire')])),
                ('aep_amount_time', models.FloatField()),
                ('aep_pay_rate', models.FloatField()),
                ('aep_start_date', models.DateField()),
                ('prc_payroll_change_type', models.IntegerField(choices=[(1, 'Increase'), (2, 'Promotion'), (3, 'Change of Status'), (4, 'Change of FTE / # Hours'), (5, 'Change of Supervisor')])),
                ('prc_change_from', models.CharField(max_length=255)),
                ('prc_change_to', models.CharField(max_length=255)),
                ('prc_effective_date', models.DateField()),
                ('prc_comments', models.CharField(max_length=1024)),
                ('es_effective_date', models.DateField()),
                ('es_voluntary_type', models.IntegerField(choices=[(1, 'Voluntary Seperation'), (2, 'Involuntary Seperation')])),
                ('es_from_type', models.IntegerField(choices=[(1, 'Voluntary Seperation'), (2, 'Involuntary Seperation')])),
                ('general_comments', models.CharField(max_length=1024)),
                ('approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('phase', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='greensheet',
            name='projects_to_charge',
            field=models.ManyToManyField(to='myforms.Project'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 13:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInformationSystem', '0003_acedamicinfo_additionalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TPOId', models.CharField(max_length=30)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.IntegerField(max_length=2)),
                ('drivedetails', models.TextField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyId', models.CharField(max_length=30)),
                ('date', models.DateTimeField(max_length=30)),
                ('status', models.IntegerField(max_length=2)),
                ('suggestion', models.CharField(max_length=70)),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentInformationSystem.PersonalInfo')),
            ],
        ),
    ]

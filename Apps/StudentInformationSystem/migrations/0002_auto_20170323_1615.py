# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInformationSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollNo', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.TextField(max_length=70)),
                ('email', models.EmailField(max_length=30)),
                ('phoneNo', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='acedamicinfo',
            name='studentId',
        ),
        migrations.RemoveField(
            model_name='additionalinfo',
            name='studentId',
        ),
        migrations.RemoveField(
            model_name='notifications',
            name='driveName',
        ),
        migrations.DeleteModel(
            name='AcedamicInfo',
        ),
        migrations.DeleteModel(
            name='AdditionalInfo',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.DeleteModel(
            name='PersonInfo',
        ),
    ]

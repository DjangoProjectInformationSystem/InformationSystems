# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StudentInformationSystem', '0004_notifications_suggestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='status',
        ),
        migrations.RemoveField(
            model_name='suggestion',
            name='status',
        ),
    ]

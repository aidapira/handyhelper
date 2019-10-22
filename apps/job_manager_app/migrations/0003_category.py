# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-22 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_manager_app', '0002_job_isadded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.ManyToManyField(related_name='categories', to='job_manager_app.Job')),
            ],
        ),
    ]
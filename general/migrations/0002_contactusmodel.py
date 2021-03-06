# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-06 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('mob_no', models.CharField(max_length=12)),
                ('subject', models.CharField(choices=[('I Would Like To Discuss', 'I Would Like To Discuss'), ('I Would Like To Know About', 'I Would Like To Know About'), ('I Would Like To Suggest', 'I Would Like To Suggest')], max_length=100)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('SerialNumber', models.CharField(max_length=15)),
                ('Price', models.FloatField()),
                ('DOA', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Depreciation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class', models.CharField(max_length=5)),
                ('Rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='assets',
            name='Assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depreciation.Users'),
        ),
        migrations.AddField(
            model_name='assets',
            name='DepClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depreciation.Depreciation'),
        ),
    ]

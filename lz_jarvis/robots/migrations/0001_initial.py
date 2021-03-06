# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-13 00:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RSeoStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=100)),
                ('google', models.BooleanField(default=False)),
                ('yahoo', models.BooleanField(default=False)),
                ('bing', models.BooleanField(default=False)),
                ('duckduck', models.BooleanField(default=False)),
                ('destination', models.TextField(default='pruebadajngo@gmail.com')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rseostatus', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TaskRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(editable=False, max_length=200, unique=True)),
                ('status', models.CharField(choices=[('STARTED', 'started'), ('PENDING', 'pending')], default='PENDING', max_length=50)),
                ('task_environment', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]

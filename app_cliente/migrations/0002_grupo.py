# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('clientes', models.ManyToManyField(to='app_cliente.Cliente')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dias_jornada',
            field=models.CharField(choices=[('SEGUNDA', b'SEGUNDA'), ('TERCA', b'TERCA'), ('QUARTA', b'QUARTA'), ('QUINTA', b'QUINTA'), ('SEXTA', b'SEXTA'), ('SABADO', b'SABADO'), ('DOMINGO', b'DOMINGO')], max_length=150),
        ),
    ]

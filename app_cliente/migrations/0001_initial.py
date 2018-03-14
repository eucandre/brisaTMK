# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-11 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_usuario', '0003_auto_20180301_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(max_length=150)),
                ('cpf_cnpj', models.CharField(max_length=23, unique=True)),
                ('porte_cliente', models.CharField(choices=[('PEQUENO', 'PEQUENO'), ('MEDIO', 'MEDIO'), ('GRANDE', 'GRANDE')], max_length=8)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('contato', models.CharField(help_text='Pessoa que deve responder pelo cliente', max_length=150)),
                ('cargo_contato', models.CharField(max_length=150)),
                ('endereco', models.CharField(blank=True, max_length=150, null=True)),
                ('observacoes', models.TextField()),
                ('imagem_loja', models.FileField(upload_to='loja_clientes/%Y/%m/%d/')),
                ('colaborador_responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_usuario.Usuario')),
            ],
            options={
                'verbose_name_plural': 'CLientes do nosso Sistema',
            },
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='segmento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_cliente.Segmento'),
        ),
    ]

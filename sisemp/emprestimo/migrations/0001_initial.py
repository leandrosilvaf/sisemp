# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data_emprestimo', models.DateTimeField(verbose_name='Data de Empréstimo', auto_now_add=True)),
                ('prazo_devolucao', models.DateTimeField(verbose_name='Prazo para Devolução', null=True)),
                ('data_devolucao', models.DateTimeField(verbose_name='Data de Devolução', null=True)),
                ('devolvido', models.BooleanField(default=False)),
                ('funcionario_devolucao', models.ForeignKey(null=True, related_name='emprestimo_devolucao', to=settings.AUTH_USER_MODEL)),
                ('funcionario_emprestimo', models.ForeignKey(null=True, related_name='emprestimo_emprestimo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('tombo', models.IntegerField(primary_key=True, max_length=10, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('numeroserie', models.CharField(verbose_name='Número de Série', max_length=30, null=True)),
                ('categoria', models.CharField(max_length=50, choices=[('topografico', 'Topográfico'), ('audio', 'Áudio'), ('video', 'Vídeo'), ('foto', 'Fotografia'), ('info', 'Informática'), ('museu', 'Museologia')])),
                ('disponivel', models.BooleanField(default=True)),
                ('observacoes', models.TextField(verbose_name='Observações', max_length=300, blank=True)),
                ('ultimo_inventario', models.DateField(verbose_name='Data do último inventário', null=True)),
            ],
            options={
                'ordering': ('nome', 'tombo'),
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('matricula', models.IntegerField(primary_key=True, max_length=9, serialize=False)),
                ('categoria', models.CharField(max_length=50, choices=[('Estudante', (('agrimensura', 'Engenharia de Agrimensura e Cartográfica'), ('transporte', 'Tecnologia em Transporte Terrestre'), ('civil', 'Engenharia Civil'), ('ambiental', 'Engenharia Ambiental'), ('geografia', 'Geografia'), ('interdisciplinar', 'Bacharelado Interdisciplinar'))), ('professor', 'Professor'), ('tecnico', 'Técnico Administrativo')])),
                ('email', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField(verbose_name='Endereço', max_length=200)),
                ('suspensao', models.DateField(verbose_name='Suspenso até', null=True, default=datetime.date(2010, 9, 7))),
                ('disponivel', models.BooleanField(default=True)),
                ('observacoes', models.TextField(verbose_name='Observações', max_length=300, blank=True)),
                ('atualizacao_cadastral', models.DateField(verbose_name='Última atualização de cadastro', auto_now_add=True)),
            ],
            options={
                'ordering': ('nome',),
            },
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='itens',
            field=models.ManyToManyField(to='emprestimo.Equipamento'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(to='emprestimo.Usuario'),
        ),
    ]

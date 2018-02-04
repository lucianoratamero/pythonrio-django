# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180204_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='agenda',
            field=markdownx.models.MarkdownxField(default='Hora | Local | Atividade\n--- | --- | ---\n13:30|Recepção|Credenciamento\n13:55||Abertura\n14:00||\n14:50||\n15:40||\n16:00||\n16:30||\n17:00||\n17:50||Encerramento\n18:00|No bar mais próximo, vamos trocar ideias e beber um chopp.|Pós-evento'),
        ),
        migrations.AddField(
            model_name='evento',
            name='endereço',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
    ]
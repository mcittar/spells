# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spell',
            name='school',
            field=models.CharField(choices=[('A', 'Abjuration'), ('C', 'Conjuration'), ('D', 'Divination'), ('E', 'Enchantment'), ('EV', 'Evocation'), ('I', 'Illusion'), ('N', 'Necromancy'), ('T', 'Transmutation')], default='EV', max_length=2),
        ),
    ]

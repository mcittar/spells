# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(choices=[('Abjuration', 'Abjuration'), ('Conjuration', 'Conjuration'), ('Divination', 'Divination'), ('Enchantment', 'Enchantment'), ('Evocation', 'Evocation'), ('Illusion', 'Illusion'), ('Necromancy', 'Necromancy'), ('Transmutation', 'Transmutation')], max_length=20),
        ),
    ]

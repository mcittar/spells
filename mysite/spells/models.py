# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Spell(models.Model):
    ABJURATION = 'A'
    CONJURATION = 'C'
    DIVINATION = 'D'
    ENCHANTMENT = 'E'
    EVOCATION = 'EV'
    ILLUSION = 'I'
    NECROMANCY = 'N'
    TRANSMUTATION = 'T'
    SPELL_SCHOOL_CHOICES = (
        (ABJURATION, 'Abjuration'),
        (CONJURATION, 'Conjuration'),
        (DIVINATION, 'Divination'),
        (ENCHANTMENT, 'Enchantment'),
        (EVOCATION, 'Evocation'),
        (ILLUSION, 'Illusion'),
        (NECROMANCY, 'Necromancy'),
        (TRANSMUTATION, 'Transmutation')
    )

    name = models.CharField(max_length = 100, unique = True)
    level = models.IntegerField(default = 0)
    school = models.CharField(
        max_length = 2,
        choices = SPELL_SCHOOL_CHOICES,
        default = EVOCATION,
    )
    casting_time = models.CharField(max_length = 200)
    range = models.CharField(max_length = 50)
    components = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    classes = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

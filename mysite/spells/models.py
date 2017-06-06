# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
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

    name = models.CharField(
        max_length = 2,
        choices = SPELL_SCHOOL_CHOICES
    )

class Class(models.Model):
    ANCIENTS = 'Paladin (Ancients)',
    ARCANA = 'Cleric (Arcana)',
    ARCHFEY = 'Warlock (Archfey)',
    ARCTIC = 'Druid (Arctic)',
    ARTIFICIER = 'Artificier',
    BARBARIAN = 'Barbarian',
    BARD = 'Bard',
    CLERIC = 'Cleric',
    COAST = 'Druid (Coast)',
    CROWN = 'Paladin (Crown)',
    DEATH = 'Cleric (Death)',
    DESERT = 'Druid (Desert)',
    DEVOTION = 'Paladin (Devotion)',
    DRUID = 'Druid',
    ELDRITCH = 'Fighter (Eldritch Knight)',
    FIEND = 'Warlock (Fiend)',
    FIGHTER = 'Fighter',
    FOREST = 'Druid (Forest)',
    GOO = 'Warlock (Great Old One)',
    GRASSLAND = 'Druid (Grassland)',
    KNOWLEDGE = 'Cleric (Knowledge)',
    LIFE = 'Cleric (Life)',
    LIGHT = 'Cleric (Light)',
    NATURE = 'Cleric (Nature)',
    OATHBREAKER = 'Paladin (Oathbreaker)',
    PALADIN = 'Paladin',
    RANGER = 'Ranger',
    ROGUE = 'Rogue',
    SORCERER = 'Sorcerer',
    SWAMP = 'Cleric (Swamp)',
    TEMPEST = 'Cleric (Tempest)',
    TRICKERY = 'Cleric (Trickery)',
    TRICKSTER = 'Rogue (Arcane Trickster)',
    UNDERDARK = 'Druid (Underdark)',
    UNDYING = 'Warlock (Undying Light)',
    VENGEANCE = 'Paladin (Vengeance)',
    WAR = 'Cleric (War)',
    WARLOCK = 'Warlock',
    WIZARD = 'Wizard'
    SPELL_CLASS_CHOICES = (
        (ANCIENTS, 'Paladin (Ancients)'),
        (ARCANA,'Cleric (Arcana)'),
        (ARCHFEY, 'Warlock (Archfey)'),
        (ARCTIC, 'Druid (Arctic)'),
        (ARTIFICIER, 'Artificier'),
        (BARBARIAN, 'Barbarian'),
        (BARD, 'Bard'),
        (CLERIC, 'Cleric'),
        (COAST, 'Druid (Coast)'),
        (CROWN, 'Cleric (Crown)'),
        (DEATH, 'Cleric (Death)'),
        (DESERT, 'Druid (Desert)'),
        (DEVOTION, 'Paladin (Devotion)'),
        (DRUID, 'Druid'),
        (ELDRITCH, 'Fighter (Eldritch Knight)'),
        (FIEND, 'Warlock (Fiend)'),
        (FIGHTER, 'FIghter'),
        (FOREST, 'Druid (Forest)'),
        (GOO, 'Warlock (Great Old One)'),
        (GRASSLAND, 'Druid (Grassland)'),
        (NATURE, 'Cleric (Nature)'),
        (KNOWLEDGE, 'Cleric (Knowledge)'),
        (LIFE, 'Cleric (Life)'),
        (LIGHT, 'Cleric (Light)'),
        (OATHBREAKER, 'Paladin (Oathbreaker)'),
        (PALADIN, 'Paladin'),
        (RANGER, 'Ranger'),
        (ROGUE, 'Rogue'),
        (SORCERER, 'Sorcerer'),
        (SWAMP, 'Cleric (Swamp)'),
        (TEMPEST, 'Cleric (Tempest)'),
        (TRICKERY, 'Cleric (Trickery)'),
        (TRICKSTER, 'Rogue (Arcane Trickster)'),
        (UNDERDARK, 'Druid (Underdark)'),
        (UNDYING, 'Warlock (Undying)'),
        (VENGEANCE, 'Paladin (Vengeance)'),
        (WAR, 'Cleric (War)'),
        (WARLOCK, 'Warlock'),
        (WIZARD, 'Wizard')
    )

    name = models.CharField(
        max_length = 20,
        choices = SPELL_CLASS_CHOICES
    )

class Spell(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    level = models.IntegerField(default = 0)
    school = models.ForeignKey(School, on_delete = models.CASCADE)
    casting_time = models.CharField(max_length = 200)
    range = models.CharField(max_length = 50)
    components = models.CharField(max_length = 100)
    duration = models.CharField(max_length = 100)
    classes = models.ForeignKey(Class, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

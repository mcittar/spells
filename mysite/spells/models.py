# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Spell(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name

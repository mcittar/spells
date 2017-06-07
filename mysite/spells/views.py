# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Spell

# Create your views here.
def index(request):
    latest_spell_list = Spell.objects.order_by('level')[:5]

    return HttpResponse("hello")

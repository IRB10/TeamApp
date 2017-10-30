# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Sportovi, Destinacije, Uloge, Tereni, Termini
from django.contrib import admin

# Register your models here.
admin.site.register(Sportovi)
admin.site.register(Destinacije)
admin.site.register(Uloge)
admin.site.register(Tereni)
admin.site.register(Termini)

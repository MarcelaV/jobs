# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ofertas.models import Empresa, DescripcionCargo, Requisito

admin.site.register(Empresa)
admin.site.register(DescripcionCargo)
admin.site.register(Requisito)

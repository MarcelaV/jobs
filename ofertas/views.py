# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from ofertas.models import Empresa, DescripcionCargo

import ofertas


def home(request):
    cargos = DescripcionCargo.objects.all()
    empresas = Empresa.objects.all()
    context = {
        'descripcion_list': cargos,
        'empresas': empresas
    }
    return render(request, 'ofertas/home.html', context)
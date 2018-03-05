# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from ofertas.models import Empresa, DescripcionCargo, ACTIVA




def home(request):
    cargos = DescripcionCargo.objects.filter(estado_publicacion=ACTIVA).order_by('-id')
    empresas = Empresa.objects.all()
    context = {
        'descripcion_list': cargos[:10],
        'empresas': empresas
    }
    return render(request, 'ofertas/home.html', context)


def detail(request, pk):
    ofertas_list = DescripcionCargo.objects.filter(pk=pk)
    ofertas_detail = ofertas_list[0] if len(ofertas_list) >= 1 else None
    if ofertas_detail is not None:
        #plantilla
        context = {
            'ofertas_detail': ofertas_detail
        }
        return render(request, 'ofertas/detail.html', context)
    else:
        return HttpResponseNotFound("No existe")
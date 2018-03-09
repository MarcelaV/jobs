# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View
from ofertas.forms import OfertaForm, PostularForm
from ofertas.models import Empresa, DescripcionCargo, ACTIVA
from django.utils.decorators import method_decorator

from ofertas.models import Postular


class HomeView(View):

    def get(self, request):
        cargos = DescripcionCargo.objects.filter(estado_publicacion=ACTIVA).order_by('-id')
        empresas = Empresa.objects.all()
        context = {
            'descripcion_list': cargos[:5],
            'empresas': empresas
        }
        return render(request, 'ofertas/home.html', context)


class DetailView(View):

    def get(self, request, pk):
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

class CreateView(View):

    @method_decorator(login_required())
    def get(self, request):
        form = OfertaForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'ofertas/nueva_oferta.html', context)

    @method_decorator(login_required())
    def post(self, request):
        # Formulario para crear una oferta laboral
        success_message = ''
        form = OfertaForm(request.POST)
        if form.is_valid():
            nueva_oferta = form.save()
            form = OfertaForm()
            success_message = "Oferta creada con éxito.  "
            success_message += '<a href="{0}">'.format(reverse('ofertas_detail', args=[nueva_oferta.pk]))
            success_message += 'Ver oferta'
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'ofertas/nueva_oferta.html', context)

class ListView(View):
    def get(self, request):
        ofertas = DescripcionCargo.objects.all()
        context = {
            'ofertas': ofertas[:7]
        }

        return render(request, 'ofertas/ofertas_list.html', context)

class Postulacion(ListView):
    def get(self, request):
        modelo = Postular.objects.all()
        form = PostularForm
        context = {
            'modelo_postulacion': modelo,
            'form': form,
        }


        return render(request, 'ofertas/postulacion.html', context)


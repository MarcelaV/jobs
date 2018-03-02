# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# CLASE DESCRIPCIÓN
COMPLETA = 'COMPLETA'
MEDIA = 'MEDIA'
PART_TIME = 'PART_TIME'
TURNOS = 'TURNOS'

JORNADAS = (
    (COMPLETA, 'Completa'),
    (MEDIA, 'Media'),
    (PART_TIME, 'Part time'),
    (TURNOS, 'Turnos')
)

#CLASE REQUISITOS_CONTRATO
FIJO = 'FIJO'
INDEFINIDO = 'INDEFINIDO'
HONORARIOS = 'HONORARIOS'

CONTRATO = (
    (FIJO, 'Plazo fijo'),
    (INDEFINIDO, 'Indefinido'),
    (HONORARIOS, 'Honorarios')
)

#CLASE REQUISITOS_EDUCACION
PRACTICA = 'PRACTICA'
OFICIO = 'OFICIO'
TECNICA = 'TECNICA'
PROFESIONAL = 'PROFESIONAL'
UNIVERSITARIA = 'UNIVERSITARIA'
INDIFERENTE = 'INDIFERENTE'

EDUCACION = (
    (PRACTICA, 'Practicante'),
    (OFICIO, 'Nivel oficio'),
    (TECNICA, 'Nivel técnico'),
    (PROFESIONAL, 'Nivel profesional'),
    (UNIVERSITARIA, 'Nivel universitaria'),
    (INDIFERENTE, 'Indiferente')
)

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    anos_experiencia = models.IntegerField()

    def __unicode__(self):
        return self.nombre

class DescripcionCargo(models.Model):
    cargo = models.CharField(max_length=30)
    descripcion_cargo = models.TextField()
    ciudad = models.CharField(max_length=30)
    fecha_contratacion = models.DateField()
    sueldo = models.IntegerField()
    tipo_jornada = models.CharField(max_length=20, choices=JORNADAS)
    tipo_contrato = models.CharField(max_length=20, choices=CONTRATO)

    def __unicode__(self):
        return self.cargo

class Requisito(models.Model):
    nivel_educacional = models.CharField(max_length=20, choices=EDUCACION)
    carrera = models.CharField(max_length=30)
    experiencia = models.IntegerField()

    def __unicode__(self):
        return self.carrera




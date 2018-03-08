# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db import IntegrityError

# CLASE DESCRIPCIÓN
from django.forms import ModelForm

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

ACTIVA = 'ACTIVA'
INACTIVA = 'INACTIVA'

ESTADO_PUBLICACION = (
    (ACTIVA, 'Activa'),
    (INACTIVA, 'Inactiva')
)

ENFERMERO = 'ENFERMERIA'
KINESIOLOGO = 'KINESIOLOGO'
NUTRICIONISTA = 'NUTRICIONISTA'
ODONTOLOGO = 'ODONTOLOGO'
MATRON = 'MATRON'
TENS = 'TENS'
PARAMEDICO = 'PARAMEDICO'
PSICOLOGO = 'PSICOLOGO'
TECNOLOGO_MEDICO = "TECNOLOGO MEDICO"
INFORMATICO_BIOMEDICO = "INFORMATICO_BIOMEDICO"
MEDICO_GENERAL = 'MEDICO_GENERAL'
MEDICO_ESPECIALIDAD = 'MEDICO_ESPECIALIDAD'

CATEGORIAS = {
    (ENFERMERO, 'Enfermero/a'),
    (KINESIOLOGO, 'Kinesiólogo/a'),
    (NUTRICIONISTA, 'Nutricionista'),
    (ODONTOLOGO, 'Odontólogo/a'),
    (MATRON, 'Matron/a'),
    (TENS, 'TENS'),
    (PARAMEDICO, 'Paramédico/a'),
    (PSICOLOGO, 'Psicológo/a'),
    (TECNOLOGO_MEDICO, "Tecnológo/a médico"),
    (INFORMATICO_BIOMEDICO, "Informático/a Biomédico/a"),
    (MEDICO_GENERAL, 'Médico general'),
    (MEDICO_ESPECIALIDAD, 'Médica especialidad'),
}


class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    anos_experiencia = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.nombre

class DescripcionCargo(models.Model):
    owner = models.ForeignKey(Empresa)
    cargo = models.CharField(max_length=40, choices=CATEGORIAS)
    descripcion_cargo = models.TextField()
    ciudad = models.CharField(max_length=30)
    fecha_contratacion = models.DateField()
    sueldo = models.IntegerField()
    tipo_jornada = models.CharField(max_length=20, choices=JORNADAS)
    tipo_contrato = models.CharField(max_length=20, choices=CONTRATO)
    estado_publicacion = models.CharField(max_length=10, choices=ESTADO_PUBLICACION, default=ACTIVA)
    #created_at = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.cargo



class Postular(models.Model):
    postulante_oferta = models.ForeignKey(User, related_name='usuario')
    nivel_educacional = models.CharField(max_length=20, choices=EDUCACION)
    carrera = models.CharField(max_length=30)
    experiencia = models.IntegerField()
    descripcion_breve = models.TextField()

    def __unicode__(self):
        return self.carrera

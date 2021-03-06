# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0017_postular_postulante_oferta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcioncargo',
            name='cargo',
            field=models.CharField(choices=[('PARAMEDICO', 'Param\xe9dico/a'), ('INFORMATICO_BIOMEDICO', 'Inform\xe1tico/a Biom\xe9dico/a'), ('PSICOLOGO', 'Psicol\xf3go/a'), ('TECNOLOGO MEDICO', 'Tecnol\xf3go/a m\xe9dico'), ('MEDICO_GENERAL', 'M\xe9dico general'), ('KINESIOLOGO', 'Kinesi\xf3logo/a'), ('MEDICO_ESPECIALIDAD', 'M\xe9dica especialidad'), ('TENS', 'TENS'), ('ODONTOLOGO', 'Odont\xf3logo/a'), ('MATRON', 'Matron/a'), ('ENFERMERIA', 'Enfermero/a'), ('NUTRICIONISTA', 'Nutricionista')], max_length=40),
        ),
    ]

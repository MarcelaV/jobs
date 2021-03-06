# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-07 19:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0015_auto_20180306_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_educacional', models.CharField(choices=[('PRACTICA', 'Practicante'), ('OFICIO', 'Nivel oficio'), ('TECNICA', 'Nivel t\xe9cnico'), ('PROFESIONAL', 'Nivel profesional'), ('UNIVERSITARIA', 'Nivel universitaria'), ('INDIFERENTE', 'Indiferente')], max_length=20)),
                ('carrera', models.CharField(max_length=30)),
                ('experiencia', models.IntegerField()),
                ('descripcion_breve', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Requisito',
        ),
    ]

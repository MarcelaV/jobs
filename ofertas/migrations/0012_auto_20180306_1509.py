# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0011_descripcioncargo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcioncargo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
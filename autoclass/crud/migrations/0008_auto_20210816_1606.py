# Generated by Django 3.2.5 on 2021-08-16 19:06

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20210816_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='duracao_da_aula_minutos',
            field=models.PositiveSmallIntegerField(default=90, validators=[django.core.validators.MaxValueValidator(600, message='Sua aula deve durar menos de 10 horas')]),
        ),
        migrations.AlterField(
            model_name='aula',
            name='horario_de_inicio',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]

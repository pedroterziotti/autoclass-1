# Generated by Django 3.2.5 on 2021-08-24 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0028_auto_20210824_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='horario_de_inicio',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
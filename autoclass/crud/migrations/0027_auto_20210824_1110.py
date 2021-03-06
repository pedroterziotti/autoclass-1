# Generated by Django 3.2.5 on 2021-08-24 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0026_auto_20210824_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='horario_de_inicio',
            field=models.TimeField(default=datetime.datetime(2021, 8, 24, 11, 10, 47, 570693)),
        ),
        migrations.AlterField(
            model_name='aula',
            name='plataforma',
            field=models.CharField(choices=[('Zoom', 'Zoom'), ('Blackboard', 'Blackboard'), ('Teams', 'Teams'), ('Classroom', 'Classroom')], default='Teams', max_length=22),
        ),
    ]

# Generated by Django 3.2.5 on 2021-08-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20210816_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='dia_da_aula',
            field=models.CharField(choices=[('Segunda', 'Segunda'), ('Terça', 'Terça'), ('Quarta', 'Quarta'), ('Quinta', 'Quinta'), ('Sexta', 'Sexta'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=20),
        ),
    ]

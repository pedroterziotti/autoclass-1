# Generated by Django 3.2.5 on 2021-08-16 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_alter_aula_dia_da_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='link_da_aula',
            field=models.URLField(default=''),
        ),
    ]
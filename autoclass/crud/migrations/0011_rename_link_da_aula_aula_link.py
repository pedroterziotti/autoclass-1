# Generated by Django 3.2.5 on 2021-08-16 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_aula_link_da_aula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aula',
            old_name='link_da_aula',
            new_name='link',
        ),
    ]

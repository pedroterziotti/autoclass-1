# Generated by Django 3.2.5 on 2021-08-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0019_auto_20210823_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='password',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='aula',
            name='user',
            field=models.CharField(default='', max_length=300),
        ),
    ]

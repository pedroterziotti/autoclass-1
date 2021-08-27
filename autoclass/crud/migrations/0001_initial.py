# Generated by Django 3.2.5 on 2021-08-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('plataforma', models.CharField(choices=[('z', 'zoom'), ('b', 'blackboard'), ('t', 'teams'), ('c', 'classroom'), ('n', None)], default=None, max_length=2)),
            ],
        ),
    ]

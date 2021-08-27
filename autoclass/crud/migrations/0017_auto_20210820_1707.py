# Generated by Django 3.2.5 on 2021-08-20 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_users_zoom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='Zoom',
        ),
        migrations.AddField(
            model_name='users',
            name='Zoom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='crud.zoom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='zoom',
            name='passw',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AlterField(
            model_name='zoom',
            name='username',
            field=models.CharField(default='admin', max_length=300),
        ),
    ]

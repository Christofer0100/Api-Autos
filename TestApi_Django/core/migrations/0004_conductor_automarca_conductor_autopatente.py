# Generated by Django 4.2.7 on 2023-11-22 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_conductor'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='autoMarca',
            field=models.CharField(default=22, max_length=50, verbose_name='Marca del Auto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conductor',
            name='autoPatente',
            field=models.CharField(default=33, max_length=50, verbose_name='Patente del Auto'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0 on 2023-12-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_des', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='descripsion',
            new_name='descripcion',
        ),
    ]

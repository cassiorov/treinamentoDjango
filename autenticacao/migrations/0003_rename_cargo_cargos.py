# Generated by Django 4.0.6 on 2022-07-17 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_cargo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cargo',
            new_name='Cargos',
        ),
    ]
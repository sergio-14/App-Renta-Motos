# Generated by Django 5.0.6 on 2024-06-15 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('ndi', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('moto_id', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=50)),
                ('detalle', models.TextField()),
                ('tarifa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('ocupado', 'Ocupado')], default='disponible', max_length=10)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='motos_fotos/')),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('nacionalidad_id', models.AutoField(primary_key=True, serialize=False)),
                ('nacionalidad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoMoto',
            fields=[
                ('tipo_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('alquiler_id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('cantidad_horas', models.IntegerField()),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('ocupado', 'Ocupado')], default='disponible', max_length=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentamotos.cliente')),
                ('moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentamotos.moto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentamotos.nacionalidad'),
        ),
        migrations.AddField(
            model_name='moto',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentamotos.tipomoto'),
        ),
    ]
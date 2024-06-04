# Generated by Django 5.0.4 on 2024-05-26 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('telefono', models.IntegerField(blank=True, null=True, verbose_name='Telefono')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Responsable departamento')),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
                'db_table': 'Departamentos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PuestoTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RRHH.departamento', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Puesto de trabajo',
                'verbose_name_plural': 'Puestos de trabajos',
                'db_table': 'PuestosTrabajos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(blank=True, max_length=40, null=True, verbose_name='DNI')),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('direccion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empleados/', verbose_name='Imagen')),
                ('antiguedad', models.IntegerField(blank=True, default=0, null=True, verbose_name='Antiguedad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RRHH.departamento', verbose_name='Departamento')),
                ('user', models.ForeignKey(limit_choices_to={'group__name': 'empleados'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Empleado')),
                ('puestoTrabajo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='RRHH.puestotrabajo', verbose_name='Puesto')),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
                'db_table': 'Empleados',
                'ordering': ['id'],
            },
        ),
    ]

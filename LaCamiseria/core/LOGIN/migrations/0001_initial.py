# Generated by Django 5.0.4 on 2024-05-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('descripcion', models.CharField(max_length=256)),
                ('fecha_vencimiento', models.DateTimeField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'Tasks',
                'ordering': ['nombre'],
            },
        ),
    ]

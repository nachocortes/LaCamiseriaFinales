# Generated by Django 5.0.4 on 2024-05-28 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_clientevalidator'),
        ('VENTAS', '0009_alter_pedido_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='clienteValidator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='CRM.clientevalidator'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-26 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VENTAS', '0002_remove_pedido_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='fechaPedido',
        ),
    ]

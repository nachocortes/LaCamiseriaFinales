from django.contrib.auth.models import User
from django.db import models

from core.CRM.models import Cliente, Direccion
from core.STORE.models import Producto, Variante


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='pedidos', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=250)
    codigo_postal = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Pedidos'
        verbose_name = "producto"
        verbose_name_plural = "pedidos"
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']), ]

    def __str__(self):
        return self.cliente.nombre

    def obtener_total_coste(self):
        return sum(item.obtener_coste() for item in self.items.all())


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='productosPedido', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def obtener_coste(self):
        return self.precio * self.cantidad

    class Meta:
        db_table = 'PedidoItems'
        verbose_name = "pedido item"
        verbose_name_plural = "pedidos items"
        indexes = [models.Index(fields=['id']), ]
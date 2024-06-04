from django.db import models



class Task(models.Model):
    nombre = models.CharField(max_length=256)
    descripcion = models.CharField(max_length=256)
    fecha_vencimiento = models.DateTimeField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['nombre']
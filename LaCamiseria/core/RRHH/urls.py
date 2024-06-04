from django.urls import path, include
from .views import (
    DepartamentoListApiView,
    DepartamentoDetailApiView, EmpleadoDetailApiView, EmpleadoListApiView,
    PuestoTrabajoListApiView
)

urlpatterns = [
    path('departamentos', DepartamentoListApiView.as_view()),
    path('departamentos/<int:departamento_id>', DepartamentoDetailApiView.as_view()),
    path('puestosTrabajos', PuestoTrabajoListApiView.as_view()),
    path('puestosTrabajos/<int:habilidad_id>', PuestoTrabajoListApiView.as_view()),
    path('empleados', EmpleadoListApiView.as_view()),
    path('empleados/<int:empleado_id>', EmpleadoDetailApiView.as_view()),
]